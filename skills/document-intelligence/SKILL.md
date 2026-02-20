---
name: document-intelligence
description: >
  Comprehensive construction document intelligence extraction system. Use when processing ANY construction documents (plans, specs, schedules, contracts, geotech, safety, SWPPP, sub lists, RFIs, submittals) to extract field-actionable data for daily reports, project management, quality control, and procurement. Also generates the Project Intelligence Dashboard and construction schedules (door, hardware, fixture, finish, plumbing, equipment, room) from extracted data. Triggers: "process documents", "extract from plans", "read the specs", "analyze schedule", "set up project", "add documents", "show project intelligence", "project intel", "what data do we have", "door schedule", "hardware schedule", "finish schedule", "generate schedules", "room schedule", "equipment schedule", any mention of construction document processing or project intelligence building. This skill should be used EVERY TIME construction documents need to be processed - it extracts deep, comprehensive data including specific values, schedules, specifications, and coordination information that goes far beyond basic document reading.
version: 1.0.0
---

# Construction Document Intelligence

A comprehensive extraction system for construction project documents that captures deep, field-actionable intelligence for daily reports, project management, quality control, and procurement tracking.

## Overview

This skill transforms raw construction documents into structured, actionable project intelligence by:

1. **Classifying documents** automatically (plans, specs, schedules, contracts, etc.)
2. **Extracting comprehensive data** with specific numerical values, not just descriptions
3. **Cross-referencing** information across multiple documents
4. **Tracking extraction quality** with confidence levels and coverage metrics
5. **Structuring output** for downstream consumption by project management systems

**Key difference from basic document reading**: This skill extracts SPECIFIC VALUES and COMPLETE SCHEDULES rather than just summaries. For example:
- Not just "concrete requirements" → "4,000 PSI concrete, w/c ratio 0.45 max, slump 4\"±1\", air content 5.5%±1.5%, cure 7 days wet"
- Not just "room list" → Complete room schedule with ALL 50+ rooms, numbers, names, areas, departments
- Not just "schedule milestones" → Full critical path with durations, float, predecessors, constraints

## When to Use This Skill

**ALWAYS use this skill when**:
- Setting up a new project (/set-project, /process-docs, project initialization)
- Processing construction drawings (plans, elevations, sections, details)
- Processing specification books or spec sections
- Processing CPM schedules (P6, MS Project, Asta)
- Processing geotech reports, safety plans, SWPPP documents
- Processing contracts, subcontractor lists, RFI logs, submittal logs
- Updating project intelligence with new document revisions
- Any task involving "extract", "process", "read", "analyze" + construction documents

**Triggers include**:
- "Process these plans and extract grid lines, rooms, and finishes"
- "Read the spec book and get concrete requirements"
- "Analyze this schedule for critical path and milestones"
- "Extract subcontractor information from these contracts"
- "Process the geotech report for bearing capacity and compaction requirements"
- "What are the weather thresholds in the specs?"
- "Set up project intelligence from these documents"
- "Show me the project intelligence" / "project intel dashboard" / "what data do we have"
- "Show me the door schedule" / "generate schedules" / "hardware schedule" / "finish schedule"
- "What schedules have been extracted?" / "room schedule" / "equipment schedule"

---

## Core Capabilities

### 1. Three-Pass Extraction System

#### Pass 1: Metadata Extraction (Automatic)
Before reading content, extract PDF metadata:
- Creator application (signals document type)
- Creation/modification dates
- Page count
- Title, author, subject

#### Pass 2: Structural Analysis (Quick Scan)
Scan for structural patterns:
- Sheet index (for drawings)
- Table of contents (for specs)
- Headers, footers, tables
- Content signals for classification

#### Pass 3: Deep Content Extraction (Targeted)
Based on document type, extract comprehensive intelligence following specialized references.

#### Pass 4: Visual Analysis (Plan Sheets)
For plan sheet PDFs, convert pages to 300 DPI PNG images and run `visual_plan_analyzer.py` for:
- OCR text extraction (room labels, dimensions, notes, title block data)
- Wall/line detection and classification (walls, grids, dimension lines)
- Construction symbol recognition (doors, outlets, fixtures, markers)
- Material zone detection (hatches → concrete, VCT, tile, insulation)
- Dimension extraction (pairing OCR text with dimension lines)
- Scale calibration (graphic scale bars and text-format scales)

