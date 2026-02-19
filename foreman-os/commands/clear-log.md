---
description: Clear today's intake log and start fresh (archives cleared entries)
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint:
---

Clear today's intake log entries. Archives the cleared data so nothing is permanently lost, then starts a fresh log for the day.

Read the project-data skill at `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` before proceeding.

## Step 1: Load Context

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (folder_mapping for output paths)
- `daily-report-intake.json` (today's intake log)

## Step 2: Check for Existing Log

Read `daily-report-intake.json`. If it doesn't exist or has no entries for today:
- Tell the user: "No entries to clear — today's log is already empty."
- Exit.

## Step 3: Confirm with User

Show the user what will be cleared:
- Number of entries
- Time range (first entry to last entry)
- Brief summary of sections covered

Ask: "Clear [X] entries from today's log? They'll be archived in case you need them."

If the user confirms, proceed. If not, exit.

## Step 4: Archive

Before clearing, save the current entries to an archive file:
- Filename: `daily-report-intake-archive-{YYYY-MM-DD}-{HHmmss}.json`
- Save in `folder_mapping.ai_output` (or working directory root if not configured)
- Include all current entries with their timestamps, classifications, and enrichments

## Step 5: Clear the Log

Reset `daily-report-intake.json` to an empty state for today:

```json
{
  "date": "2026-02-19",
  "entries": []
}
```

## Step 6: Confirm

Tell the user: "Log cleared. [X] entries archived to [archive filename]. Start logging with `/log`."

Log the clear action in `project-config.json` version_history:
```json
{
  "timestamp": "2026-02-19T14:30:00Z",
  "command": "clear-log",
  "details": "Cleared X entries, archived to [filename]"
}
```
