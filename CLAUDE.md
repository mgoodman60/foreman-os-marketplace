# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

This is **foreman-os-marketplace**, a cowork plugin marketplace repository containing the **Foreman_OS** plugin (v4.0.2) — a construction superintendent operating system with 41 skills, 36 commands, and 21 field-reference documents. It runs as a plugin inside the cowork platform.

## Repository Structure

```
.claude-plugin/marketplace.json    — Marketplace manifest (lists plugins)
foreman-os/                        — The plugin itself
  .claude-plugin/plugin.json       — Plugin metadata (name, version, description)
  README.md                        — Full documentation of commands, skills, and data files
  commands/                        — 36 slash-command definitions (markdown files)
  skills/                          — 41 skill directories, each with SKILL.md + references/
```

There is no build system, no tests, no package manager. The entire codebase is markdown files, JSON configs, and a few Python reference scripts.

## Architecture

### Plugin System
- `marketplace.json` at root registers plugins by name and source path
- Each plugin has a `plugin.json` with name, version, description, author
- Commands are markdown files with YAML frontmatter (`description`, `allowed-tools`, `argument-hint`)
- Skills are directories containing a `SKILL.md` and an optional `references/` folder

### Command → Skill Relationship
Commands (in `commands/`) are the user-facing entry points (invoked as `/log`, `/daily-report`, etc.). Each command's markdown body tells the AI which skill(s) to read before executing. Skills (in `skills/`) contain the deep logic, classification rules, extraction pipelines, and data schemas.

Example chain: `/log` command → reads `intake-chatbot` skill + `project-data` skill → classifies input → enriches with project intelligence → writes to `daily-report-intake.json`.

### Key Conventions
- Commands reference skills via `${CLAUDE_PLUGIN_ROOT}/skills/<skill-name>/SKILL.md` — this variable resolves to the `foreman-os/` directory at runtime
- Commands also reference cowork platform skills (e.g., `docx`, `pdf`, `construction-takeoff`) for output formatting
- All project data files are JSON, stored in the user's `AI - Project Brain/` folder (or working directory root as fallback)
- The `project-data` skill (`skills/project-data/SKILL.md`) is the central data backbone — nearly every command reads it first

### Data Flow
Documents → `document-intelligence` skill (three-pass extraction) → structured JSON files → consumed by all other commands/skills. The multi-file data store includes:
- `project-config.json` — master config, folder mapping, document tracking
- `plans-spatial.json` — grid lines, rooms, quantities, site layout
- `specs-quality.json` — spec sections, materials, thresholds, tolerances
- `schedule.json` — milestones, critical path, lookahead history
- `directory.json` — subs, vendors, assignments
- Various `*-log.json` files for RFIs, submittals, procurement, delays, etc.

### Python Reference Scripts
Three Python files exist under `skills/document-intelligence/references/` and `skills/quantitative-intelligence/references/` — these are reference implementations for DWG/DXF conversion, DXF parsing, visual plan analysis, sheet cross-referencing, and calculation bridging. They are not executed directly by the plugin but serve as reference code for the AI.

## Editing Patterns

When adding a **new command**: create a markdown file in `foreman-os/commands/` with YAML frontmatter (`description`, `allowed-tools`, `argument-hint`) and step-by-step instructions that reference the relevant skills.

When adding a **new skill**: create a directory under `foreman-os/skills/<skill-name>/` with a `SKILL.md` (YAML frontmatter with `name`, `description`, `version`) and optionally a `references/` folder for supporting docs or scripts.

When modifying the **plugin manifest**: update both `marketplace.json` (root) and `plugin.json` (`foreman-os/.claude-plugin/`) if the description or metadata changes.
