# Visual Plan Analysis — Extraction Reference

Extract construction intelligence from plan sheet images using computer vision and OCR. This is the visual complement to text-based extraction (Phase 5) and DXF spatial extraction (Phase 6), capturing the 80% of plan data communicated through drawings rather than text.

---

## Pipeline Overview

The visual analysis pipeline (`visual_plan_analyzer.py`) runs 7 sequential passes on a plan sheet image (PNG, 300 DPI recommended):

| Pass | Name | Extracts | Feeds Into |
|------|------|----------|------------|
| 1 | Sheet Layout Detection | Zone map (title block, plan area, details, notes, schedules) | All subsequent passes (zone-aware) |
| 2 | Full OCR Extraction | All text with position, angle, type classification, zone | Pass 6 (dimension text), Pass 7 (scale text) |
| 3 | Line Detection & Classification | Walls, dimension lines, grid lines, leaders, section cuts | Pass 6 (dimension lines) |
| 4 | Symbol Detection | Doors, windows, electrical, plumbing, markers | Cross-ref with schedules |
| 5 | Material Zone Detection | Hatch patterns → material types with areas | Cross-ref with finish schedule |
| 6 | Dimension Extraction | Paired dimension values + line segments | Quantity intelligence |
| 7 | Scale Detection | Pixels-per-foot calibration per zone | Area calculations in Pass 5 |

### Processing Time (CPU, 300 DPI ~3000×4000px)

| Pass | Time | Notes |
|------|------|-------|
| 1 | 2-3 sec | OpenCV contours |
| 2 | 5-7 sec | PaddleOCR + CRAFT, CPU-bound |
| 3 | <1 sec | Hough transform |
| 4 | 3-5 sec | Template matching + filtering |
| 5 | 3-5 sec | Texture analysis |
| 6 | 1-2 sec | Post-processing of Pass 2+3 |
| 7 | 1-2 sec | Template match + OCR |
| **Total** | **~16-25 sec** | **Per sheet** |

A 50-sheet plan set processes in approximately 15-25 minutes.

---

## Running the Pipeline

```bash
# Full pipeline
python3 visual_plan_analyzer.py sheet.png --output result.json --dpi 300

# With annotated overlay image
python3 visual_plan_analyzer.py sheet.png --output result.json --annotate annotated.png

# Specific passes only
python3 visual_plan_analyzer.py sheet.png --passes 1,2,6,7

# Summary statistics
python3 visual_plan_analyzer.py sheet.png --summary
```

### Input Requirements

- **Format**: PNG (recommended), JPG, TIFF
- **Resolution**: 300 DPI recommended (200 DPI minimum, 600 DPI maximum for performance)
- **Source**: PDF plan sheets converted to PNG using `pdf_to_images.py` from the construction-takeoff skill
- **Color**: Color or grayscale — pipeline converts to grayscale internally for line/symbol detection

### Converting PDFs to Images

```bash
python3 /mnt/.skills/skills/construction-takeoff/pdf_to_images.py plans.pdf --dpi 300 --output-dir ./sheet_images/
```

---

## Text Type Classification (Pass 2)

After OCR extracts all text, each text element is classified by content pattern:

| Text Type | Pattern | Example | Use |
|-----------|---------|---------|-----|
| Room number | 3-4 digits, in plan area | "101", "201A" | Room schedule cross-ref |
| Dimension | X'-Y" format | "25'-0\"", "12'-6\"" | Measurement data |
| Elevation | EL. or +/- prefix | "EL. 100'-0\"", "+4'-0\"" | Vertical positioning |
| Spec reference | XX XX XX format | "09 65 00", "03 30 00" | Spec cross-ref |
| Scale notation | Fraction = feet | "1/4\" = 1'-0\"" | Calibration |
| Grid label | Single letter or number at plan edge | "A", "1", "C.5" | Grid system |
| Sheet number | X-NNN format | "A-101", "S-201" | Sheet identification |
| Door/window mark | Letter + number | "D101", "W-3" | Schedule cross-ref |

---

## Line Type Classification (Pass 3)

Lines are classified by visual characteristics:

| Type | Thickness | Length | Pattern | Association |
|------|-----------|--------|---------|-------------|
| Wall | >2px at 300 DPI | Moderate | Solid | Form closed/near-closed rectangles |
| Dimension line | 1px thin | Moderate | Solid | Text nearby (dimension value), witness lines at ends |
| Grid line | 1px thin | Long (>50% sheet) | Dash-dot or solid | Grid labels at endpoints |
| Leader line | 1px thin | Short | Solid | 45°-60° angle, connects text to element |
| Section cut | >2px thick | Long | Heavy dashed | Section markers at endpoints |
| Hidden line | 1px thin | Variable | Short dashes | Below-slab elements, future work |

---

## Symbol Reference Library (Pass 4)

### Architectural Symbols

| Symbol | Visual | Description |
|--------|--------|-------------|
| Door swing | Arc + line at wall opening | Single, double, pocket, sliding |
| Window | Parallel lines with breaks in wall | Casement, sliding, fixed, awning |
| Stair arrow | Arrow with "UP" or "DN" text | Direction of travel |
| North arrow | Decorated arrow, usually circled | Plan orientation |
| Room tag | Circle or rectangle with number | Room identification |

### Section and Detail Markers

| Symbol | Visual | Description |
|--------|--------|-------------|
| Section cut | Circle with number/letter, arrow pointing | References section view on another sheet |
| Elevation marker | Circle with number/letter, no arrow | References elevation view |
| Detail callout | Circle or diamond with number/sheet | References enlarged detail |
| Revision cloud | Irregular wavy closed curve | Marks revised areas |
| Grid bubble | Circle at end of grid line | Grid identification |

### Electrical Symbols

| Symbol | Visual | Description |
|--------|--------|-------------|
| Duplex outlet | Circle with 2 lines | Standard receptacle |
| GFCI outlet | Circle with "GFI" text | Ground-fault outlet |
| 220V outlet | Circle with "220" or specific mark | High-voltage outlet |
| Single-pole switch | "S" in circle or at wall | Light switch |
| 3-way switch | "S3" mark | Multi-location switch |
| Junction box | Square or octagon | Electrical junction |
| Light fixture | Various shapes (circle, rectangle, line) | Ceiling or wall-mounted |

### Plumbing Symbols

| Symbol | Visual | Description |
|--------|--------|-------------|
| Water closet | Elongated oval/rectangle at wall | Toilet |
| Lavatory | Small oval/rectangle at wall | Sink |
| Floor drain | Circle with cross | Floor drain |
| Cleanout | Circle with "CO" | Access cleanout |
| Hose bib | Triangle at wall | Outdoor faucet |

### Fire Protection Symbols

| Symbol | Visual | Description |
|--------|--------|-------------|
| Sprinkler head | Circle with cross or dot | Pendent, upright, or sidewall |
| Pull station | Square with "PS" | Manual fire alarm pull |
| Horn/strobe | "HS" or bell symbol | Notification appliance |
| Fire extinguisher | "FE" or cabinet symbol | Extinguisher location |
| FDC | Double connection symbol | Fire department connection |

---

## Hatch Pattern Reference (Pass 5)

### Standard Construction Hatching Conventions

| Visual Pattern | Material | Standard | Use On |
|---------------|----------|----------|--------|
| Diagonal lines (45°, single direction) | Steel (section cut) | ANSI31 | Structural sections |
| Diagonal crosshatch (two directions, 45°/135°) | Concrete | AR-CONC | Foundation/slab sections |
| Random dots/stipple | Earth fill | EARTH | Embankments, backfill |
| Zigzag/wavy parallel lines | Insulation | INSUL | Wall/roof insulation |
| Offset rectangles (brick pattern) | Masonry | BRICK | Brick/CMU walls |
| Small dots in grid | Sand/gravel | AR-SAND | Base course, drainage |
| Solid light gray fill | VCT or generic flooring | DOTS | Floor plans |
| X-pattern grid | Ceramic tile | CROSS | Bathrooms, kitchens |
| No fill (white) | May be carpet or unfinished | — | Floor plans |

### Texture Analysis Method

The pipeline uses two complementary texture analysis techniques:

1. **Gabor Filters**: Detect repeating directional patterns at multiple frequencies (0.05, 0.1, 0.15) and orientations (0°, 45°, 90°, 135°). Strong response indicates hatching with known direction.

