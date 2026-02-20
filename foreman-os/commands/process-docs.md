---
description: Process project documents to extract intelligence for daily reports
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [document type, filename, or "scan"]
---

Process new or updated project documents. Extracts intelligence and merges it into the existing project data without overwriting what's already there. Designed for both initial bulk processing (after `/set-project`) and incremental updates (single new document added to a folder).

Read the document-intelligence skill at `${CLAUDE_PLUGIN_ROOT}/skills/document-intelligence/SKILL.md` and the project-data skill at `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` before proceeding. Also read `${CLAUDE_PLUGIN_ROOT}/skills/document-intelligence/references/extraction-rules.md` for type-specific extraction rules. If available, also read the `construction-takeoff` Cowork skill for extracting material quantities from plan sheets during document processing.

## Step 1: Load Existing Project Data

Search for `project-config.json` in the user's working directory. Check these locations in order:
1. `AI - Project Brain/project-config.json`
2. `project-config.json` in the working directory root

If not found, tell the user: "No project is set up yet. Run `/set-project` first to create your project, then come back to process documents."

If found, load it and check the `documents_loaded` array to see what's already been processed.

## Step 2: Identify What to Process

### Mode A: Specific file or type (`/process-docs ASI-003.pdf` or `/process-docs schedule`)

If `$ARGUMENTS` contains a filename:
- Locate that file in the mapped folders (using `folder_mapping` from config) and process it.
- If the file isn't found, tell the user: "I couldn't find [filename] in your project folders. Check the path or drag the file into this chat."

If `$ARGUMENTS` contains a document type (e.g., "schedule", "specs", "plans", "safety"):
- Look in the relevant mapped folder for that type
- If multiple files of that type exist, list them and ask the user which one(s) to process

### Mode B: User uploads a file directly

If the user drags/drops or uploads a file into the chat:
- Process the uploaded file directly. No folder lookup needed.

### Mode C: No arguments (`/process-docs`)

If no arguments and no uploaded file:
- Tell the user: "What would you like me to process? You can:"
  - "Drag a file into this chat"
  - "Tell me a filename: `/process-docs ASI-003.pdf`"
  - "Tell me a document type: `/process-docs schedule`"
  - "Run `/process-docs scan` to see what's new in your folders"

### Mode D: Scan (`/process-docs scan`)

Lightweight folder scan. Compares what's in the project folders against what's already been processed. Reports what's new, what's changed, and what's ready to process. Does NOT extract or process any documents — just looks and reports.

1. **Load folder_mapping and documents_loaded** from `project-config.json`
2. **Walk every mapped folder** — list all supported file types (`.pdf`, `.xlsx`, `.xls`, `.csv`, `.docx`, `.doc`). Record filename, full path, file size, and parent folder.
3. **Compare against documents_loaded**:
   - Not in documents_loaded → **NEW**
   - Same filename and file size → **UNCHANGED**
   - Same filename, different file size → **UPDATED**
4. **Present scan report** grouped by status:

   > **Project Update Scan — [Project Name]**
   > *Last full scan: [date] · [X] documents on file*
   >
   > **New Files (3):**
   > 1. `ASI-003_Window_Revision.pdf` (480 KB) — in `08 - Change Orders/` — Likely: ASI
   > 2. `Submittal_08-1000_Doors.pdf` (2.1 MB) — in `06 - Submittals/` — Likely: submittal package
   >
   > **Updated Files (1):**
   > 3. `CPM_Schedule.pdf` — in `09 - Schedule/` — was 2.3 MB, now 2.8 MB
   >
   > **Unchanged: [X] files** — already processed, no changes detected.
   >
   > Tell me which files to process, or say "all new" to process everything that's new.

   If nothing's new: "All [X] documents are up to date. Your project intelligence is current."

   If no documents have been processed yet: list all files grouped by folder and recommend starting with specs and schedule.

This scan is read-only — safe to run as often as needed.

