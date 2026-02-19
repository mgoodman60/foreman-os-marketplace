---
description: Search for suppliers and vendors for project materials
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
argument-hint: [material or spec section]
---

Find vendors and suppliers for project materials. Searches the existing vendor database first, then optionally searches the web. Saves results for future reference.

This command is a convenience shortcut that routes to the material-tracker skill's vendor search capability.

Read the material-tracker skill at `${CLAUDE_PLUGIN_ROOT}/skills/material-tracker/SKILL.md` and the project-data skill at `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` before proceeding.

## Step 1: Load Project Intelligence

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `directory.json` (vendor_database — existing vendor records)
- `specs-quality.json` (spec_sections — for material requirement lookup)
- `procurement-log.json` (existing procurement items for this material)
- `submittal-log.json` (approved submittals with manufacturer data)

## Step 2: Parse Input

Extract the material or spec section from `$ARGUMENTS`:
- Material name: `/find-vendor door frames`, `/find-vendor concrete`, `/find-vendor roofing membrane`
- Spec section: `/find-vendor 08 1000`, `/find-vendor 07 5400`
- No argument: Ask "What material or product are you looking for vendors for?"

If a spec section is provided, look up the material requirements from `specs-quality.json` to understand exactly what's needed (standards, certifications, performance requirements).

## Step 3: Search Existing Vendor Database

Check `directory.json` vendor_database for matching vendors:
- Match on material category, capabilities, or product lines
- Show results with: vendor name, contact info, materials supplied, certifications, past project history

If matches are found, display them:
```
Found 2 vendors in your database for [material]:

1. ABC Supply Co — (555) 123-4567 — abc@supply.com
   Materials: Door frames, hollow metal, specialty frames
   Certifications: SDI-certified, fire-rated assemblies
   Last quote: 01/15/2026

2. Metro Building Products — (555) 987-6543 — sales@metro.com
   Materials: Commercial doors and frames
   Notes: Used on previous project, good lead times
```

## Step 4: Check Approved Submittals

If there's an approved submittal for this material type in `submittal-log.json`:
- Show the approved manufacturer and product
- Note: "You have an approved submittal for [product] from [manufacturer]. Contact them directly or find a distributor."

## Step 5: Offer Web Search

If the user needs more options or no database matches were found:
- Ask: "Search the web for additional [material] suppliers? (yes/no)"
- If yes, run targeted web searches for suppliers in the project's region
- Present results with contact info, capabilities, and relevant details
- Focus on suppliers who carry products meeting the spec requirements identified in Step 2

## Step 6: Save Results

For any new vendors the user wants to keep:
- Add to `directory.json` vendor_database with: name, contact, materials, capabilities, certifications, source, date_added
- Link to procurement item if one exists (suggest creating one: "Run `/material-tracker add` to start tracking procurement for this material")

Log the search in `project-config.json` version_history:
```json
{
  "timestamp": "2026-02-19T11:00:00Z",
  "command": "find-vendor",
  "details": "Searched for [material] vendors — [X] database matches, [Y] web results"
}
```

Present summary: "Found [X] vendors for [material]. [New vendors saved to database / Suggest next steps]."