Merge visual results with text-based extraction. Visual data fills gaps where PDF text extraction misses graphical content. See `references/visual-extraction-reference.md` for accuracy expectations and integration rules.

### 2. Modular Specialized References

This skill uses domain-specific extraction guides. **Read the appropriate reference(s) before extracting**:

| Reference | When to Use | Contains |
|-----------|-------------|----------|
| **[construction-document-conventions.md](references/construction-document-conventions.md)** | **Always read first** — before any extraction | How drawings are organized, sheet numbering navigation, cross-reference system, scale/measurement, quantity calculation formulas, contour/grading, line types, hatch patterns, abbreviations |
| **[extraction-rules.md](references/extraction-rules.md)** | Read second | Framework, classification, principles |
| **[plans-deep-extraction.md](references/plans-deep-extraction.md)** | Processing plans/drawings | Complete room/finish/door/window schedules, MEP equipment, structural specs |
| **[specifications-deep-extraction.md](references/specifications-deep-extraction.md)** | Processing specs | All CSI divisions with exact values, weather thresholds, testing frequencies |
| **[schedule-deep-extraction.md](references/schedule-deep-extraction.md)** | Processing CPM schedules | Activity details, sequencing logic, float, critical path, constraints |
| **[civil-deep-extraction.md](references/civil-deep-extraction.md)** | Processing civil/site drawings | Storm/sanitary/water systems with pipe sizes and elevations |
| **[compliance-deep-extraction.md](references/compliance-deep-extraction.md)** | Processing geotech, safety, SWPPP | Bearing capacity, compaction, BMPs, inspection requirements |
| **[project-docs-deep-extraction.md](references/project-docs-deep-extraction.md)** | Processing contracts, sub lists, RFIs, subcontracts, POs | Contract terms, sub contacts, RFI status, submittal tracking, SC scope/exclusions, PO line items |
| **[pemb-deep-extraction.md](references/pemb-deep-extraction.md)** | Processing PEMB manufacturer documents | Column reactions, anchor bolts, framing, erection sequence, panels, accessories |
| **[submittals-deep-extraction.md](references/submittals-deep-extraction.md)** | Processing submittal packages | Concrete mixes, door hardware, shop drawings, MEP equipment, finishes |
| **[dxf-extraction.md](references/dxf-extraction.md)** | Processing .dxf/.dwg CAD files | Layer mapping, block attributes, hatch areas, polyline geometry, dimensions, parse_dxf.py |
| **[visual-extraction-reference.md](references/visual-extraction-reference.md)** | Processing plan sheet images (PDF→PNG) | OCR text extraction, line/wall detection, symbol recognition, material zones, dimensions, scale calibration |
| **[masterformat-reference.md](references/masterformat-reference.md)** | Enriching reports, QA checks, morning briefs | CSI Div 01-33: sequencing, QC issues, hold points, testing, weather limits, PEMB + healthcare overlays |

---

## Workflow

### For Single Document

1. **Read base extraction rules**:
   ```
   Read references/extraction-rules.md
   ```

2. **Classify the document** (Pass 1 + 2):
   - Check PDF metadata (creator application)
   - Scan for structural patterns
   - Identify document type

3. **Read appropriate specialized reference(s)**:
   ```
   # If plans/drawings:
   Read references/plans-deep-extraction.md

   # If specifications:
   Read references/specifications-deep-extraction.md

   # If schedule:
   Read references/schedule-deep-extraction.md

   # etc.
   ```

4. **Extract comprehensively** following the reference guide

5. **Track extraction quality** and structure output

### For Multiple Documents

When processing a document set (e.g., during project setup):

1. **Read base rules**: `references/extraction-rules.md`

2. **Classify all documents** first (Pass 1 + 2 for each)

3. **Present classification** to user for confirmation

4. **Read relevant specialized references** based on document types found

5. **Process in priority order** (earlier provides context for later):
   - Plans/drawings FIRST (establishes spatial framework)
     - For plan sheet PDFs: also run visual analysis (Pass 4) to extract graphical data
     - Merge visual results (OCR text, symbols, material zones) with text-based extraction
     - Visual data fills gaps where PDF text extraction misses graphical content
   - DXF/DWG files FIRST-A (exact spatial data takes priority over PDF estimates)
   - Specifications SECOND (adds material/quality details)
   - Schedule THIRD (adds time dimension)
   - Contract FOURTH (adds constraints)
   - Sub list FIFTH (adds personnel)
   - Support docs LAST (RFIs, submittals, minutes)

