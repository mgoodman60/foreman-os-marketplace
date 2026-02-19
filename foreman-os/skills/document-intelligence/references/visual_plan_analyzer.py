#!/usr/bin/env python3
"""
Visual Plan Analyzer - Construction Plan Sheet Analysis Pipeline

A comprehensive multi-pass extraction pipeline for analyzing construction plan sheets.
Performs sheet layout detection, OCR extraction, line detection, symbol detection,
material zone identification, dimension extraction, and scale calibration.

Author: Foreman OS Document Intelligence Team
License: Proprietary
"""

import os
import sys
import json
import argparse
import re
import warnings
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import traceback

import cv2
import numpy as np
from skimage import filters, feature, img_as_float, img_as_uint
from skimage.morphology import binary_dilation, binary_erosion
from sklearn.cluster import DBSCAN
import logging

# Suppress warnings
warnings.filterwarnings('ignore')
os.environ['PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK'] = 'True'

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

# Optional imports with graceful fallback
try:
    from paddleocr import PaddleOCR
    PADDLE_AVAILABLE = True
except ImportError:
    logger.warning("PaddleOCR not available, will use OpenCV text detection only")
    PADDLE_AVAILABLE = False

try:
    from craft_text_detector import Craft
    CRAFT_AVAILABLE = True
except ImportError:
    logger.warning("CRAFT text detector not available")
    CRAFT_AVAILABLE = False


# =============================================================================
# Data Classes and Enums
# =============================================================================

class ZoneType(Enum):
    """Zone classification enumeration."""
    TITLE_BLOCK = "title_block"
    PLAN = "plan"
    DETAIL = "detail"
    SCHEDULE = "schedule"
    NOTES = "notes"
    LEGEND = "legend"
    MARGIN = "margin"
    GENERAL = "general"


class LineType(Enum):
    """Line classification enumeration."""
    WALL = "wall"
    DIMENSION = "dimension"
    GRID = "grid"
    LEADER = "leader"
    SECTION_CUT = "section_cut"
    HATCH = "hatch"
    UNKNOWN = "unknown"


class SymbolType(Enum):
    """Symbol classification enumeration."""
    DOOR_SWING = "door_swing"
    SECTION_MARKER = "section_marker"
    ELEVATION_MARKER = "elevation_marker"
    EQUIPMENT = "equipment"
    WINDOW = "window"
    FIXTURE = "fixture"
    UNKNOWN = "unknown"


class MaterialType(Enum):
    """Material hatch pattern classification."""
    CONCRETE = "concrete"
    EARTH = "earth"
    INSULATION = "insulation"
    WOOD = "wood"
    STEEL = "steel"
    MASONRY = "masonry"
    WATER = "water"
    UNKNOWN = "unknown"


@dataclass
class TextExtraction:
    """OCR extracted text entry."""
    content: str
    bbox: Tuple[float, float, float, float]  # (x_min, y_min, x_max, y_max)
    confidence: float
    zone_type: Optional[ZoneType] = None
    text_type: Optional[str] = None  # 'room_number', 'dimension', 'elevation', etc.
    rotation: float = 0.0


@dataclass
class LineSegment:
    """Detected line segment."""
    x1: float
    y1: float
    x2: float
    y2: float
    line_type: LineType
    thickness: float
    confidence: float
    associated_text: List[str] = None

    def __post_init__(self):
        if self.associated_text is None:
            self.associated_text = []


@dataclass
class DetectedSymbol:
    """Detected symbol or marker."""
    symbol_type: SymbolType
    bbox: Tuple[float, float, float, float]
    centroid: Tuple[float, float]
    confidence: float
    label: Optional[str] = None
    properties: Dict[str, Any] = None

    def __post_init__(self):
        if self.properties is None:
            self.properties = {}


@dataclass
class MaterialZone:
    """Detected material/hatch pattern zone."""
    material_type: MaterialType
    contour: np.ndarray  # polygon vertices
    area_pixels: float
    area_real: Optional[float] = None  # in square feet
    confidence: float = 0.8
    bbox: Tuple[float, float, float, float] = None


@dataclass
class Dimension:
    """Extracted dimension with associated line."""
    value: str
    unit: str
    numeric_value: Optional[float] = None
    x1: float = 0.0
    y1: float = 0.0
    x2: float = 0.0
    y2: float = 0.0
    confidence: float = 0.8


@dataclass
class ZoneMapEntry:
    """Zone map entry."""
    zone_type: ZoneType
    bbox: Tuple[float, float, float, float]
    text_density: float = 0.0
    confidence: float = 0.8


