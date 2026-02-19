---
name: document-annotation
description: >
  Construction document annotation and markup system for superintendents. Produce redline markups, revision clouds, text annotations, symbol placement, color-coded discipline markups, and layered annotation management on plans, specs, photos, and RFIs. Generate annotated PDFs using PyMuPDF/fitz and reportlab, annotated images for photo documentation, and HTML annotated views for dashboard integration. Integrates with document-intelligence, rfi-preparer, punch-list, daily-report-format, and drawing-control. Triggers: "annotate", "markup", "redline", "cloud", "mark up plans", "annotate drawing", "redline drawing", "photo markup", "punch list photo", "annotate spec", "spec markup", "RFI markup", "as-built markup", "callout", "dimension callout", "field note on drawing", "highlight on plan", "revision cloud", "annotation layer", "color-coded markup".
version: 1.0.0
---

# Document Annotation Skill

## Overview

The **document-annotation** skill provides programmatic construction document markup and annotation capabilities for superintendents and field managers. This skill does not replace Bluebeam Revu or PlanGrid for interactive markup sessions -- it provides **automated, data-driven annotation** that turns extracted project data into marked-up documents ready for field distribution, RFI submission, punch list documentation, and as-built recording.

Construction documents are only useful when the right information reaches the right trade at the right time. A 200-page spec book is useless to the plumber who needs three paragraphs about fixture rough-in requirements. A full set of architectural plans means nothing to the electrician who needs to know which rooms have dedicated circuits. This skill bridges that gap by producing annotated, trade-specific document extracts that put actionable information directly on the drawings, specs, and photos that field crews actually use.

**Core capabilities**:
- Redline and revision cloud markup on PDF plan sheets
- Text annotation with callouts, labels, leaders, and notes
- Symbol placement using standard construction markup conventions
- Color-coded markup by discipline following industry convention
- Layer-based annotation management for organizing markup by type
- Annotated document production for trade distribution
- Photo markup with deficiency callouts for punch list and QC
- RFI drawing markup with highlighted question areas
- As-built redline markup with field-verified dimensions and deviations
- Auto-generated annotations from document-intelligence extracted data
- Structured annotation records with full traceability

**Critical distinction**: This skill produces output documents. It takes source documents (plans, specs, photos) and produces annotated versions with markup applied. The annotations are data-driven -- they come from project data, field observations, RFI content, punch list items, and extracted document intelligence, not from freehand drawing.

### Why Programmatic Annotation Matters

**Traditional markup workflow**:
- Open drawing in Bluebeam or PlanGrid
- Manually draw clouds, add text, place symbols
- Save and distribute
- No structured data behind the markup -- it is a picture of annotations

**Data-driven annotation workflow**:
- Annotation records created from project data (RFIs, punch items, field notes, extracted specs)
- Markup generated programmatically with consistent formatting
- Every annotation linked to source data (RFI number, punch item ID, spec section)
- Annotations queryable, filterable, and trackable
- Bulk annotation production for trade-specific document packages

This skill enables the superintendent to produce professional, consistent, traceable document markup at scale -- not one drawing at a time, but entire packages of annotated documents for distribution.

---

## PDF Markup Capabilities

### Redline and Cloud Markup

Redline markup is the fundamental language of construction document revision. This skill supports programmatic generation of all standard redline markup types.

