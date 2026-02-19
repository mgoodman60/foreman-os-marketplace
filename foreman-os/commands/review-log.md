---
description: Review today's intake log organized by report section before generating the daily report
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint:
---

Review everything logged today via `/log`, organized by daily report section. Shows coverage gaps so the superintendent can fill in missing sections before running `/daily-report`.

Read the intake-chatbot skill at `${CLAUDE_PLUGIN_ROOT}/skills/intake-chatbot/SKILL.md` and the project-data skill at `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` before proceeding.

## Step 1: Load Context

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `daily-report-intake.json` (today's intake log)
- `directory.json` (subcontractors array — for resolving sub names)
- `schedule.json` (milestones — for schedule coverage check)

If no config exists, still attempt to load the intake log from the working directory root.

## Step 2: Load Today's Intake Log

Read `daily-report-intake.json`. If it doesn't exist or has no entries for today's date:
- Tell the user: "No entries logged today yet. Use `/log` to start capturing field observations."
- Exit.

## Step 3: Organize by Report Section

Group all intake entries by their classified section:

1. **Weather / Site Conditions**
2. **Crew / Work Performed**
3. **Materials / Deliveries**
4. **Equipment**
5. **Schedule Updates**
6. **Visitors / Inspections**
7. **Photos**
8. **General Notes**

For each section, show:
- Number of entries
- Summary of what was logged (sub names, locations, key details)
- The raw input for reference

## Step 4: Identify Coverage Gaps

Flag any sections with **no entries**:
- "No weather logged yet — what were conditions today?"
- "No equipment noted — anything on site or down?"
- "No schedule updates — any milestones or delays to report?"

If project intelligence is loaded, add smart gap detection:
- If subs are scheduled to be on site this week (per `schedule.json`) but none were logged, note: "These subs are scheduled this week but weren't logged: [sub names]"
- If a milestone is within 7 days, note: "[Milestone] is approaching — any update?"

## Step 5: Present Summary

Display a clean summary:

```
Today's Log Review — [date]
[X] entries across [Y] sections

WEATHER: ✓ 1 entry — Partly cloudy, 72°F
CREW: ✓ 4 entries — Walker (6), Smith Electric (3), ABC Mechanical (4), Ready Paint (2)
MATERIALS: ✓ 1 entry — Rebar delivery from Harris
EQUIPMENT: ✗ No entries
SCHEDULE: ✗ No entries
VISITORS: ✓ 1 entry — Inspector, footing inspection passed
PHOTOS: ✗ No photos uploaded
NOTES: ✗ No entries

Gaps: Equipment, Schedule, Photos, Notes
```

## Step 6: Prompt for Additions

After showing the summary, ask: "Want to add anything before generating the report? You can fill gaps now or run `/daily-report` and add during generation."

If the user provides additional observations, process them using the same intake-chatbot classification and enrichment pipeline from `/log`, append to the intake log, and show the updated summary.