@dataclass
class ScaleCalibration:
    """Scale calibration data."""
    scale_string: str  # e.g., "1/4\" = 1'-0\""
    pixels_per_foot: Optional[float] = None
    scale_factor: Optional[float] = None  # e.g., 1/48 for 1/4" = 1'-0"
    confidence: float = 0.8
    location: Optional[Tuple[float, float]] = None


# =============================================================================
# Pass 1: Sheet Layout Detection
# =============================================================================

def detect_sheet_layout(image: np.ndarray, dpi: int = 300) -> Dict[str, Any]:
    """
    Detect outer border, identify zones (title block, plan areas, details, schedules).

    Args:
        image: Input image (BGR)
        dpi: DPI value for scaling calculations

    Returns:
        Dictionary with zone map and detected regions
    """
    logger.info("Pass 1: Sheet Layout Detection")

    height, width = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Edge detection
    edges = cv2.Canny(gray, 50, 150)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    edges = cv2.dilate(edges, kernel, iterations=1)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find outer border (largest rectangle)
    largest_area = 0
    outer_border = None
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            area = cv2.contourArea(approx)
            if area > largest_area:
                largest_area = area
                outer_border = cv2.boundingRect(approx)

    zones = []

    # Detect title block: typically in lower-right corner
    # Title blocks have high text density
    if outer_border:
        x, y, w, h = outer_border
        # Title block is roughly 20-30% of width, 20-30% of height, bottom-right
        title_block_x = int(x + 0.7 * w)
        title_block_y = int(y + 0.7 * h)
        title_block_w = int(0.28 * w)
        title_block_h = int(0.28 * h)
        title_bbox = (title_block_x, title_block_y, title_block_x + title_block_w, title_block_y + title_block_h)

        zones.append(ZoneMapEntry(
            zone_type=ZoneType.TITLE_BLOCK,
            bbox=title_bbox,
            confidence=0.85
        ))

        # Main plan area (upper-left to middle)
        plan_bbox = (x + 10, y + 10, int(x + 0.7 * w), int(y + 0.7 * h))
        zones.append(ZoneMapEntry(
            zone_type=ZoneType.PLAN,
            bbox=plan_bbox,
            confidence=0.9
        ))

        # Detail areas (typically top-right and/or bottom-left)
        detail_bbox_tr = (int(x + 0.7 * w), y + 10, int(x + w - 10), int(y + 0.35 * h))
        zones.append(ZoneMapEntry(
            zone_type=ZoneType.DETAIL,
            bbox=detail_bbox_tr,
            confidence=0.75
        ))

        # Notes/legend areas (typically left side or top)
        notes_bbox = (x + 10, int(y + 0.35 * h), int(x + 0.25 * w), int(y + 0.7 * h))
        zones.append(ZoneMapEntry(
            zone_type=ZoneType.NOTES,
            bbox=notes_bbox,
            confidence=0.7
        ))

    return {
        "zones": [asdict(z) for z in zones],
        "outer_border": outer_border,
        "sheet_dimensions": (width, height)
    }


# =============================================================================
# Pass 2: Full OCR Extraction
# =============================================================================

def extract_text_paddle(image: np.ndarray) -> List[TextExtraction]:
    """
    Extract text using PaddleOCR with comprehensive bounding boxes and confidence.

    Args:
        image: Input image (BGR)

    Returns:
        List of TextExtraction objects
    """
    logger.info("Pass 2a: OCR Extraction (PaddleOCR)")

    if not PADDLE_AVAILABLE:
        logger.warning("PaddleOCR not available, skipping Paddle extraction")
        return []

    try:
        ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)
        results = ocr.ocr(image, cls=True)

        extractions = []
        for line_idx, line in enumerate(results):
            if line is None:
                continue
            for word_result in line:
                points, (text, confidence) = word_result
                # Convert points to bounding box
                points = np.array(points, dtype=np.float32)
                x_coords = points[:, 0]
                y_coords = points[:, 1]
                bbox = (float(x_coords.min()), float(y_coords.min()),
                       float(x_coords.max()), float(y_coords.max()))

                extraction = TextExtraction(
                    content=text,
                    bbox=bbox,
                    confidence=float(confidence),
                    text_type=classify_text_type(text)
                )
                extractions.append(extraction)

        logger.info(f"Extracted {len(extractions)} text elements via PaddleOCR")
        return extractions

    except Exception as e:
        logger.error(f"PaddleOCR extraction failed: {e}")
        return []