**Revision Clouds**
- Freeform cloud outlines drawn around areas of change or concern
- Cloud arc radius configurable (default: 0.15" arc segments for standard revision cloud appearance)
- Cloud line weight: heavy (2pt) for revision clouds, per AIA convention
- Cloud color follows discipline color coding (see Color Conventions below)
- Interior of cloud may be left clear or filled with semi-transparent wash (10-15% opacity)
- Revision clouds are the primary markup for identifying areas affected by a design change, ASI, or field deviation

**Redline Annotations**
- Strikethrough lines for deleted elements (single diagonal or X through deleted item)
- Addition lines for new elements (drawn in revision color with delta symbol)
- Dimension callouts showing field-verified measurements vs. design dimensions
- Leader lines connecting annotations to specific locations on the drawing
- Section cuts and detail references pointing to supplementary information

**Implementation**: PDF markup is generated using PyMuPDF (fitz) for reading and modifying existing PDFs, and reportlab for generating new annotation overlays. The workflow:
1. Open source PDF with PyMuPDF
2. Calculate page dimensions and coordinate system
3. Generate annotation shapes (clouds, lines, text, symbols) as PDF drawing operations
4. Apply annotations as overlay on the source page
5. Save annotated PDF with annotations on a separate layer when possible

### Text Annotations

Text annotations place readable information directly on drawings at specific locations. All text follows construction document conventions for readability at typical reproduction scales.

**Note Annotations**
- Freestanding text blocks placed at specified coordinates
- Font: sans-serif (Helvetica/Arial) for markup text, matching typical construction document conventions
- Size hierarchy: 12pt for primary notes, 10pt for secondary, 8pt for reference text
- Background: optional white or yellow rectangle behind text for readability over complex drawings
- Border: optional thin black border around text block

**Comment Annotations**
- Text with leader line pointing to a specific location on the drawing
- Leader line terminates with arrowhead at the target location
- Text block positioned to avoid overlapping existing drawing content
- Comment format: "[PREFIX] Comment text" where prefix is the annotation type (e.g., "RFI-042:", "PUNCH:", "NOTE:")

**Label Annotations**
- Short text labels placed directly at or adjacent to elements
- Used for room numbers, equipment tags, grid references, elevation callouts
- Typically 8-10pt bold text with optional circle, rectangle, or hexagon enclosure
- Label placement follows drafting convention: above and to the right of the labeled element when space permits

**Callout Annotations**
- Numbered or lettered callouts with corresponding legend
- Callout marker: circled number or letter placed on the drawing
- Legend block: numbered list of callout descriptions placed in margin or title block area
- Used for punch list items, inspection points, deficiency locations

### Symbol Placement

Standard construction markup symbols communicate specific meanings without text. This skill places symbols programmatically at specified coordinates.

| Symbol | Name | Meaning | Usage |
|---|---|---|---|
| Triangle (delta) | Revision triangle | Marks a revision or change | Placed next to revised elements with revision number inside |
| Cloud outline | Revision cloud | Encloses area of change | Drawn around the affected area on the drawing |
| Arrow (straight) | Direction arrow | Indicates direction of flow, access, or reference | Placed on plans for traffic flow, pipe flow, access routes |
| Arrow (curved) | Rotation arrow | Indicates rotation or turning direction | Equipment orientation, door swing direction |
| Circle with crosshairs | Control point | Survey or layout control point | Placed at survey control locations |
| Diamond | Hold point | Inspection or quality hold point | Placed at locations requiring inspection before proceeding |
| Flag | Flag/attention | Calls attention to a specific item | General attention marker for important notes |
| X (cross) | Deficiency | Marks a deficient condition | Placed on photos or plans at deficiency locations |
| Checkmark | Verified/approved | Marks verified or approved condition | Placed on items that pass inspection |
| Circle with number | Callout bubble | Numbered reference to legend | Sequential numbering for punch list, inspection items |
| Dashed rectangle | Zone boundary | Defines a work zone or area | Drawn around work areas, hold zones, safety zones |
| Hatched area | Restricted zone | Indicates restricted or no-access area | Drawn over areas with access restrictions |

### Color-Coded Markup by Discipline

Industry convention assigns specific colors to discipline-specific markup. Consistent color coding allows field crews to immediately identify which trade a markup applies to.

| Discipline | Primary Color | RGB Value | Hex Code | Usage |
|---|---|---|---|---|
| Architectural | Black | (0, 0, 0) | #000000 | Architectural markups, general notes, dimensions |
| Structural | Red | (255, 0, 0) | #FF0000 | Structural markups, beam/column modifications, load paths |
| Mechanical (HVAC) | Green | (0, 128, 0) | #008000 | Ductwork routing, equipment placement, diffuser locations |
| Electrical | Blue | (0, 0, 255) | #0000FF | Conduit routing, panel locations, device placement |
| Plumbing | Purple | (128, 0, 128) | #800080 | Pipe routing, fixture locations, drain lines |
| Fire Protection | Red-Dashed | (255, 0, 0) dashed | #FF0000 | Sprinkler routing, head locations, FDC, standpipes |
| Civil/Site | Brown | (139, 90, 43) | #8B5A2B | Grading, utilities, paving, site features |
| Safety | Orange | (255, 140, 0) | #FF8C00 | Safety zones, barricades, fall protection, exclusion areas |
| General/Multi-trade | Magenta | (255, 0, 255) | #FF00FF | Multi-discipline coordination, general field notes |
| Owner/Design team | Cyan | (0, 200, 200) | #00C8C8 | Owner comments, design team responses, ASI markups |

**Fire protection distinction**: Fire protection uses the same red as structural but with a dashed line pattern to differentiate. When both structural and fire protection markups appear on the same sheet, the dash pattern provides clear visual separation.

**Discipline color override**: Project-specific color conventions may differ. The annotation system allows color override per project through the project configuration.

### Layer Management

Annotations are organized into layers that can be toggled, filtered, and managed independently. Layer management enables multiple annotation types to coexist on a single document without visual clutter.

**Standard Annotation Layers**:

| Layer Name | Content | Default Visibility |
|---|---|---|
| `RFI_REFERENCES` | RFI markup -- highlighted question areas, RFI numbers, cross-references | Visible |
| `FIELD_NOTES` | Superintendent field notes, observations, measurements | Visible |
| `QC_MARKS` | Quality control inspection marks, verification stamps, deficiency flags | Visible |
| `SAFETY_ZONES` | Safety barricade lines, exclusion zones, fall protection boundaries | Visible |
| `WORK_AREAS` | Work zone boundaries, trade access routes, staging areas | Visible |
| `DIMENSIONS` | Field-verified dimensions, deviation callouts, measurement annotations | Visible |
| `REVISIONS` | Revision clouds, delta symbols, change descriptions | Visible |
| `PUNCH_ITEMS` | Punch list callouts, deficiency markers, numbered references | Visible |
| `AS_BUILT` | As-built redlines showing field deviations from design | Visible |
| `HOLD_POINTS` | Inspection hold points, QC stop points, witness test locations | Visible |
| `TRADE_SPECIFIC` | Trade-specific annotations filtered by discipline color | Visible |
| `REFERENCE` | Background reference annotations, spec section references, code citations | Hidden by default |

**Layer naming convention**: `[TYPE]_[SUBTYPE]` using uppercase with underscores. Custom layers follow the same pattern (e.g., `SAFETY_FALL_PROTECTION`, `QC_CONCRETE_PLACEMENT`).

**PDF layer implementation**: When the output PDF supports Optional Content Groups (OCG), annotations are placed on named layers that can be toggled in PDF viewers (Adobe Acrobat, Bluebeam Revu). When OCG is not supported, layers are flattened but visually distinguished by color and line style.

---

## Annotated Document Production

### Plan Markup for Trade Distribution

The most common annotation task is marking up a plan sheet with trade-specific information for field distribution. This produces a document that a foreman can hand to a crew with all relevant information visible on the drawing.

**Work Area Markup**
- Dashed rectangle or cloud outline defining the active work zone for the day/week
- Zone label with work description (e.g., "ZONE 3A -- MEP ROUGH-IN THIS WEEK")
- Color-coded by responsible trade
- Access route arrows showing crew entry/exit paths
- Material staging area marked with hatching

**Hold Zone Markup**
- Solid red boundary line around areas where work must stop
- "HOLD" label with reason (e.g., "HOLD -- PENDING RFI-042 RESPONSE")
- Diamond hold point symbols at specific hold locations
- Reference to the RFI, inspection, or coordination item causing the hold

**Sequence Markup**
- Numbered zones showing installation sequence (1, 2, 3...)
- Directional arrows showing work flow direction
- Phase boundaries with date labels
- Predecessor/successor notes between zones

**Trade-Specific Plan Package**
For each trade receiving a marked-up plan:
1. Start with the relevant discipline sheet (mechanical plan for HVAC, electrical plan for electrical, etc.)
2. Add work area boundaries for the current look-ahead period
3. Mark hold zones and restricted areas
4. Add field notes relevant to that trade
5. Highlight RFI areas affecting that trade's work
6. Add spec references for critical requirements
7. Include callouts for coordination points with other trades

### Spec Section Annotation

Specification books are dense legal documents. Field crews need the critical requirements extracted and highlighted, not the full 50-page section. This capability produces annotated spec extracts.

**Spec Highlighting**
- Key requirements highlighted with colored background (yellow for critical, green for informational)
- Margin annotations explaining requirements in plain language
- Cross-references to plan sheet locations where the requirement applies
- Submittal references linked to approved submittals for specified products

**Trade Field Spec Sheet**
A one-to-three page annotated extract from the full spec section containing:
- Section header with spec section number, title, and revision date
- Critical requirements extracted and highlighted (strengths, tolerances, materials, methods)
- Testing and inspection requirements with hold points marked
- Approved products/manufacturers from submittal log
- Weather restrictions and environmental requirements
- Quality control requirements and acceptance criteria
- Relevant code references (ACI, AISC, NEC, UPC, NFPA)
- Superintendent notes and project-specific clarifications

**Implementation**: The document-intelligence skill extracts spec data; this skill formats it into annotated field-ready documents. The extraction provides structured data; the annotation provides visual presentation.

### RFI Drawing Markup

When preparing an RFI, the referenced drawing must be marked up to clearly identify the question area and provide context to the reviewer.

**RFI Markup Elements**
1. **Question Area Cloud** -- Revision cloud around the area in question, colored magenta for RFI markup
2. **RFI Reference Label** -- "RFI-[NUMBER]" label placed adjacent to the cloud with leader line
3. **Dimension Callouts** -- Key dimensions relevant to the question, highlighted in red
4. **Section References** -- Arrows pointing to relevant detail/section views
5. **Conflict Indication** -- If the RFI is about a conflict, both conflicting elements highlighted with contrasting colors
6. **Spec Reference** -- Annotation noting the relevant spec section number
7. **Photo Reference** -- If field photos exist, annotation noting "SEE ATTACHED PHOTO [X]"
8. **Proposed Solution** -- If the superintendent has a proposed resolution, it is sketched/annotated in green with "PROPOSED" label

**RFI Markup Package**
The complete RFI markup package includes:
- Annotated plan sheet (primary affected sheet)
- Annotated detail/section views (if applicable)
- Annotated photos (if field conditions are relevant)
- Annotation legend explaining all markup symbols used

### Punch List Photo Markup

Photo documentation of deficiencies requires clear annotation to communicate exactly what the problem is and where it is located.

**Photo Annotation Elements**
- **Deficiency Callout**: Circled number at the deficiency location with leader line to description
- **Description Box**: Text box with deficiency description, responsible trade, and punch item ID
- **Directional Arrows**: Arrows pointing to the specific deficient element
- **Measurement Overlay**: Dimension lines showing measured values vs. required values
- **Reference Overlay**: Spec section or drawing reference for the applicable standard
- **Before/After Comparison**: Side-by-side layout with "BEFORE" and "AFTER" labels, deficiency marks on the "before" image, acceptance marks on the "after" image
- **Location Stamp**: Text overlay with location information (building, floor, room, grid)

**Photo Markup Standards**
- Callout numbers correspond to the punch list item numbering
- Arrow colors match the responsible discipline color
- Description text is minimum 14pt for readability on mobile devices
- Location stamp is placed in the lower-left corner of the photo
- Date/time stamp placed in the lower-right corner
- White semi-transparent background behind all text overlays (80% opacity)

### As-Built Drawing Markup

As-built markup records the actual field conditions that differ from the design documents. These markups become part of the permanent project record and are used for closeout documentation.

**As-Built Markup Elements**
- **Dimension Redlines**: Actual field-measured dimensions shown in red, replacing or supplementing design dimensions
- **Routing Changes**: Revised pipe, conduit, or duct routing shown with colored lines matching the discipline
- **Elevation Changes**: Actual elevations annotated at key points (invert elevations, top-of-steel, finish floor)
- **Location Shifts**: Arrows showing the direction and distance of element displacement from design location
- **Deletion Marks**: X through elements that were not installed or were removed
- **Addition Marks**: New elements drawn in red with delta symbol and "ADDED" label
- **Deviation Notes**: Text annotations explaining why the field condition differs from design
- **Verification Stamps**: Checkmark with date and initials at locations verified by field measurement

**As-Built Color Convention**
- Red: All as-built changes and deviations
- Green: Verified as-installed matching design (confirmation markup)
- Blue: Information annotations (notes, references, explanations)
- Original drawing content remains in its original color (typically black)

**As-Built Accuracy Requirements**
- Horizontal dimensions: verified to +/- 1/4" for MEP, +/- 1/2" for structural
- Vertical dimensions: verified to +/- 1/4" for all systems
- Routing changes: drawn to approximate scale showing general path, with key dimensions noted
- All as-built markups must include the date of field verification and the verifier's initials

---

## Integration with Document Intelligence

The document-annotation skill leverages data extracted by the document-intelligence skill to auto-generate annotations. This eliminates manual placement of common annotations and ensures consistency.

### Auto-Generated Annotations from Extracted Data

**Room Number Placement**
- Document-intelligence extracts room numbers, names, and approximate locations from floor plans
- Annotation skill places room number labels at extracted coordinates on plan sheets
- Labels formatted as circled or boxed room numbers with room name below
- Useful for producing marked-up plans for trades that reference room numbers (finishes, electrical, low-voltage)

**Hold Point Locations**
- Document-intelligence extracts inspection and hold point requirements from spec sections
- Annotation skill places diamond symbols at corresponding locations on plan sheets
- Each hold point labeled with the inspection type and spec reference
- Produces a "hold point plan" showing all required inspections spatially

**Equipment Tag Placement**
- Document-intelligence extracts equipment schedules with tag numbers and locations
- Annotation skill places equipment tags at plan locations
- Tags formatted as hexagonal or rectangular labels with equipment designation
- Cross-references to submittal log entries and O&M manual references

**Spec Requirement Overlays**
- Document-intelligence extracts key requirements per area (concrete strength by pour area, fire rating by zone, finish schedule by room)
- Annotation skill produces annotated plans with requirements shown at their applicable locations
- Example: Floor plan with concrete strength noted in each pour area ("4000 PSI", "5000 PSI HIGH-EARLY")

### Annotated Spec Summaries

Produce trade-specific "field spec sheets" by combining extracted spec data with annotation formatting:

1. **Extract** key requirements from full spec section using document-intelligence
2. **Filter** requirements by trade applicability
3. **Format** as annotated document with highlighted critical items, plain-language notes, and visual callouts
4. **Cross-reference** with plan sheet locations and approved submittals
5. **Output** as annotated PDF ready for field distribution

**Example output**: A two-page "Concrete Field Spec Sheet" containing:
- Mix design requirements (extracted from 03 30 00) with critical values highlighted in yellow
- Placement requirements (slump, temperature, vibration) with hold points marked
- Curing requirements with timeline graphic and weather restrictions flagged in orange
- Testing requirements (cylinders, slump tests) with frequency table
- Approved ready-mix suppliers from submittal log
- Reference to specific pour area on plan with callout to spec requirements

### Annotated Schedule Overlays

Generate annotated schedule views by combining schedule data with visual markup:

**Critical Path Highlighting**
- Critical path activities highlighted in red on the bar chart or network diagram
- Near-critical activities (< 5 days float) highlighted in orange
- Float values annotated on each activity bar
- Milestone diamonds enlarged and labeled with dates

**Weather-Sensitive Activity Flags**
- Activities sensitive to weather conditions flagged with weather symbol
- Temperature restrictions (concrete pours, coatings, roofing) noted with threshold values
- Rain-sensitive activities (earthwork, exterior finishes) noted with restriction description
- Seasonal considerations annotated on the timeline

**Upcoming Milestone Highlights**
- Activities due within the look-ahead period highlighted with colored border
- Predecessor completion status shown with green (complete) or red (incomplete) indicators
- Resource requirements annotated on upcoming activities
- Material delivery dates cross-referenced from procurement log

---

## Output Formats

### Annotated PDF (Primary Format)

The primary output format is annotated PDF, produced using Python PDF libraries for programmatic markup.

**Technology Stack**:
- **PyMuPDF (fitz)**: Primary library for reading source PDFs, extracting page geometry, and applying annotations. PyMuPDF provides direct access to PDF page content, coordinate transformation, and annotation insertion.
- **reportlab**: Secondary library for generating complex annotation overlays (tables, formatted text blocks, charts) as separate PDF pages that are merged with the source document.
- **Pillow (PIL)**: For image manipulation when annotating photos (resize, composite, draw operations).

**PDF Annotation Process**:
1. Open source PDF with `fitz.open()`
2. Get page dimensions and rotation: `page.rect`, `page.rotation`
3. Calculate annotation coordinates in PDF user space (origin at lower-left, 72 points per inch)
4. Create annotation shapes:
   - `page.draw_rect()` for rectangles, zones, text backgrounds
   - `page.draw_circle()` for callout bubbles, control points
   - `page.draw_line()` for leader lines, dimension lines, arrows
   - `page.draw_polyline()` for revision clouds (series of arcs)
   - `page.insert_text()` for text annotations
   - `page.insert_image()` for symbol placement from pre-rendered symbol library
5. Set annotation properties: color, line width, fill, opacity, layer (OCG)
6. Save with `doc.save()` preserving original content with annotations overlaid

**Coordinate System Handling**:
- Construction drawings are often at non-standard scales (1/4" = 1'-0", 1/8" = 1'-0", etc.)
- The annotation system works in PDF points (1 point = 1/72 inch) regardless of drawing scale
- Location references from annotation records are converted to PDF coordinates using the page's coordinate mapping
- Grid intersections, room centers, and element locations are mapped to PDF coordinates before annotation placement

### Annotated Images

Photo documentation annotations use image manipulation to produce marked-up photos.

**Image Annotation Process**:
1. Open source image with Pillow
2. Calculate overlay positions based on image dimensions
3. Draw annotation elements:
   - Circles, arrows, rectangles using `ImageDraw`
   - Text with background using `ImageDraw.text()` with measured text bounding box
   - Semi-transparent overlays using alpha compositing
4. Composite all annotation layers onto the source image
5. Save as PNG (lossless for quality) or JPEG (compressed for distribution)

**Image Output Specifications**:
- Resolution: maintain source resolution, minimum 150 DPI for print, 72 DPI for screen
- Format: PNG for markup with transparency, JPEG for distribution
- Maximum dimension: 4096px on longest side for distribution (larger for archival)
- Text rendering: anti-aliased, minimum 14pt equivalent at output resolution

### HTML Annotated Views

For dashboard integration and web-based viewing, annotations can be rendered as HTML/SVG overlays.

**HTML Annotation Output**:
- Source document rendered as background image (rasterized from PDF or original photo)
- Annotations rendered as SVG overlay elements positioned absolutely
- Interactive elements: hover tooltips showing annotation details, click to navigate to source data
- Responsive scaling: annotations maintain relative position as the view scales
- Layer toggles: checkbox controls to show/hide annotation layers
- Print-friendly: CSS print media query produces clean printable output

---

## Annotation Data Model

All annotations are tracked through a structured data model stored in `annotation-log.json`. Each annotation is a discrete record linked to its source document, location, and associated project data.

### Schema

```json
{
  "annotations": [
    {
      "annotation_id": "ANN-001",
      "document_ref": "A-101",
      "document_path": "plans/architectural/A-101_Floor_Plan_Level_1.pdf",
      "sheet_number": "A-101",
      "sheet_title": "First Floor Plan",
      "annotation_type": "revision_cloud",
      "location": {
        "page": 1,
        "x": 324.5,
        "y": 512.0,
        "width": 180.0,
        "height": 120.0,
        "grid_ref": "C-4",
        "level": "Level 1",
        "room": "Room 105",
        "description": "Corridor ceiling area between grids C-D and 3-4"
      },
      "content": {
        "text": "Duct routing revised per RFI-042 response. See ASI-007.",
        "symbols": ["revision_delta"],
        "revision_number": "R3",
        "markup_elements": [
          {
            "type": "cloud",
            "points": [[300, 490], [350, 480], [420, 490], [450, 520], [440, 580], [380, 600], [310, 590], [290, 540]],
            "arc_radius": 10
          },
          {
            "type": "text",
            "position": [460, 500],
            "value": "RFI-042: Duct rerouted above beam",
            "font_size": 10
          },
          {
            "type": "leader_line",
            "from": [456, 510],
            "to": [420, 530]
          }
        ]
      },
      "discipline": "mechanical",
      "color": "#008000",
      "line_weight": "heavy",
      "layer": "RFI_REFERENCES",
      "created_by": "John Smith, Superintendent",
      "created_date": "2024-11-15",
      "modified_date": "2024-11-15",
      "linked_items": {
        "rfi": "RFI-042",
        "asi": "ASI-007",
        "clash_id": "CLH-MEP-STR-0042",
        "punch_item": null,
        "daily_report": "DR-2024-11-15",
        "spec_section": "23 31 13"
      },
      "status": "active",
      "version_history": [
        {
          "version": 1,
          "date": "2024-11-15",
          "action": "created",
          "by": "John Smith",
          "notes": "Initial RFI markup for duct rerouting at C-4"
        }
      ]
    }
  ],
  "annotation_sets": [
    {
      "set_id": "ASET-001",
      "name": "Level 1 MEP Coordination Markup",
      "description": "Complete MEP coordination markup for Level 1 distribution to mechanical and electrical foremen",
      "created_date": "2024-11-15",
      "created_by": "John Smith, Superintendent",
      "source_documents": ["A-101", "M-101", "E-101"],
      "annotation_ids": ["ANN-001", "ANN-002", "ANN-003", "ANN-004"],
      "output_format": "annotated_pdf",
      "output_path": "markups/Level1_MEP_Coordination_2024-11-15.pdf",
      "distribution": ["Tom Brown (Mechanical Foreman)", "Sarah Davis (Electrical Foreman)"],
      "status": "distributed"
    }
  ],
  "symbol_library": {
    "revision_delta": {
      "type": "triangle",
      "size": 16,
      "fill": false,
      "label_position": "center"
    },
    "hold_point": {
      "type": "diamond",
      "size": 20,
      "fill": true,
      "fill_color": "#FF0000",
      "label_position": "right"
    },
    "deficiency": {
      "type": "cross",
      "size": 14,
      "color": "#FF0000",
      "line_weight": 2
    },
    "verified": {
      "type": "checkmark",
      "size": 14,
      "color": "#008000",
      "line_weight": 2
    },
    "callout_bubble": {
      "type": "circle",
      "size": 20,
      "fill": true,
      "fill_color": "#FFFFFF",
      "border_color": "#000000",
      "label_position": "center"
    },
    "direction_arrow": {
      "type": "arrow",
      "size": 24,
      "fill": true,
      "head_style": "closed"
    },
    "section_cut": {
      "type": "section_arrow",
      "size": 24,
      "fill": true,
      "label_position": "tail"
    },
    "match_line": {
      "type": "dashed_line",
      "dash_pattern": [10, 5],
      "line_weight": 1.5,
      "label_position": "center"
    },
    "detail_bubble": {
      "type": "circle_with_line",
      "size": 24,
      "fill": false,
      "label_position": "center",
      "reference_position": "bottom"
    }
  },
  "layer_definitions": [
    {
      "layer_name": "RFI_REFERENCES",
      "display_name": "RFI References",
      "default_color": "#FF00FF",
      "default_visibility": true,
      "description": "RFI markup including question area clouds, RFI numbers, and cross-references"
    },
    {
      "layer_name": "FIELD_NOTES",
      "display_name": "Field Notes",
      "default_color": "#0000FF",
      "default_visibility": true,
      "description": "Superintendent field notes, observations, and measurements"
    },
    {
      "layer_name": "QC_MARKS",
      "display_name": "Quality Control",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "Quality control inspection marks, verification stamps, deficiency flags"
    },
    {
      "layer_name": "SAFETY_ZONES",
      "display_name": "Safety Zones",
      "default_color": "#FF8C00",
      "default_visibility": true,
      "description": "Safety barricade lines, exclusion zones, fall protection boundaries"
    },
    {
      "layer_name": "WORK_AREAS",
      "display_name": "Work Areas",
      "default_color": "#008000",
      "default_visibility": true,
      "description": "Work zone boundaries, trade access routes, staging areas"
    },
    {
      "layer_name": "PUNCH_ITEMS",
      "display_name": "Punch List Items",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "Punch list callouts, deficiency markers, numbered references"
    },
    {
      "layer_name": "AS_BUILT",
      "display_name": "As-Built Redlines",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "As-built redlines showing field deviations from design"
    },
    {
      "layer_name": "DIMENSIONS",
      "display_name": "Field Dimensions",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "Field-verified dimensions, deviation callouts, measurement annotations"
    },
    {
      "layer_name": "REVISIONS",
      "display_name": "Revisions",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "Revision clouds, delta symbols, change descriptions"
    },
    {
      "layer_name": "HOLD_POINTS",
      "display_name": "Hold Points",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "Inspection hold points, QC stop points, witness test locations"
    }
  ],
  "project_color_overrides": {}
}
```

### Annotation Record Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `annotation_id` | string | Yes | Unique identifier (ANN-###) |
| `document_ref` | string | Yes | Sheet number or document identifier of the source document |
| `document_path` | string | Yes | File path to the source document |
| `sheet_number` | string | No | Drawing sheet number (e.g., A-101, M-201) |
| `sheet_title` | string | No | Drawing sheet title |
| `annotation_type` | enum | Yes | Type: revision_cloud, text_note, comment, label, callout, symbol, dimension, zone_boundary, photo_markup, redline |
| `location` | object | Yes | Position data: page, x, y, width, height, grid_ref, level, room, description |
| `content` | object | Yes | Annotation content: text, symbols, revision_number, markup_elements array |
| `discipline` | enum | Yes | Discipline: architectural, structural, mechanical, electrical, plumbing, fire_protection, civil, safety, general |
| `color` | string | Yes | Hex color code for the annotation |
| `line_weight` | enum | Yes | Line weight: heavy (2pt), medium (1pt), light (0.5pt) |
| `layer` | string | Yes | Annotation layer name |
| `created_by` | string | Yes | Name and role of the annotation creator |
| `created_date` | string | Yes | ISO date of creation |
| `modified_date` | string | No | ISO date of last modification |
| `linked_items` | object | No | Cross-references: rfi, asi, clash_id, punch_item, daily_report, spec_section |
| `status` | enum | Yes | Status: active, superseded, voided, archived |
| `version_history` | array | Yes | Array of version records tracking annotation changes |

### Annotation Set Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `set_id` | string | Yes | Unique identifier (ASET-###) |
| `name` | string | Yes | Descriptive name for the annotation set |
| `description` | string | No | Detailed description of the annotation set purpose |
| `created_date` | string | Yes | ISO date of creation |
| `created_by` | string | Yes | Name and role of the set creator |
| `source_documents` | array | Yes | List of source document references included in the set |
| `annotation_ids` | array | Yes | List of annotation IDs included in the set |
| `output_format` | enum | Yes | Output format: annotated_pdf, annotated_image, html_view |
| `output_path` | string | No | File path to the generated output |
| `distribution` | array | No | List of recipients for the annotated document |
| `status` | enum | Yes | Status: draft, generated, distributed, archived |

### Status Lifecycle

**Annotation Status**:

| Status | Definition |
|---|---|
| `active` | Current, valid annotation displayed on output documents |
| `superseded` | Replaced by a newer annotation (e.g., revised RFI response, updated punch item) |
| `voided` | Annotation was created in error or is no longer applicable |
| `archived` | Annotation is historical record, retained but no longer displayed by default |

**Annotation Set Status**:

| Status | Definition |
|---|---|
| `draft` | Set defined but output not yet generated |
| `generated` | Output document produced, not yet distributed |
| `distributed` | Output document distributed to recipients |
| `archived` | Set is historical record, output may be superseded |

---

## Annotation Workflow Patterns

### Pattern 1: Weekly Trade Distribution Package

**Frequency**: Weekly, aligned with look-ahead planning cycle

**Process**:
1. Pull current look-ahead activities by trade from schedule data
2. For each trade with active work in the coming week:
   a. Select the relevant plan sheets covering their work areas
   b. Generate work area boundary annotations (WORK_AREAS layer)
   c. Add hold zone annotations for pending RFIs, inspections (HOLD_POINTS layer)
   d. Add field notes relevant to the trade (FIELD_NOTES layer)
   e. Compile into an annotation set
   f. Generate annotated PDF output
   g. Distribute to trade foreman

### Pattern 2: RFI Submission Package

**Trigger**: RFI preparation (integrates with rfi-preparer skill)

**Process**:
1. Identify the drawing sheet(s) referenced by the RFI
2. Generate revision cloud around the question area (RFI_REFERENCES layer)
3. Add RFI number label with leader line
4. Add dimension callouts for relevant measurements
5. Add spec section reference annotation
6. If field photos exist, generate annotated photo with callouts
7. Compile into annotation set
8. Generate annotated PDF package for RFI attachment

### Pattern 3: Punch List Walkthrough Documentation

**Trigger**: Punch list walkthrough (integrates with punch-list skill)

**Process**:
1. For each punch list item captured during the walkthrough:
   a. Annotate the field photo with deficiency callout, description, and location stamp
   b. Place callout marker on the relevant plan sheet at the item location
   c. Number callouts sequentially matching the punch list numbering
2. Generate annotated plan sheet with all punch items shown spatially
3. Generate annotated photo package with all deficiency photos marked up
4. Compile into annotation set for distribution to responsible trades

### Pattern 4: As-Built Documentation

**Trigger**: Work completion verification, pre-cover inspection, closeout documentation

**Process**:
1. Collect field-verified dimensions and routing data
2. For each deviation from design:
   a. Place redline annotation showing actual condition
   b. Add dimension callout with actual vs. design values
   c. Add deviation note explaining the change
3. Place verification stamps at locations confirmed as matching design
4. Generate annotated as-built drawing for record
5. Log all deviations in the field verification tracking system

---

## Integration

The document-annotation skill connects with other ForemanOS skills to provide comprehensive document management:

### document-intelligence
- Receives extracted data (room numbers, equipment tags, spec requirements, hold points) for auto-generated annotations
- Consumes document classification and coordinate mapping for accurate annotation placement
- Uses extracted spec section data to produce annotated field spec sheets
- Leverages schedule data for annotated timeline views and milestone highlights

### rfi-preparer
- Produces annotated drawing markups for RFI submission packages
- Generates revision cloud and question area highlighting referenced by RFI content
- Creates annotated photo attachments for field condition documentation
- Maintains cross-reference between annotation records and RFI log entries

### punch-list
- Produces annotated photos with deficiency callouts, descriptions, and location stamps
- Generates annotated plan sheets showing punch item locations spatially
- Creates numbered callout overlays matching punch list item numbering
- Supports before/after photo comparison annotation for punch item resolution

### daily-report-format
- Provides annotated plan references for daily report work area documentation
- Generates annotated site photos for daily report photo logs
- Creates quick-markup plan sheets showing today's active work areas
- Supplies annotation records for daily report activity logging

### drawing-control
- Tracks revision markup on controlled drawings through annotation version history
- Maintains annotation layer state across drawing revisions (carry forward or archive)
- Links revision cloud annotations to drawing revision log entries
- Ensures as-built markup annotations are preserved through the revision process

### bim-coordination
- Consumes clash report data to auto-generate clash location markups on plan sheets
- Places deviation markers from model-to-field verification records
- Produces annotated plans showing scan results and out-of-tolerance conditions
- Generates coordination markup showing multi-discipline conflict areas