6. **Cross-reference** data across documents

7. **Report comprehensive results** with metrics

---

## Extraction Depth Guidance

### Extract DEEP (100% completeness)

**Plans**:
- Grid lines (ALWAYS - critical for spatial reference)
- ALL room numbers and names
- ALL doors in door schedule
- ALL equipment in MEP schedules
- Structural general notes with EXACT VALUES (PSI, rebar sizes, embedments)

**Specifications**:
- Weather thresholds with NUMBERS (40°F, 90°F, 25 mph)
- Testing frequencies with NUMBERS ("1 set per 50 CY")
- Hold points vs. witness points (clearly distinguished)
- Tolerances with LIMITS (FF 35/FL 25, ±1/4")

**Schedule**:
- ALL milestones with dates
- Critical path activities (float = 0)
- Activity durations, dates, predecessors for critical/near-critical

### Extract BROAD (key items only)

- Meeting minutes (action items, decisions only)
- Correspondence (directives, not entire threads)
- Historical RFIs (closed items, not deep detail)

---

## Integration with Downstream Systems

### Daily Reports
- Auto-complete location references
- Spell subcontractor names correctly
- Track room-by-room progress
- Flag weather threshold conflicts

### Project Management
- Phase completion percentages
- Schedule health monitoring
- Procurement status tracking
- Resource loading analysis

### Quality Control
- Test result verification
- Tolerance acceptance
- Hold point tracking
- Inspection frequency compliance

### Procurement
- Equipment lead times
- Submittal approval status
- Long-lead item tracking
- Critical path dependencies

### Quantitative Intelligence
After extraction, the **quantitative-intelligence** skill uses extracted data + sheet cross-references to:
- Build assembly chains linking elements across multiple sheets
- Calculate derived quantities (concrete CY, flooring SF, fixture counts)
- Merge DXF, visual, takeoff, and text sources with priority rules
- Flag discrepancies when sources disagree by >10%
- Store quantities in `plans-spatial.json` and sheet references in the respective data files for use by reports, briefs, and dashboards

---

## Success Metrics

A successful extraction includes:
- **Completeness**: 100% of critical items extracted
- **Specificity**: Numerical values extracted, not just "per spec"
- **Structure**: JSON output ready for consumption
- **Quality tracking**: Coverage and confidence metrics
- **Cross-references**: Related data linked across documents
- **User validation**: Conflicts and low-confidence items flagged

---

## Project Intelligence Dashboard

When the user asks to see extracted project data ("show me the project intelligence", "project intel dashboard", "what data do we have"), generate a comprehensive Project Intelligence Dashboard:

1. Load the project data files from the user's working directory (`project-config.json`, `plans-spatial.json`, `specs-quality.json`, `schedule.json`, `directory.json`, and all log files)
2. If not found: "No project intelligence found. Run /set-project first to extract data from your construction documents."
3. Generate a single self-contained HTML file with:
   - **Sidebar navigation** with sections for: Overview, Documents Loaded, Grid Lines, Building Areas, Room Schedule (searchable), Site Layout, Spec Sections (searchable/filterable by CSI division), Key Materials, Weather Thresholds, Hold Points & Inspections, Construction Tolerances, Schedule, Contract Intelligence, Subcontractor Directory (searchable), Safety Intelligence, SWPPP & Erosion Control, Geotechnical Data, RFI Log, Submittal Log, Procurement & Materials, Vendor Database, Quantities (by CSI division, with source attribution), Sheet Cross-References (drawing index, detail callouts, assembly chains), Discrepancies (unresolved quantity variances)
   - **Data embedding**: Embed the entire config as a JavaScript object (fully self-contained)
   - **Color palette**: Navy #1B2A4A (headers), Blue #2E5EAA (accents), Light gray #F8F9FB (background), Light blue #EDF2F9 (sections), Amber #E8A838 (warnings), Green #2D8F4E (success), Red #C0392B (danger)
   - **Features**: Search and filter, status badges, sidebar count badges, coverage checklist, responsive layout
4. Save as `{PROJECT_CODE}_Project_Intelligence.html` in the user's output folder


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.