def extract_text_opencv(image: np.ndarray) -> List[TextExtraction]:
    """
    Fallback OCR using OpenCV text detection and Tesseract if available.

    Args:
        image: Input image (BGR)

    Returns:
        List of TextExtraction objects
    """
    logger.info("Pass 2b: OCR Extraction (OpenCV Fallback)")

    extractions = []

    # Try to use CRAFT if available
    if CRAFT_AVAILABLE:
        try:
            craft = Craft(output_dir=None, crop_type="poly", cuda=False)
            prediction_result = craft.detect_text(image)

            if 'boxes' in prediction_result:
                for box_idx, box in enumerate(prediction_result['boxes']):
                    if box is not None:
                        x_coords = [p[0] for p in box]
                        y_coords = [p[1] for p in box]
                        bbox = (min(x_coords), min(y_coords), max(x_coords), max(y_coords))

                        extraction = TextExtraction(
                            content=f"text_{box_idx}",
                            bbox=bbox,
                            confidence=0.6
                        )
                        extractions.append(extraction)

            logger.info(f"Extracted {len(extractions)} text regions via CRAFT")
        except Exception as e:
            logger.warning(f"CRAFT text detection failed: {e}")

    return extractions


def classify_text_type(text: str) -> str:
    """
    Classify text type based on pattern matching.

    Args:
        text: Text string to classify

    Returns:
        Classification string
    """
    text_lower = text.lower().strip()

    # Room number: 3-4 digits
    if re.match(r'^\d{3,4}$', text):
        return 'room_number'

    # Dimension: X'-Y" or X'
    if re.search(r"\d+['\u2019]\s*-?\s*\d*\s*[\"″\u201D]?", text):
        return 'dimension'

    # Elevation: EL followed by number
    if re.match(r'^EL\.?\s*[\d\.\-\+]+', text):
        return 'elevation'

    # Spec reference: section + number (like "A2.1")
    if re.match(r'^[A-Z]+[\d\.]+', text):
        return 'spec_reference'

    # Scale notation
    if re.match(r'^[\d\.\-]*/[\d\.\-]+', text) or re.match(r'^1:[\d]+', text):
        return 'scale'

    # Grid label: single letter or number
    if re.match(r'^[A-Z]$|^[\d]$', text):
        return 'grid_label'

    return 'general_text'


def extract_title_block_text(texts: List[TextExtraction], title_zone: Tuple) -> Dict[str, str]:
    """
    Extract structured data from title block text.

    Args:
        texts: List of extracted text elements
        title_zone: Bounding box of title block

    Returns:
        Dictionary with extracted title block data
    """
    logger.info("Pass 2c: Title Block Extraction")

    title_data = {
        "project_name": None,
        "sheet_number": None,
        "sheet_title": None,
        "scale": None,
        "date": None,
        "revision": None
    }

    if title_zone is None:
        return title_data

    tx_min, ty_min, tx_max, ty_max = title_zone

    # Filter texts in title block
    title_texts = []
    for text in texts:
        bx_min, by_min, bx_max, by_max = text.bbox
        if (bx_min >= tx_min and bx_max <= tx_max and
            by_min >= ty_min and by_max <= ty_max):
            title_texts.append(text)

    # Sort by position
    title_texts.sort(key=lambda t: (t.bbox[1], t.bbox[0]))

    # Try to identify structured fields
    for idx, text in enumerate(title_texts):
        content = text.content.lower()

        if re.search(r'sheet|sheet\s*no', content):
            if idx + 1 < len(title_texts):
                title_data['sheet_number'] = title_texts[idx + 1].content
        elif re.search(r'scale', content):
            if idx + 1 < len(title_texts):
                title_data['scale'] = title_texts[idx + 1].content
        elif re.search(r'date|dated', content):
            if idx + 1 < len(title_texts):
                title_data['date'] = title_texts[idx + 1].content
        elif re.search(r'revision|rev', content):
            if idx + 1 < len(title_texts):
                title_data['revision'] = title_texts[idx + 1].content

    # First few large texts likely project name
    if title_texts:
        title_data['project_name'] = title_texts[0].content

    return title_data


