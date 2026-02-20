---
description: Generate a 3-week (or custom) construction lookahead schedule
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
argument-hint: [optional: number of weeks, default 3]
---

## Overview
Generate a construction lookahead schedule from project intelligence. This command reads critical project data including schedule, subs, procurement, RFIs, and submittals to create a forward-looking view of upcoming work.

**Skills Referenced:**
- `${CLAUDE_PLUGIN_ROOT}/skills/look-ahead-planner/SKILL.md` - Lookahead scheduling methodology
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` - Project data extraction and management
- `${CLAUDE_PLUGIN_ROOT}/skills/field-reference/SKILL.md` - Field reference knowledge for trade sequencing (mep-coordination-guide.md), site logistics (site-logistics-guide.md), and activity-specific constraints

## Execution Steps

### 1. Load Project Configuration
- Read project data files to retrieve:
  - Schedule data from `schedule.json` (activities, durations, dependencies, critical path)
  - Subcontractor roster from `directory.json` (subcontractors and scopes)
  - Procurement log from `procurement-log.json` (long-lead items, delivery dates)
  - RFI log from `rfi-log.json` (open items, resolution impact)
  - Submittal log from `submittal-log.json` (pending reviews)
  - Project location from `project-config.json` (for weather forecasting)
  - Weather thresholds from `specs-quality.json` (weather_thresholds)

### 2. Determine Lookahead Window
- Default: 3 weeks
- Check `$ARGUMENTS` for custom week count (1-12 weeks)
- Calculate date range from today

### 3. Extract Activities in Window
- Filter schedule for activities starting or ongoing within the window
- Include all critical path activities
- Note dependencies extending beyond the window

### 4. Map Each Activity to Resources
For each activity, gather:
- **Subcontractor**: Who is responsible
- **Location**: Grid reference, area, room number
- **Materials**: Required materials and their delivery status
- **Equipment**: Needed equipment and availability
- **Weather Constraints**: Temperature, humidity, precipitation requirements
- **Prerequisite Blockers**: Inspections, permits, approvals

### 5. Check for Blockers
Identify blocking items:
- Pending RFIs that affect the scope
- Pending submittals affecting procurement
- Delayed material deliveries
- Open permit requests
- Scheduled inspections

### 6. Fetch Weather Forecast
- Use WebSearch to fetch weather forecast for project location
- Extract 7-day and 14-day forecasts
- Note any weather-critical activities

### 7. Build Daily Breakdown
- Create day-by-day view for the window
- Show which subcontractors and crews are scheduled
- Highlight milestones and deliverables
- Flag critical dates

### 8. Generate Interactive HTML Output
- Create file: `{PROJECT_CODE}_Lookahead_{date}.html` — save to `folder_mapping.ai_output`. Fall back to user's output folder if not populated.
- Include:
  - Daily schedule view (table/calendar format)
  - Weather forecast display
  - Subcontractor schedule by crew
  - Material delivery timeline
  - Critical path items highlighted
  - Blockers and risks flagged
  - Interactive toggles for detail levels

### 9. Update Project Configuration
- Save lookahead summary to `schedule.json` lookahead_history array
- Include: window dates, critical activities, blockers identified, date generated

### 10. Present to User
Display:
- Summary: "X activities scheduled for [date range], Y blockers identified, Z weather impacts"
- Key deliverables and milestones
- Top blockers and recommended actions
- Link to interactive HTML file
- Suggestion: "Run /submittal-review to clear blocking submittals"

