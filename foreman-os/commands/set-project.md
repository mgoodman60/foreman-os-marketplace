---
description: Set up a project with document intelligence for daily reports
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [project name]
---

Set up a new project or resume an existing one. This command is the entry point for every project — run it once to configure, then again any time you open the same project folder to pick up where you left off.

Read the project-data skill at `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` before proceeding. This command handles project setup and folder scanning — actual document extraction is handled by `/process-docs`.

---

## Step 1: Detect Project State

Search for `project-config.json` in the user's working directory. Check these locations in order:
1. `AI - Project Brain/project-config.json`
2. `project-config.json` in the working directory root

Also check for `CLAUDE.md` in the working directory root.

### Path A — Existing Project Found

If a valid config file exists, this is a **project resume**. Do NOT re-run setup. Instead:

1. Load the config and read `CLAUDE.md` if present
2. Present a brief welcome-back summary:

   > **Morehead One Senior Care** (MOSC) — Job #825021
   > Last report: MOSC-042 (Feb 17, 2026)
   > 12 subs on file · 3 open RFIs · 2 submittals pending review
   > Next milestone: Roof dry-in — Mar 1 (11 days)
   >
   > You're ready to go. What would you like to do?

3. **Do not ask any setup questions.** The user is here to work, not to reconfigure.
4. If the user explicitly asks to update something (basics, folder mapping, add docs), then jump to the relevant step below. Otherwise, stop here — the project is loaded and ready.
5. Refresh `CLAUDE.md` if any data has changed since it was last written (compare `last_updated` date).

### Path B — No Project Found (New Setup)

If no config exists, this is a **new project setup**. Proceed through Steps 2–7 below.

Before starting, try to infer project info from the folder name. Common patterns:
- `825021 - Morehead One Senior Care` → job number = 825021, project name = Morehead One Senior Care
- `MOSC - Morehead One` → project code = MOSC, project name = Morehead One
- Just a name like `Morehead Senior Care` → project name = Morehead Senior Care

Use anything detected as defaults in Step 3 so the user has less to type.

---

## Step 2: Auto-Detect Folder Structure

Scan the user's working directory for numbered folders matching the pattern `## - Name/` (two digits, space, dash, space, then the folder name). Also check for `AI - Project Brain/`.

For each detected folder, map it to the appropriate `folder_mapping` key:

| Pattern Found | Maps To |
|---|---|
| `01 - Bidding*` | folder_mapping.bidding |
| `02 - Contract*` | folder_mapping.contracts |
| `03 - Subcontract*` | folder_mapping.subcontractors |
| `04 - Supplier*` | folder_mapping.suppliers |
| `06 - Submittal*` | folder_mapping.submittals |
| `07 - OAC*` | folder_mapping.oac_reports |
| `08 - Change*` | folder_mapping.change_orders |
| `09 - Schedule*` | folder_mapping.schedules |
| `09 - RFI*` | folder_mapping.rfis |
| `10 - *Photo*` | folder_mapping.photos |
| `11 - Daily*` | folder_mapping.daily_reports |
| `12 - Weekly*` | folder_mapping.weekly_reports |
| `13 - Spreadsheet*` | folder_mapping.spreadsheets |
| `14 - Safety*` | folder_mapping.safety |
| `AI - Project Brain*` | folder_mapping.ai_output |

If `AI - Project Brain/` doesn't exist, create it. This is where all config and data files will live.

Present the detected mapping to the user: "I found your project folder structure. Here's where I'll save files:"
- Show each mapping in a simple list
- Ask: "Does this look right, or do you want to adjust any folder assignments?"
- If a key has no matching folder, note it and suggest a fallback
- If `folder_mapping.rfis` has no dedicated folder, check if RFIs go in the schedule folder or suggest creating one

## Step 2B: Auto-Scan Subcontractor and Supplier Folders

If `folder_mapping.subcontractors` was detected (e.g., `03 - Subcontractors/`):

1. Scan for numbered sub-folders: `## - Name` pattern (e.g., "01 - Walker Construction", "08 - ELECTRICAL (PENDING)")
2. For each sub-folder found:
   - Extract the sub name from the folder name (strip the number prefix)
   - Check if the name contains "PENDING" — set status to "pending_contract"
   - Check for files inside containing "EXECUTED" in the filename — set status to "executed"
   - Otherwise set status to "active"
   - Auto-populate the `subcontractors` array in project_intelligence