2. **Local Binary Patterns (LBP)**: Classify texture type based on local pixel neighborhoods. Different materials produce distinct LBP histograms.

### Material Zone Confidence

| Confidence | Criteria |
|-----------|----------|
| HIGH (>0.8) | Pattern matches finish schedule legend on the sheet |
| MEDIUM (0.5-0.8) | Standard hatching convention match |
| LOW (<0.5) | Ambiguous pattern, multiple possible materials |

---

## Accuracy Expectations

| Extraction Type | Visual Accuracy | DXF Accuracy | Notes |
|----------------|----------------|--------------|-------|
| Room areas | ±5-10% | Exact | Visual from pixel counting at calibrated scale |
| Material areas | ±5-10% | Exact | Visual from hatch zone boundaries |
| Door/window counts | 90-95% | 100% | May miss doors at unusual angles |
| Electrical fixture counts | 80-90% | 100% | Small symbols harder to detect |
| Plumbing fixture counts | 85-95% | 100% | Distinctive shapes help detection |
| Grid line spacing | ±1-2% | Exact | From OCR'd dimension values |
| Dimension values | 95-99% (OCR) | Exact | OCR accuracy depends on print quality |
| Scale detection | 95%+ | N/A | From text parsing, very reliable |
| Title block text | 98%+ | N/A | Large, clean text — high OCR confidence |

**When DXF data is available (Phase 6), it always takes priority over visual analysis for spatial data.** Visual analysis provides fallback when DXF is unavailable and supplements DXF with information DXF doesn't carry (symbol identification, material zone classification from hatching).

---

## Integration with Text-Based Extraction

Visual analysis supplements existing text-based extraction:

| Data | Text Extraction | Visual Adds |
|------|----------------|-------------|
| Room schedule | Table from plan notes | Room locations on floor plan, measured areas |
| Door schedule | Table from plan notes | Door locations, swing directions, count verification |
| Finish schedule | Table from plan notes | Actual material zone boundaries, area calculation |
| Equipment schedule | Table from plan notes | Equipment locations on plan, symbol verification |
| Grid system | Grid labels from notes | Grid line positions, spacing measurement |
| Dimensions | Limited from notes | All dimensioned measurements on drawings |
| General notes | Direct text extraction | Callout locations linked to plan elements |

### Cross-Reference Checks

After visual extraction, compare against text-based data:

1. **Door count**: Visual door swings vs. door schedule count → flag if different
2. **Room count**: Visual room tags vs. room schedule count → flag missing rooms
3. **Equipment count**: Visual equipment symbols vs. equipment schedule → flag discrepancies
4. **Material areas**: Visual hatch zones vs. finish schedule room assignments → verify coverage

---

## Claude Vision Validation (Post-Pipeline)

After the automated pipeline runs, Claude reviews the annotated images within the Cowork session using native multimodal capability. This is the **primary validation method** and runs automatically whenever plan sheets are processed through `/process-docs` or `/set-project`.

### How It Works

1. **Pipeline runs** → produces structured JSON + annotated plan image with colored overlays
2. **Claude reads JSON** results and **views annotated images** (native Cowork vision — no external API needed)
3. **Claude validates** extraction quality:
   - Room identification: correct numbers, complete count, locations match plan
   - Door/window counts: visual door swings match detected count, no missed openings
   - Symbol accuracy: electrical outlets vs. data ports, plumbing fixture types
   - Material zones: hatch patterns correctly classified (concrete vs. VCT vs. tile)
   - Line classification: walls vs. grid lines vs. dimension lines
   - Title block data: project name, sheet number, date, revision
4. **Claude corrects** the extraction JSON in-place for any misidentifications
5. **Low-confidence items** get special attention — Claude crops and zooms sub-images for closer inspection

### Validation Priority Order

Focus validation effort where errors have the most impact:

| Priority | Check | Why |
|----------|-------|-----|
| 1 | Room count matches schedule | Missing rooms = missed progress tracking |
| 2 | Door count matches schedule | Procurement and hardware coordination |
| 3 | Equipment symbols correctly identified | Wrong equipment type = wrong spec section |
| 4 | Grid lines and labels | Spatial reference for all field reporting |
| 5 | Dimension values | Quantity verification, material ordering |
| 6 | Material zone classification | Finish schedule validation |
| 7 | Electrical/plumbing fixture counts | Trade coordination, circuit loading |