### Duplicate Check

Before processing, check if the file is already in `documents_loaded`:
- If the same filename with the same file size exists: "I already processed [filename] on [date]. Want me to re-extract it? This will update any fields that changed while keeping everything else intact."
- If the same filename with a different file size exists: "I processed an earlier version of [filename] on [date]. This looks like an updated version — I'll extract the changes."

## Step 3: Classify and Extract

For each document, run the **document-intelligence** skill's three-pass pipeline:

### Pass 1: Metadata Extraction
Extract PDF metadata (creator application, title, dates, page count). Auto-classify the document type.

### Pass 2: Structural Text Analysis
Scan for structural patterns (sheet index, TOC, tables, headers) to confirm type and guide extraction.

### Pass 3: Targeted Content Extraction
Extract intelligence following the extraction rules for the identified document type.

### Multi-Document Handling
If multiple documents are provided:
1. Classify all documents first
2. Present classification to user for confirmation
3. Process in priority order: plans → specs → schedule → contract → subs → everything else

## Step 4: Merge Intelligence

Use the project-data skill's merge rules when integrating new intelligence into existing config:

| Data Type | Merge Strategy |
|---|---|
| Subcontractors | Add new, update existing (match on name), never delete |
| Milestones | Update dates, add new milestones, never delete |
| Spec sections | Add new sections, update requirements, never delete |
| Grid lines | Merge (add new grids), never replace |
| Schedule (full update) | Replace current dates/critical path, keep history |
| Contract dates | Replace with newer, log change in version history |
| Weather thresholds | Update per spec section, log changes |
| Testing requirements | Add new, update frequency/agency, never delete |
| Hold points | Add new, update existing (match on work type + spec section), never delete |
| Tolerances | Update per material/system |
| Safety zones | Add new, update existing |
| Geotechnical | Replace with newer data (assumes newer report) |
| SWPPP BMPs | Add new, update existing locations |
| RFIs | Add new RFIs, update status for existing |
| Submittals | Add new submittals, update status, attach product specs |
| Vendors | Add new vendors, update contact/pricing info |
| Concrete mix designs | Add new mixes (match on mix_id), update existing, never delete |
| PEMB data (reactions, panels, accessories) | Replace with newer manufacturer data, keep version history |
| Electrical equipment (panels, schedules) | Add new, update existing by panel/circuit, never delete |
| Permits | Add new, update expiration dates, never delete |
| Civil/utility systems | Add new runs, update inverts/sizes, never delete |

### Version History
Log all changes to key data points in the `version_history` array:
```json
{
  "date": "2026-02-12",
  "source": "revised_schedule_020126.pdf",
  "changes": [
    {
      "field": "schedule.milestones.substantial_completion",
      "old_value": "2026-06-15",
      "new_value": "2026-07-01",
      "reason": "Schedule update from P6 revision 3"
    }
  ]
}
```

### Conflict Resolution

When NEW document data conflicts with EXISTING data:
- Compare the `date_loaded` of the new document against the `date_loaded` of the document that originally provided the existing value
- If the new document is newer: replace and log the change in version_history
- If the new document is older than what's already there: ask the user: "This [document type] is dated [date], but I already have newer data from [source] dated [date]. Use the older data anyway?"
- If dates can't be determined: present both values and ask the user to choose

### Document-Specific Merge Notes

**RFI logs or RFI correspondence:**
- Extract all open RFIs with status and description
- Link to relevant spec sections or design issues
- Note submitter, date submitted, and owner response status
- Flag any RFIs blocking work progress

**Submittal logs or tracking spreadsheets:**
- Extract submittal status for each item (pending, under review, approved, rejected, resubmitted)
- Extract submittal date, resubmit date, and due date
- Flag submittals under review for more than 10 business days
- Extract product specifications into submittal_log

**Vendor quotes or product catalogs:**
- Extract vendor contact info and product details
- Update vendor_database with new vendors and pricing
- Cross-reference with procurement_log for matching materials