3. Check for key files in the subcontractors root:
   - Contact list spreadsheet (`*Contact*List*.xlsx`) — if found, read it to populate foreman names, phone numbers, emails, and trades
   - Master SC template — note its presence

If `folder_mapping.suppliers` was detected (e.g., `04 - Suppliers/`):

1. Same pattern: scan for numbered sub-folders
2. For each supplier folder:
   - Extract supplier name
   - Auto-populate the `vendor_database` array
   - Scan inside for PO documents, delivery schedules, or product data
3. Check for master PO template in the supplier root

If `folder_mapping.spreadsheets` was detected:

1. Look for SC/PO Log file (pattern: `*SC*PO*Log*.xlsx` or `*SC-PO*.xlsx`)
2. If found, store the full path in `folder_mapping.sc_po_log`
3. Note: actual spreadsheet reading for procurement data happens via the material-tracker skill

Present the results: "I found X subcontractors and Y suppliers from your folder structure:"
- List each with their detected status (executed/active/pending)
- If a contact list spreadsheet was found: "I also found a contact list — I'll use it to fill in phone numbers and emails."
- Ask: "Anything to add or correct?"

---

## Step 3: Collect Project Basics

Collect these fields. Pre-fill anything detected from the folder name (Step 1, Path B). If the user provided info as arguments ($ARGUMENTS), use it and ask for the rest.

Required:
- **Project Name** — full name (e.g., "Morehead One Senior Care")
- **Project Code** — short code for report numbering (e.g., "MOSC")
- **Project Number** — company job number (e.g., "825021")

Optional (ask, accept blank):
- **Client/Owner** — owner or client name
- **Superintendent** — defaults to user's name if known
- **Architect** — architect firm name
- **Project Manager** — PM name
- **Engineers** — structural, MEP, civil engineer firms
- **Project Address** — site address
- **Building Type** — commercial, residential, healthcare, education, etc.
- **Gross Square Footage** — approximate building size
- **Number of Stories** — including below grade if applicable
- **Starting Report Number** — defaults to 1

---

## Step 4: Scan Project Documents

Scan all mapped subfolders for supported file types (`.pdf`, `.xlsx`, `.xls`, `.csv`, `.docx`, `.doc`). Build an inventory of what's available — do NOT extract or process content yet. For each file found, record:
- Filename and path
- File size
- Which mapped folder it's in (which tells you the likely document type)
- Whether it looks like a plan set, spec book, schedule, etc. based on filename patterns

Present the inventory grouped by folder. Example:

> **Documents Found in Your Project:**
>
> 📁 Plans (from `05 - Plans/`): 3 files — `Arch_Plans_Rev2.pdf` (45 MB), `Structural_Plans.pdf` (32 MB), `MEP_Plans.pdf` (28 MB)
> 📁 Specs (from `02 - Contract/`): 1 file — `Project_Specifications.pdf` (12 MB)
> 📁 Schedule (from `09 - Schedule/`): 1 file — `CPM_Schedule_012026.pdf` (2 MB)
> 📁 Subcontractors: 8 sub folders detected (from Step 2B)
> 📁 Submittals (from `06 - Submittals/`): 14 files
> 📁 Safety (from `14 - Safety/`): 2 files — `Safety_Plan.pdf`, `SWPPP.pdf`
>
> **Not found:** Geotechnical report, RFI log, contract documents

This is inventory only. Actual document processing happens via `/process-docs`.

---

## Step 5: Save the Config

Initialize the project data files in `folder_mapping.ai_output` (typically `AI - Project Brain/`). Use the multi-file data store structure defined in the project-data skill:

**Core Configuration Files (created now):**
- `project-config.json` — project basics, folder mapping, documents loaded list, report tracking, version history
- `directory.json` — subcontractors (from Step 2B) and vendor database (from Step 2B)
- `plans-spatial.json` — empty, ready for document processing
- `specs-quality.json` — empty, ready for document processing
- `schedule.json` — empty, ready for document processing
- `daily-report-data.json` — empty reports array, ready for the dashboard

