---
description: Scan project folders for new or changed documents
allowed-tools: Read, Bash, Glob, Grep
argument-hint:
---

Lightweight folder scan. Compares what's in the project folders against what's already been processed. Reports what's new, what's changed, and what's ready to process. Does NOT extract or process any documents — that's what `/process-docs` is for.

Read the project-data skill at `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` before proceeding.

## Step 1: Load Project Config

Search for `project-config.json` in the user's working directory. Check these locations in order:
1. `AI - Project Brain/project-config.json`
2. `project-config.json` in the working directory root

If not found, tell the user: "No project is set up yet. Run `/set-project` first."

Load `project-config.json` and read:
- `folder_mapping` — where to scan
- `documents_loaded` — what's already been processed

## Step 2: Scan Mapped Folders

Walk through every folder in `folder_mapping` that has a path set. For each folder, list all supported file types (`.pdf`, `.xlsx`, `.xls`, `.csv`, `.docx`, `.doc`). Record:
- Filename
- Full path
- File size
- Parent folder (which tells you the likely document type)

## Step 3: Compare Against documents_loaded

For every file found in Step 2, check it against the `documents_loaded` array:

- **Not in documents_loaded** → **NEW**
- **In documents_loaded, same filename and file size** → **UNCHANGED**
- **In documents_loaded, same filename but different file size** → **UPDATED** (file was modified since last processing)

## Step 4: Present Scan Report

Show the user a clean summary of what's changed. Group by status:

> **Project Update Scan — Morehead One Senior Care**
> *Last full scan: Feb 15, 2026 · 52 documents on file*
>
> **🆕 New Files (3):**
> 1. `ASI-003_Window_Revision.pdf` (480 KB) — in `08 - Change Orders/` — Likely: ASI
> 2. `Submittal_08-1000_Doors.pdf` (2.1 MB) — in `06 - Submittals/` — Likely: submittal package
> 3. `Updated_Sub_List_021826.xlsx` (85 KB) — in `03 - Subcontractors/` — Likely: sub list update
>
> **🔄 Updated Files (1):**
> 4. `CPM_Schedule.pdf` — in `09 - Schedule/` — was 2.3 MB on Feb 5, now 2.8 MB
>
> **✅ Unchanged: 48 files** — already processed, no changes detected.
>
> Run `/process-docs` to extract intelligence from the new and updated files.

### When Nothing's New

If everything matches `documents_loaded`:

> **Project Update Scan — Morehead One Senior Care**
> *52 documents on file · All up to date*
>
> No new or changed files detected. Your project intelligence is current.

### When No Documents Have Been Processed Yet

If `documents_loaded` is empty (fresh project after `/set-project`):

> **Project Update Scan — Morehead One Senior Care**
> *0 documents processed yet · 23 files found in project folders*
>
> **All files are new — nothing has been processed yet.**
>
> Run `/process-docs` to start extracting project intelligence. I'd recommend starting with your specs and schedule for the biggest impact.

Then list all files grouped by folder, same as the `/set-project` startup report inventory.

## What This Command Does NOT Do

- Does NOT extract content from any documents
- Does NOT modify any data files
- Does NOT process or classify documents beyond filename/folder guessing
- Does NOT write anything — this is a read-only scan

It's safe to run `/update` as often as you want. It just looks and reports.