**Submittal packages / product data sheets:**
- Extract product specifications and compliance info
- Attach to corresponding submittal_log entry
- Extract certifications and test reports
- Note warranty information

**Revised schedule upload:**
- Update all milestone dates
- Update current phase
- Recalculate critical path items
- Note any schedule changes vs. previous: "Substantial completion moved from [old] to [new]"

**ASI (Architect's Supplemental Instruction):**
- Extract what changed in the design
- Update affected spec sections
- Note any scope changes that impact subs

**Change order:**
- Document scope change
- Note cost impact if visible
- Flag any schedule impact
- Update affected sub scopes if applicable

**Updated sub list / new sub award:**
- Add new subcontractors to the directory
- Update contact info for existing subs
- Update scope assignments

**Meeting minutes:**
- Extract action items relevant to field operations
- Note any owner directives or design decisions
- Update schedule impacts discussed

**Geotechnical report:**
- Extract bearing capacity, soil conditions, compaction requirements
- Update dewatering requirements
- Note any changes from previous geo data

**Safety plan:**
- Extract fall protection zones, confined spaces, hot work areas
- Update competent person assignments
- Note any new safety requirements

**SWPPP:**
- Extract BMP locations and types
- Set inspection triggers (rainfall threshold)
- Note documentation requirements

### Cross-Referencing After Merge

After merging new data, run these cross-checks to catch downstream impacts:

**When processing ASIs or design changes:**
- Check `procurement-log.json` for items matching the changed spec section
- If materials are already ordered or delivered that no longer meet the updated spec, flag: "ASI-001 changed [spec]. Material PROC-XXX was ordered per old spec — verify with supplier."
- Check `submittal-log.json` for approved submittals that reference the changed section — flag for re-review

**When processing RFI responses/resolutions:**
- Check `submittal-log.json` for submittals with `related_rfis` containing this RFI
- If found with status "under_review" or "revise_and_resubmit", flag: "RFI-XXX resolved — related submittal SUB-XXX may now be approvable."
- Check `plans-spatial.json` quantities if the RFI clarifies a dimension or material — update the affected assembly chain

**When processing schedule updates:**
- Check `procurement-log.json` for delivery dates vs. updated activity dates
- Recalculate days-until-needed for each procurement item
- Flag items where the delivery-to-installation window changed significantly (>7 days shift)
- Check `inspection-log.json` for inspections tied to activities that moved

**When processing updated sub lists:**
- Cross-check against `schedule.json` for activity assignments
- Flag scope conflicts: sub listed as "Excavation" but scheduled for "Concrete"
- Update `directory.json` with new contact info

**When processing meeting minutes:**
- Scan action items for RFI references (pattern: "RFI-###") — link to `rfi-log.json`
- Scan for submittal references (pattern: "SUB-###" or "Submittal ###") — link to `submittal-log.json`
- Scan for change order references (pattern: "CO-###" or "PCO-###") — link to `change-order-log.json`

**When processing any spec update:**
- Extract ALL weather thresholds (not just "active" sections) — store inactive ones with a flag
- Extract hold points and testing frequencies with actual numbers
- Cross-check spec values against already-extracted plan values — flag conflicts >10%
- Check for new hold points that should be added to `specs-quality.json`

## Step 5: Build Cross-References and Quantities (Incremental)

After extraction, run the **quantitative-intelligence** skill workflow — but only for data affected by the newly processed documents.

### When processing plan sheets, structural drawings, or DXF files:

1. **Update the sheet cross-reference index** — parse extracted text from the NEW sheets for detail callouts (3/A5.2), section cuts, schedule references, spec callouts, and general note references. Merge into the existing index; do not rebuild from scratch.
2. **Rebuild assembly chains that touch the new sheets** — if a new structural detail was added, rebuild assembly chains that reference it. Don't rebuild chains for unrelated sheets.
3. **Recalculate affected quantities** — only recalculate quantities that depend on data from the newly processed sheets. If a new mechanical plan was added, recalculate MEP quantities but don't redo concrete quantities.
4. **Run cross-verification** — check any values from the new sheets against existing data from other sheets. Flag discrepancies >10%.
5. **Run spatial clash detection** — if the new sheets introduce elevation data for a discipline, compare against existing disciplines for conflicts.
6. **Store results** in `plans-spatial.json` (quantities and cross-references sections)

### When processing specs:
- Update `specs-quality.json` with new spec sections
- Cross-check any spec values (e.g., concrete strength) against values already extracted from plans. Flag conflicts.

### When processing schedules:
- Update `schedule.json`
- Cross-check milestone dates against any dates referenced in other documents

### Partial cross-reference updates for non-graphical documents:
For documents that don't involve spatial/quantitative data (contracts, sub lists, meeting minutes, RFI logs, submittal logs, vendor quotes):
- Still update the sheet cross-reference index if the document references specific plan sheets (e.g., an RFI referencing sheet S2.1)
- If an RFI or submittal clarifies a quantity or dimension, mark the affected assembly chain as "needs recalculation" for the next plan processing run
- Do NOT rebuild full quantities or spatial clash detection for these document types

## Step 6: Save Updated Data Files


Write changes to ONLY the data files affected by this processing run. Use the multi-file data store in `folder_mapping.ai_output`:

| Document Type Processed | Files Updated |
|---|---|
| Plans/drawings | `plans-spatial.json` |
| Specifications | `specs-quality.json` |
| Schedule | `schedule.json` |
| Subcontractor list | `directory.json` |
| Vendor quotes/catalogs | `directory.json` |
| RFI log/correspondence | `rfi-log.json` |
| Submittal log/packages | `submittal-log.json` |
| Geotechnical report | `specs-quality.json` |
| Safety plan | `specs-quality.json` |
| SWPPP | `specs-quality.json` |
| Contract/scope | `project-config.json` |
| Change order | `change-order-log.json` |
| Meeting minutes | `meeting-log.json` |

**Always update `project-config.json`** to add the processed file(s) to the `documents_loaded` array:

```json
{
  "filename": "revised_schedule_020126.pdf",
  "type": "schedule",
  "discipline": null,
  "date_loaded": "2026-02-12",
  "file_size": "2.1 MB",
  "sections_extracted": ["milestones", "critical_path", "current_phase", "weather_sensitive_activities"],
  "data_files_updated": ["schedule.json"],
  "coverage_notes": "Substantial completion moved to 07/01/2026. Steel erection added to critical path.",
  "confidence": "high"
}
```

Note the added `file_size` field (used for incremental detection in Step 3A) and `data_files_updated` field (shows which files were touched).

## Step 7: Regenerate Project Memory File

After processing documents and merging intelligence into the config, regenerate the `CLAUDE.md` project memory file to reflect the new intelligence. This ensures that Claude has the latest project context at the start of the next session.

The CLAUDE.md file should be updated with:
- Latest intelligence from newly loaded documents
- Current RFI and submittal status
- Updated procurement tracking
- Any new milestones or schedule changes
- New vendors or subcontractors

## Step 8: Summarize Changes

Tell the user what was extracted and what changed. Example:

"Got it. I processed the updated schedule and new sub list. Here's what changed:
- Substantial completion moved from 06/15 to 07/01
- Steel erection is now on the critical path
- Added 2 new subs: ABC Mechanical (HVAC) and Smith Electric (electrical)
- 3 milestones updated with new dates
- Identified 4 weather-sensitive activities for automatic threshold checking
- Extracted 12 open RFIs from RFI log, 5 over 7 days old
- Processed submittal log: 8 pending, 3 under review for 12+ days, 4 approved

Your daily reports will now reference the updated schedule, new subs, and RFI/submittal status. The CLAUDE.md project memory file has been regenerated with the latest intelligence."