**Empty Log Files (created now, populated via commands):**
- `rfi-log.json` — empty rfi_log array
- `submittal-log.json` — empty submittal_log array
- `procurement-log.json` — empty procurement_log array
- `change-order-log.json` — empty change_order_log array
- `inspection-log.json` — empty inspection_log and permit_log arrays
- `meeting-log.json` — empty meeting_log array
- `punch-list.json` — empty punch_list array
- `delay-log.json` — empty delays array
- `pay-app-log.json` — empty sov and pay_applications arrays
- `drawing-log.json` — empty drawings array with revision tracking structure
- `closeout-data.json` — empty closeout_status, commissioning, and warranties structures

**Tracking & Analytics Files (created now, populated via commands):**
- `cost-data.json` — empty budget_by_division array (populated from specs/schedule via `/cost`)
- `labor-tracking.json` — empty labor_entries and crew_summaries arrays
- `safety-log.json` — empty incidents, near_misses, toolbox_talks, and osha_logs arrays
- `quality-data.json` — empty inspections array organized by trade/phase
- `visual-context.json` — empty site_context and design_intent structures
- `rendering-log.json` — empty renderings array

At this point, configuration and directory files have data from folder scanning. The intelligence files (`plans-spatial.json`, `specs-quality.json`, `schedule.json`, quantities, locations) will be enriched by `/process-docs` as documents are processed. Log and tracking files are pre-initialized empty and will be populated via their respective commands (`/prepare-rfi`, `/material-tracker add`, `/change-order add`, `/safety log`, `/labor log`, `/cost`, `/quality log`, `/drawings update`, etc.).

**CRITICAL: All data files go to folder_mapping.ai_output, NOT the project root.**

---

## Step 6: Startup Report

This is the most important step. Based on the document inventory from Step 4 and the folder scan from Step 2, generate a personalized project startup report. This tells the user exactly what they have, what's missing, and what to do next.

### Section 1: What You've Got

Summarize what was set up from folder scanning alone (no document extraction yet):

> **Project Set Up: Morehead One Senior Care (MOSC) — Job #825021**
>
> ✅ Folder structure mapped (12 folders detected)
> ✅ 8 subcontractors loaded from folder names (5 executed, 2 active, 1 pending)
> ✅ 3 suppliers loaded from folder names
> ✅ Contact list found — phone/email populated for 6 subs
> ✅ SC/PO Log found — ready for material tracking sync
> ✅ Reports will start at MOSC-001

### Section 2: Documents Ready to Process

List every document found in Step 4, grouped by priority. Tell the user what intelligence each will unlock:

> **High Priority — Run `/process-docs` on these first:**
>
> 1. `Project_Specifications.pdf` (12 MB) — Unlocks: weather thresholds, hold points, material specs, testing requirements, quality tolerances. *These feed into every daily report and inspection.*
> 2. `CPM_Schedule_012026.pdf` (2 MB) — Unlocks: milestones, critical path, long-lead items, weather-sensitive activities. *Required for `/morning-brief` and `/look-ahead`.*
> 3. `Arch_Plans_Rev2.pdf` (45 MB) — Unlocks: grid lines, building areas, floor levels, room schedule, site layout. *Required for location references in reports and RFIs.*
>
> **Medium Priority:**
>
> 4. `Structural_Plans.pdf` (32 MB) — Unlocks: structural grid, foundation details, quantities for concrete/rebar/steel.
> 5. `MEP_Plans.pdf` (28 MB) — Unlocks: mechanical/electrical/plumbing layout, fixture counts, spatial coordination data.
> 6. `Safety_Plan.pdf` — Unlocks: fall protection zones, confined spaces, crane exclusion zones. *Feeds safety checks in daily reports.*
> 7. `SWPPP.pdf` — Unlocks: BMP locations, rainfall inspection triggers. *Auto-triggers SWPPP inspection reminders.*
>
> **Also Available:**
>
> 8–21. 14 submittals in `06 - Submittals/` — Run `/submittal-review` on these individually as needed.

### Section 3: What's Missing

Flag important document types NOT found in any folder:

> **Not Found — Consider Adding:**
>
> ⚠️ **Geotechnical report** — Without this, I can't check compaction requirements, bearing capacity, or soil conditions. If you have one, drop it in any folder and run `/process-docs`.
> ⚠️ **Contract documents** — No contract or scope of work found. This means I won't know about liquidated damages, working hour restrictions, or documentation requirements.
> ⚠️ **RFI log** — No running RFI log found. You can start tracking RFIs with `/prepare-rfi`, or if you have an existing log, run `/process-docs` to import it.

Only flag document types that are genuinely useful. Don't flag obscure items. Focus on specs, schedule, plans, geotech, contract, safety, and SWPPP.

### Section 4: Recommended Next Steps

Give a numbered action list based on what was actually found:

> **Your Getting-Started Checklist:**
>
> 1. Run `/process-docs` — Start with your specs and schedule (highest impact). Then plans. I'll walk you through it. Run `/process-docs scan` anytime to see what's new in your folders.
> 2. Run `/morning-brief` — Once docs are processed, this gives you a daily briefing with weather, schedule, and open items.
> 3. Run `/log` — Start logging field observations throughout the day. I'll sort them into report sections.
> 4. Run `/daily-report` — Generate your first daily report when you're ready.
>
> **As the project progresses:**
> - `/material-tracker` — Track deliveries and verify specs once materials start arriving
> - `/look-ahead` — Generate 3-week lookaheads for coordination meetings
> - `/prepare-rfi` — Draft RFIs with auto-filled project references
> - `/submittal-review` — Check submittals against spec requirements
> - `/inspections` — Schedule and track inspections and permits
> - `/meeting-notes` — Record OAC and coordination meeting minutes with action item tracking

### Adapting the Report

The startup report should adapt based on what's actually there. Examples:
- If NO documents were found at all: emphasize that `/process-docs` is the critical next step and explain what each document type unlocks
- If the project has a rich folder with many docs: prioritize which to process first based on what gives the most immediate value (specs + schedule + plans)
- If subcontractors were found but no specs: note that daily reports will have sub names but won't be able to validate work against specifications yet
- If a schedule was found: mention that `/morning-brief` and `/look-ahead` will be available once it's processed
- If no schedule was found: suggest that even a simple milestone list helps, and they can enter one manually

---

## Step 7: Generate Project Memory File

After saving the config, generate a `CLAUDE.md` file in the user's working directory root (NOT in AI - Project Brain — it goes at the root so Claude finds it immediately when the folder is opened).

This file serves as a quick-reference working memory that Claude reads at the start of each session to instantly understand the project context.

The CLAUDE.md file should contain:

```markdown
# {Project Name} — Project Memory

> Auto-generated by Foreman_OS. Updated each time project data changes.
> Last updated: {date}

## Project Basics
- **Project**: {name} ({code}) — Job #{number}
- **Client**: {client}
- **Super**: {superintendent} | **PM**: {project_manager}
- **Architect**: {architect}
- **Address**: {address}
- **Type**: {building_type} | {gross_sf} SF | {stories} stories

## Current Status
- **Phase**: {current_phase} — {percent_complete} complete
- **Report Count**: {last_report_number} reports generated
- **Next Milestone**: {nearest milestone name} — {date} ({days away} days)

## Key Intelligence Summary
- **Grid**: Columns {columns}, Rows {rows}
- **Building Areas**: {comma-separated list of area names}
- **Subs on Project**: {count} subs — {comma-separated list of active sub names}
- **Active RFIs**: {count} open
- **Pending Submittals**: {count} under review
- **Critical Procurements**: {count} items tracked

## Weather Thresholds to Watch
{list key thresholds: e.g., "- Concrete: min 40°F, max 90°F (Section 03 30 00)"}

## Active Issues
{list from most recent daily report open_items}

## Commands Available
/log, /morning-brief, /daily-report, /dashboard, /look-ahead, /submittal-review, /prepare-rfi, /weekly-report, /material-tracker, /set-project, /update, /process-docs

## Folder Structure
{show folder_mapping entries that are populated}
```

This CLAUDE.md should be regenerated (overwritten) whenever project data changes significantly — after /set-project, /process-docs, /daily-report, or any command that modifies the config.