### Superintendent Participation

The superintendent can participate in validation during Cowork sessions:

- **Correct misidentifications**: "That's not an outlet, that's a data port" → Claude updates extraction JSON
- **Add project-specific context**: "The hatching in those rooms is polished concrete, not VCT" → Claude reclassifies
- **Confirm ambiguous symbols**: "Those circles in the corridor are smoke detectors" → Claude adds to symbol map
- **Flag missing items**: "There should be 6 RTUs on the roof plan" → Claude re-examines

All superintendent corrections are logged and applied to improve future extractions on the same project.

### When to Use Claude Vision Validation

- **Always**: During `/set-project` and `/process-docs` for plan sheet PDFs
- **Per-sheet**: Claude validates each sheet after pipeline processing (automatic)
- **On-demand**: User asks "verify the floor plan extraction" → Claude re-examines
- **After corrections**: Re-validate after superintendent provides corrections

### Annotated Image Overlay Colors

The pipeline generates annotated images with these overlay colors for Claude to review:

| Color | Meaning |
|-------|---------|
| Green | Walls (thick lines) |
| Blue | Grid lines |
| Red | Dimension lines |
| Yellow text boxes | OCR-detected text with classification |
| Orange circles | Detected symbols |
| Semi-transparent fills | Material zones by type |

---

## Optional: Gemini 2.5 Pro Batch Validation

For bulk processing of large plan sets (100+ sheets) where interactive Cowork review is impractical, the pipeline supports automated validation using Google's Gemini 2.5 Pro vision model. This is **optional** — Claude Vision validation (above) is the default and preferred method.

### When to Use Gemini Batch Validation

- Initial project setup with 100+ plan sheets
- Overnight processing of full plan sets
- Bulk re-extraction after pipeline improvements
- Projects where superintendent isn't available for interactive review

### Setup

1. **Install**: `pip install google-genai --break-system-packages`
2. **Get API key**: From [Google AI Studio](https://aistudio.google.com/) (included with Gemini Pro subscription)
3. **Store key** in `AI - Project Brain/gemini-config.json`:
   ```json
   {
     "api_key": "YOUR_GEMINI_API_KEY",
     "model": "gemini-2.5-pro",
     "batch_size": 5,
     "max_retries": 3
   }
   ```

### Batch Validation Workflow

1. **Run automated pipeline** on all sheets → produces JSON + annotated PNGs
2. **Group sheets by discipline** (A-sheets together, S-sheets together, etc.)
3. **Send annotated images to Gemini** in batches of 5-10 sheets per API call
4. **Prompt Gemini** with extraction JSON + annotated image:
   - "Review this floor plan extraction. Verify room count, door count, and equipment identification."
   - "Check these dimension values against what you see on the plan."
   - "Confirm material zone classifications match the hatching patterns."
5. **Gemini returns corrections** as structured JSON (same schema as pipeline output)
6. **Apply corrections** to extraction results
7. **Generate validation summary** with correction counts by type

### Cost Estimate

- Gemini 2.5 Pro: ~$0.002-0.005 per plan sheet (image + text input/output)
- 50-sheet plan set: ~$0.10-0.25 total
- 200-sheet plan set: ~$0.40-1.00 total

### Limitations

- Requires internet access and valid API key
- API rate limits may slow processing of very large sets
- Gemini may not catch project-specific symbol conventions
- Claude Vision + superintendent review catches more nuanced errors
- Not suitable for confidential/classified projects (data leaves local machine)

---

## Fallback Strategy

When visual analysis components fail:

| Component | Fallback | Impact |
|-----------|----------|--------|
| PaddleOCR unavailable | CRAFT text detection + basic OCR | Reduced text recognition accuracy |
| CRAFT unavailable | PaddleOCR only | May miss angled text |
| Both OCR unavailable | OpenCV text detection (limited) | Significantly reduced text extraction |
| scikit-image unavailable | Skip Pass 5 (material zones) | No hatch pattern detection |
| Low-resolution image (<200 DPI) | Upscale with interpolation | Reduced accuracy across all passes |
| Complex/busy sheet | Claude Vision validation catches misses | Human-in-the-loop correction |

The pipeline is designed to degrade gracefully — each pass runs independently and handles missing upstream data.