def extract_all_text(image: np.ndarray, zones: List[ZoneMapEntry]) -> List[TextExtraction]:
    """
    Main OCR extraction function combining multiple methods.

    Args:
        image: Input image
        zones: Detected zones from Pass 1

    Returns:
        List of extracted text elements
    """
    logger.info("Pass 2: Full OCR Extraction")

    # Primary: PaddleOCR
    texts = extract_text_paddle(image)

    # Fallback: OpenCV methods
    if not texts:
        texts = extract_text_opencv(image)

    # Assign zone types
    for text in texts:
        for zone in zones:
            zx_min, zy_min, zx_max, zy_max = zone['bbox']
            tx_min, ty_min, tx_max, ty_max = text.bbox
            if (tx_min >= zx_min and tx_max <= zx_max and
                ty_min >= zy_min and ty_max <= zy_max):
                text.zone_type = ZoneType(zone['zone_type'])
                break

    return texts


# =============================================================================
# Pass 3: Line Detection and Classification
# =============================================================================

def detect_and_classify_lines(image: np.ndarray) -> List[LineSegment]:
    """
    Detect and classify lines: walls, dimensions, grids, leaders, section cuts.

    Args:
        image: Input image (BGR)

    Returns:
        List of LineSegment objects
    """
    logger.info("Pass 3: Line Detection and Classification")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    # Adaptive thresholding for better edge detection
    threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 11, 2)

    # Canny edge detection
    edges = cv2.Canny(threshold, 50, 150)

    # Detect lines using HoughLinesP
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=20, maxLineGap=10)

    line_segments = []

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            thickness = estimate_line_thickness(gray, x1, y1, x2, y2)

            # Classify line type
            line_type = classify_line(x1, y1, x2, y2, length, thickness, width, height)

            segment = LineSegment(
                x1=float(x1),
                y1=float(y1),
                x2=float(x2),
                y2=float(y2),
                line_type=line_type,
                thickness=float(thickness),
                confidence=0.8
            )
            line_segments.append(segment)

    logger.info(f"Detected and classified {len(line_segments)} line segments")
    return line_segments


def estimate_line_thickness(gray: np.ndarray, x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Estimate thickness of a line segment.

    Args:
        gray: Grayscale image
        x1, y1, x2, y2: Line endpoints

    Returns:
        Estimated thickness in pixels
    """
    # Simple approach: sample perpendicular to line
    dx = x2 - x1
    dy = y2 - y1
    length = np.sqrt(dx ** 2 + dy ** 2)

    if length < 1:
        return 1.0

    # Perpendicular direction
    px = -dy / length
    py = dx / length

    # Count pixels along perpendicular
    thickness = 1.0
    for offset in range(1, 10):
        x_sample = int(x1 + px * offset)
        y_sample = int(y1 + py * offset)

        if 0 <= x_sample < gray.shape[1] and 0 <= y_sample < gray.shape[0]:
            if gray[y_sample, x_sample] > 128:
                thickness += 1.0
            else:
                break

    return thickness


def classify_line(x1: float, y1: float, x2: float, y2: float, length: float,
                  thickness: float, width: int, height: int) -> LineType:
    """
    Classify a detected line based on characteristics.

    Args:
        x1, y1, x2, y2: Line endpoints
        length: Line length
        thickness: Line thickness
        width, height: Image dimensions

    Returns:
        LineType classification
    """
    # Thick lines (>2px) are likely walls
    if thickness > 2.0:
        return LineType.WALL

    # Long spanning lines (>50% of dimension) are likely grid lines
    max_span = max(width, height)
    if length > max_span * 0.5:
        return LineType.GRID

    # Angled lines are likely leaders
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if dx > 0 and dy > 0:
        angle = abs(dy / (dx + 1e-6))
        if 0.3 < angle < 3.0:
            return LineType.LEADER

    # Thin lines with moderate length are dimension lines
    if thickness <= 1.0 and 20 < length < 500:
        return LineType.DIMENSION

    # Check for dashed pattern (section cuts)
    # This is a simplified check
    if thickness > 1.5:
        return LineType.SECTION_CUT

    return LineType.UNKNOWN


# =============================================================================
# Pass 4: Symbol Detection
# =============================================================================

def detect_symbols(image: np.ndarray, texts: List[TextExtraction]) -> List[DetectedSymbol]:
    """
    Detect and classify symbols: doors, sections, elevations, equipment, windows.

    Args:
        image: Input image (BGR)
        texts: Extracted text elements (for association)

    Returns:
        List of DetectedSymbol objects
    """
    logger.info("Pass 4: Symbol Detection")

    symbols = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    # Detect circles (section markers, elevation markers)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                               param1=50, param2=30, minRadius=5, maxRadius=50)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            x, y, r = circle
            bbox = (float(x - r), float(y - r), float(x + r), float(y + r))
            label = find_nearest_text(texts, (float(x), float(y)))

            symbol = DetectedSymbol(
                symbol_type=SymbolType.SECTION_MARKER,
                bbox=bbox,
                centroid=(float(x), float(y)),
                confidence=0.75,
                label=label
            )
            symbols.append(symbol)

    # Detect rectangular equipment/fixtures
    threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 11, 2)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:  # Rectangle
            x, y, w, h = cv2.boundingRect(approx)
            area = w * h

            # Filter by size: equipment/fixtures typically 20-500 px²
            if 20 < area < 500:
                bbox = (float(x), float(y), float(x + w), float(y + h))
                label = find_nearest_text(texts, (float(x + w / 2), float(y + h / 2)))

                symbol = DetectedSymbol(
                    symbol_type=SymbolType.EQUIPMENT,
                    bbox=bbox,
                    centroid=(float(x + w / 2), float(y + h / 2)),
                    confidence=0.7,
                    label=label
                )
                symbols.append(symbol)

    logger.info(f"Detected {len(symbols)} symbols")
    return symbols


def find_nearest_text(texts: List[TextExtraction], point: Tuple[float, float],
                      max_distance: float = 100.0) -> Optional[str]:
    """
    Find text nearest to a given point.

    Args:
        texts: List of text extractions
        point: (x, y) point
        max_distance: Maximum distance to consider

    Returns:
        Nearest text content or None
    """
    nearest = None
    min_dist = max_distance

    for text in texts:
        tx_min, ty_min, tx_max, ty_max = text.bbox
        text_center = ((tx_min + tx_max) / 2, (ty_min + ty_max) / 2)
        dist = np.sqrt((text_center[0] - point[0]) ** 2 + (text_center[1] - point[1]) ** 2)

        if dist < min_dist:
            min_dist = dist
            nearest = text.content

    return nearest


# =============================================================================
# Pass 5: Material Zone / Hatch Pattern Detection
# =============================================================================

def detect_material_zones(image: np.ndarray) -> List[MaterialZone]:
    """
    Detect and classify material zones based on texture patterns.

    Args:
        image: Input image (BGR)

    Returns:
        List of MaterialZone objects
    """
    logger.info("Pass 5: Material Zone Detection")

    zones = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_float = img_as_float(gray)

    height, width = gray.shape

    # Use Gabor filter banks to detect patterns
    gabor_responses = []
    for frequency in [0.05, 0.1, 0.15]:
        for angle in [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]:
            try:
                real, imag = filters.gabor(gray_float, frequency=frequency, theta=angle)
                response = np.sqrt(real ** 2 + imag ** 2)
                gabor_responses.append(response)
            except Exception as e:
                logger.debug(f"Gabor filter error: {e}")
                continue

    if not gabor_responses:
        logger.warning("No Gabor responses generated")
        return zones

    # Combine responses
    combined_response = np.mean(gabor_responses, axis=0)

    # Threshold to get pattern regions
    threshold = cv2.adaptiveThreshold((combined_response * 255).astype(np.uint8),
                                      255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 15, 2)

    # Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area_pixels = cv2.contourArea(contour)

        # Filter by area (avoid noise)
        if area_pixels < 100:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        bbox = (float(x), float(y), float(x + w), float(y + h))

        # Classify material type based on texture response
        material_type = classify_material_pattern(contour, gray, gabor_responses)

        zone = MaterialZone(
            material_type=material_type,
            contour=contour,
            area_pixels=float(area_pixels),
            bbox=bbox,
            confidence=0.7
        )
        zones.append(zone)

    logger.info(f"Detected {len(zones)} material zones")
    return zones


def classify_material_pattern(contour: np.ndarray, gray: np.ndarray,
                              gabor_responses: List[np.ndarray]) -> MaterialType:
    """
    Classify material pattern based on texture analysis.

    Args:
        contour: Contour region
        gray: Grayscale image
        gabor_responses: Gabor filter responses

    Returns:
        MaterialType classification
    """
    # Create mask for contour
    mask = np.zeros(gray.shape, dtype=np.uint8)
    cv2.drawContours(mask, [contour], 0, 255, -1)

    # Calculate LBP (Local Binary Pattern) within region
    try:
        gray_float = img_as_float(gray)
        lbp = feature.local_binary_pattern(gray_float, P=8, R=1, method='uniform')
        lbp_hist, _ = np.histogram(lbp[mask > 0], bins=256, range=(0, 256))
        entropy = -np.sum(lbp_hist / (lbp_hist.sum() + 1e-6) *
                         np.log(lbp_hist / (lbp_hist.sum() + 1e-6) + 1e-6))
    except Exception:
        entropy = 0.5

    # Simple heuristic classification
    if entropy < 0.3:
        return MaterialType.EARTH
    elif entropy < 0.6:
        return MaterialType.CONCRETE
    elif entropy < 1.0:
        return MaterialType.INSULATION
    else:
        return MaterialType.WOOD

    return MaterialType.UNKNOWN


# =============================================================================
# Pass 6: Dimension Extraction
# =============================================================================

def extract_dimensions(texts: List[TextExtraction],
                       lines: List[LineSegment]) -> List[Dimension]:
    """
    Extract dimensions by pairing dimension text with dimension lines.

    Args:
        texts: Extracted text elements
        lines: Detected line segments

    Returns:
        List of Dimension objects
    """
    logger.info("Pass 6: Dimension Extraction")

    dimensions = []
    dimension_regex = r"(\d+)['\u2019]\s*-?\s*(\d+)\s*[\"″\u201D]?|(\d+)['\u2019](?!\s*-)|(\d+)\s*[\"″\u201D]"

    # Extract dimension text
    dimension_texts = [t for t in texts if t.text_type == 'dimension']

    for dim_text in dimension_texts:
        match = re.search(dimension_regex, dim_text.content)
        if match:
            # Extract numeric value
            if match.group(1) and match.group(2):
                feet = int(match.group(1))
                inches = int(match.group(2))
                numeric_value = feet + inches / 12.0
                unit = "ft-in"
            elif match.group(3):
                numeric_value = float(match.group(3))
                unit = "ft"
            elif match.group(4):
                numeric_value = float(match.group(4))
                unit = "in"
            else:
                continue

            # Find nearest dimension line
            nearest_line = find_nearest_line(dim_text, lines, max_distance=100)

            if nearest_line:
                dimension = Dimension(
                    value=dim_text.content,
                    unit=unit,
                    numeric_value=numeric_value,
                    x1=nearest_line.x1,
                    y1=nearest_line.y1,
                    x2=nearest_line.x2,
                    y2=nearest_line.y2,
                    confidence=dim_text.confidence
                )
                dimensions.append(dimension)

    logger.info(f"Extracted {len(dimensions)} dimensions")
    return dimensions


def find_nearest_line(text: TextExtraction, lines: List[LineSegment],
                      max_distance: float = 100.0) -> Optional[LineSegment]:
    """
    Find line nearest to a text element.

    Args:
        text: Text extraction
        lines: List of line segments
        max_distance: Maximum distance threshold

    Returns:
        Nearest line or None
    """
    tx_min, ty_min, tx_max, ty_max = text.bbox
    text_center = ((tx_min + tx_max) / 2, (ty_min + ty_max) / 2)

    nearest = None
    min_dist = max_distance

    for line in lines:
        if line.line_type != LineType.DIMENSION:
            continue

        # Distance from text center to line segment
        line_center = ((line.x1 + line.x2) / 2, (line.y1 + line.y2) / 2)
        dist = np.sqrt((line_center[0] - text_center[0]) ** 2 +
                      (line_center[1] - text_center[1]) ** 2)

        if dist < min_dist:
            min_dist = dist
            nearest = line

    return nearest


# =============================================================================
# Pass 7: Scale Detection
# =============================================================================

def detect_scale(image: np.ndarray, texts: List[TextExtraction],
                 title_zone: Optional[Tuple]) -> List[ScaleCalibration]:
    """
    Detect scale from graphic scale bars and text labels.

    Args:
        image: Input image (BGR)
        texts: Extracted text elements
        title_zone: Bounding box of title block

    Returns:
        List of ScaleCalibration objects
    """
    logger.info("Pass 7: Scale Detection")

    scales = []

    # Search for text-based scales in title block and texts
    for text in texts:
        if text.text_type == 'scale':
            scale_calib = parse_scale_text(text.content, text.bbox)
            if scale_calib:
                scales.append(scale_calib)

    # Also search for common scale patterns
    common_scales = [
        ("1/4\" = 1'-0\"", 1/48),
        ("1/8\" = 1'-0\"", 1/96),
        ("1/2\" = 1'-0\"", 1/24),
        ("1\" = 1'-0\"", 1/12),
        ("1/4\"", 1/48),
        ("1:48", 1/48),
        ("1:96", 1/96),
    ]

    for scale_text, scale_factor in common_scales:
        for text in texts:
            if scale_text.lower() in text.content.lower():
                scale_calib = ScaleCalibration(
                    scale_string=scale_text,
                    scale_factor=scale_factor,
                    confidence=0.8,
                    location=(text.bbox[0], text.bbox[1])
                )
                scales.append(scale_calib)

    logger.info(f"Detected {len(scales)} scale calibrations")
    return scales


def parse_scale_text(text: str, bbox: Tuple) -> Optional[ScaleCalibration]:
    """
    Parse scale notation from text.

    Args:
        text: Text content
        bbox: Bounding box

    Returns:
        ScaleCalibration or None
    """
    # Match patterns like "1/4\" = 1'-0\""
    match = re.search(r"(\d+)/(\d+)[\"′]?\s*=\s*(\d+)['\u2019]\s*-?\s*(\d*)\s*[\"″]?", text)
    if match:
        scale_numerator = float(match.group(1))
        scale_denominator = float(match.group(2))
        feet = float(match.group(3))
        inches = float(match.group(4)) if match.group(4) else 0

        feet_total = feet + inches / 12.0
        scale_factor = (scale_numerator / scale_denominator) / feet_total

        return ScaleCalibration(
            scale_string=text,
            scale_factor=scale_factor,
            confidence=0.85,
            location=bbox[:2]
        )

    return None


# =============================================================================
# Main Pipeline and Visualization
# =============================================================================

def create_annotated_image(image: np.ndarray, result: Dict[str, Any]) -> np.ndarray:
    """
    Create annotated image with overlays from all passes.

    Args:
        image: Original image
        result: Pipeline result dictionary

    Returns:
        Annotated image
    """
    logger.info("Creating annotated image")

    annotated = image.copy()

    # Draw zones from Pass 1
    for zone in result.get('pass_1', {}).get('zones', []):
        x_min, y_min, x_max, y_max = zone['bbox']
        color = (0, 255, 0)  # Green
        cv2.rectangle(annotated, (int(x_min), int(y_min)), (int(x_max), int(y_max)), color, 2)
        cv2.putText(annotated, zone['zone_type'], (int(x_min), int(y_min) - 10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # Draw text bboxes from Pass 2
    for text in result.get('pass_2', {}).get('texts', [])[:50]:  # Limit for clarity
        x_min, y_min, x_max, y_max = text['bbox']
        color = (255, 0, 0)  # Blue
        cv2.rectangle(annotated, (int(x_min), int(y_min)), (int(x_max), int(y_max)), color, 1)

    # Draw lines from Pass 3
    for line in result.get('pass_3', {}).get('lines', [])[:100]:
        color_map = {
            'wall': (0, 0, 255),
            'dimension': (255, 255, 0),
            'grid': (255, 0, 255),
            'leader': (0, 255, 255),
            'section_cut': (128, 0, 255),
        }
        color = color_map.get(line['line_type'], (128, 128, 128))
        cv2.line(annotated, (int(line['x1']), int(line['y1'])),
                (int(line['x2']), int(line['y2'])), color, 1)

    # Draw symbols from Pass 4
    for symbol in result.get('pass_4', {}).get('symbols', []):
        x_min, y_min, x_max, y_max = symbol['bbox']
        cx, cy = symbol['centroid']
        cv2.circle(annotated, (int(cx), int(cy)), 5, (0, 165, 255), -1)  # Orange
        if symbol['label']:
            cv2.putText(annotated, symbol['label'], (int(x_min), int(y_min) - 5),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 165, 255), 1)

    return annotated


def run_pipeline(image_path: str, dpi: int = 300,
                 passes: Optional[List[int]] = None,
                 annotate_output: Optional[str] = None) -> Dict[str, Any]:
    """
    Main pipeline execution.

    Args:
        image_path: Path to input image
        dpi: DPI value
        passes: List of passes to run (default: all)
        annotate_output: Optional output path for annotated image

    Returns:
        Dictionary with all extraction results
    """
    logger.info(f"Starting visual plan analysis pipeline on {image_path}")

    if passes is None:
        passes = [1, 2, 3, 4, 5, 6, 7]

    image = cv2.imread(image_path)
    if image is None:
        logger.error(f"Failed to load image: {image_path}")
        return {"error": f"Failed to load image: {image_path}"}

    result = {
        "image_path": image_path,
        "image_shape": image.shape,
        "dpi": dpi,
        "passes_executed": passes
    }

    try:
        # Pass 1: Sheet Layout Detection
        if 1 in passes:
            pass_1_result = detect_sheet_layout(image, dpi)
            result['pass_1'] = pass_1_result
            zones = [ZoneMapEntry(**z) for z in pass_1_result['zones']]
            title_zone = zones[0].bbox if zones else None
        else:
            zones = []
            title_zone = None

        # Pass 2: OCR Extraction
        if 2 in passes:
            texts = extract_all_text(image, zones)
            title_block = extract_title_block_text(texts, title_zone) if title_zone else {}
            result['pass_2'] = {
                "texts": [asdict(t) for t in texts],
                "title_block": title_block,
                "text_count": len(texts)
            }
        else:
            texts = []

        # Pass 3: Line Detection
        if 3 in passes:
            lines = detect_and_classify_lines(image)
            result['pass_3'] = {
                "lines": [asdict(l) for l in lines],
                "line_count": len(lines)
            }
        else:
            lines = []

        # Pass 4: Symbol Detection
        if 4 in passes:
            symbols = detect_symbols(image, texts)
            result['pass_4'] = {
                "symbols": [asdict(s) for s in symbols],
                "symbol_count": len(symbols)
            }

        # Pass 5: Material Zones
        if 5 in passes:
            materials = detect_material_zones(image)
            result['pass_5'] = {
                "material_zones": [
                    {
                        "material_type": m.material_type.value,
                        "area_pixels": m.area_pixels,
                        "bbox": m.bbox,
                        "confidence": m.confidence
                    } for m in materials
                ],
                "material_count": len(materials)
            }

        # Pass 6: Dimension Extraction
        if 6 in passes:
            dimensions = extract_dimensions(texts, lines)
            result['pass_6'] = {
                "dimensions": [asdict(d) for d in dimensions],
                "dimension_count": len(dimensions)
            }

        # Pass 7: Scale Detection
        if 7 in passes:
            scales = detect_scale(image, texts, title_zone)
            result['pass_7'] = {
                "scales": [asdict(s) for s in scales],
                "scale_count": len(scales)
            }

        # Create annotated image if requested
        if annotate_output:
            annotated = create_annotated_image(image, result)
            cv2.imwrite(annotate_output, annotated)
            logger.info(f"Annotated image saved to {annotate_output}")
            result['annotated_image_path'] = annotate_output

    except Exception as e:
        logger.error(f"Pipeline error: {e}")
        logger.error(traceback.format_exc())
        result['error'] = str(e)

    logger.info("Pipeline execution complete")
    return result


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Visual Plan Analyzer - Construction Plan Sheet Analysis Pipeline"
    )
    parser.add_argument('input', help='Input image path')
    parser.add_argument('--output', help='Output JSON path', default=None)
    parser.add_argument('--passes', help='Comma-separated pass numbers (default: 1,2,3,4,5,6,7)',
                       default='1,2,3,4,5,6,7')
    parser.add_argument('--dpi', type=int, help='Image DPI (default: 300)', default=300)
    parser.add_argument('--annotate', help='Output annotated image path', default=None)
    parser.add_argument('--summary', action='store_true', help='Print summary to stdout')

    args = parser.parse_args()

    # Parse passes
    try:
        passes = [int(p.strip()) for p in args.passes.split(',')]
    except ValueError:
        logger.error("Invalid pass specification")
        sys.exit(1)

    # Run pipeline
    result = run_pipeline(args.input, dpi=args.dpi, passes=passes,
                         annotate_output=args.annotate)

    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2, default=str)
        logger.info(f"Results saved to {args.output}")
    else:
        # Output to stdout as JSON
        print(json.dumps(result, indent=2, default=str))

    # Print summary if requested
    if args.summary:
        print("\n=== Summary ===", file=sys.stderr)
        if 'error' in result:
            print(f"Error: {result['error']}", file=sys.stderr)
        else:
            for pass_num in passes:
                key = f'pass_{pass_num}'
                if key in result:
                    count_key = None
                    if pass_num == 2:
                        count_key = 'text_count'
                    elif pass_num == 3:
                        count_key = 'line_count'
                    elif pass_num == 4:
                        count_key = 'symbol_count'
                    elif pass_num == 5:
                        count_key = 'material_count'
                    elif pass_num == 6:
                        count_key = 'dimension_count'
                    elif pass_num == 7:
                        count_key = 'scale_count'

                    if count_key:
                        print(f"Pass {pass_num}: {result[key].get(count_key, 0)} items", file=sys.stderr)


if __name__ == '__main__':
    main()
