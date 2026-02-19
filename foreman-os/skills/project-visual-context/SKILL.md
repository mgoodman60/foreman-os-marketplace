---
name: project-visual-context
description: >
  Gather site context, exterior conditions, and interior design intent for AI rendering. Trigger phrases include "site context", "visual context", "gather context", "rendering context". Dependencies: project-config, plans-spatial, specs-quality, schedule, directory.
version: 1.0.0
---

# Project Visual Context Skill

## Overview

The **project-visual-context** skill guides you through a structured interview to gather comprehensive visual context about your construction project. This context enables the rendering-generator skill to produce accurate, photorealistic AI renderings at any project phase.

Visual context includes:
- **Exterior conditions**: site setting, terrain, adjacent structures, vegetation, climate, orientation
- **Interior design intent**: design character, color palette, materials by room type, furniture, special features
- **Photo documentation**: site photos with AI-generated descriptions for reference

## When to Use

**Trigger:** `/site-context` command

**Timing:**
- Run BEFORE `/render` for best results
- Re-run at major project phases to update context as conditions change
- Partial updates welcome — update only what's changed

**Best Results:** Run after project kick-off, before major design/construction phases

## How the Skill Works

The skill operates in **3 phases** over a single session:

1. **Exterior Context** — Gather site setting, terrain, adjacent structures, vegetation, climate, orientation, construction status
2. **Interior Design Intent** — Gather design character, color palette, finishes, furniture, and special features by room type
3. **Photo Documentation** — Process uploaded site/inspiration photos with AI analysis

At the end, the skill generates **visual-context.json** saved to `AI - Project Brain/` folder.

## Starting the Skill

### Initial Setup

When you trigger `/site-context`:

1. The skill checks if **visual-context.json** already exists
   - **If EXISTS:** Load it and ask "What would you like to update? (exterior / interior / photos / all)" → Jump to incremental update workflow
   - **If NEW:** Proceed with full interview below

2. The skill auto-populates data from existing project files:
   - **project-config.json** → `project_code`, building type, address, occupancy
   - **plans-spatial.json** → room types, areas, dimensions, door schedule
   - **specs-quality.json** → finish schedule, material specs, casework specs
   - **schedule.json** → current phase
   - **directory.json** → architect, owner contacts (for design preferences)

Pre-populated data is shown to the user for confirmation/correction.

---

## Phase 1: Exterior Context

### Step 1.1: Confirm Building Basics

Display pre-populated data:
```
Project: [project_code]
Address: [address]
Building Type: [type] ([occupancy] occupants)
Building Size: [SF]
Current Phase: [phase from schedule]
```

Ask: "Are these details correct? (yes/no/edit)"

If user edits, update the displayed values.

### Step 1.2: Setting Type

Ask: "What best describes the **site setting**?"
- **Rural** — farmland, open countryside, minimal nearby structures
- **Suburban** — residential neighborhoods, scattered commercial, green space
- **Urban** — dense development, city block, multiple adjacent buildings, minimal green
- **Industrial** — manufacturing area, warehouses, commercial corridors, paved surfaces
- **Campus** — institutional grounds (hospital, university, corporate), multiple buildings with open space
- **Mixed** — combination of above characteristics

Capture response.

### Step 1.3: Terrain Description

Ask: "Describe the **terrain** around the building:"
- Flat — level ground
- Sloping/Rolling — gentle elevation changes
- Hillside — significant elevation change, building may be cut into slope
- Valley — building in low point
- Elevated/Promontory — building on high ground

Ask for any additional details (e.g., "hillside with rock outcrops," "flat cleared site in forest").

Capture response.

### Step 1.4: Adjacent Structures

Ask: "Describe buildings/structures **adjacent** to this site in each direction:"

For each cardinal direction (North, South, East, West):
- Type of adjacent structure (residential, commercial, industrial, open land, water, etc.)
- Distance (immediate neighbor, across street, far away)
- Height relative to this building (taller, similar, shorter)
- Any notable features (parking lots, vegetation screening, etc.)

Capture responses for each direction.

### Step 1.5: Vegetation & Landscaping

Ask: "Describe **existing vegetation** on or near the site:"
- Types of trees (deciduous, conifer, mixed)
- Density (sparse, scattered, dense forest)
- Ground cover (grass, shrubs, bare soil, paved)
- Any significant vegetation to be preserved or removed

Ask: "Is **landscaping planned** for this project? (yes/no/unknown)"

If yes: "Describe the landscaping intent" (e.g., "native plantings, bioswale screening to south, street trees along entry drive")

Capture responses.

### Step 1.6: Climate & Season

Ask: "Select the **climate zone** for this location:"

Display options based on address (or ask user):
- **Four-season** (temperate) — spring, summer, fall, winter
- **Mild winter** — cool season, rarely freezes, year-round green
- **Tropical** — warm, high humidity, distinct wet/dry seasons
- **Arid/Desert** — dry, minimal precipitation, extreme temperature swings
- **Mediterranean** — warm dry summer, cool wet winter
- **Monsoon** — distinct rainy season, dry season

Capture response.

Ask: "What is the **region/zone**?" (e.g., "USDA Zone 6a," "Sonoran Desert," "Pacific Northwest")

Ask: "For rendering purposes, which **season** best represents this project?"
- Spring (greening, fresh, moderate light)
- Summer (full foliage, bright, warm light)
- Fall (color change, golden light, clear skies)
- Winter (bare trees, diffuse light, snow possible)

Capture response.

Ask: "What is the **prevailing weather** you expect to show in renderings?" (e.g., "clear skies," "partly cloudy," "dramatic storm clouds," "morning fog")

Capture response.

### Step 1.7: Building Orientation

Ask: "**Which direction does the main entry face?**" (N, NE, E, SE, S, SW, W, NW)

Ask: "Which elevation faces **north**?" (e.g., "long side," "short side," "corner")

Ask: "Where is **parking** located?" (e.g., "south and east," "detached lot to north," "below building")

Ask: "Describe the **sun path** in your region during the default season you selected" (e.g., "low southern sun, dramatic shadows," "high overhead sun, minimal shadows," "strong western afternoon glare")

Capture responses.

### Step 1.8: Construction Status

Auto-populate from schedule if available:
```
Current Phase: [phase]
Expected Visible Work: [construction activities in progress]
Equipment on Site: [cranes, formwork, trailers, etc.]
```

Ask: "Are these details accurate? Anything to add or correct about the current construction status?"

Capture any corrections.

### Step 1.9: Site Photo Upload

Ask: "Would you like to upload **site photos** for reference? (yes/no)"

If yes:
- Invite user to upload photos in these categories:
  - **Aerial view** — drone/satellite view of site
  - **Street level** — approach view from public street
  - **Adjacent contexts** — nearby structures, street context
  - **Terrain** — ground conditions, slopes, drainage
  - **Vegetation** — trees, landscaping, ground cover
  - **Current conditions** — construction progress, existing site conditions
  - **Interior reference** — existing spaces for design intent

For each uploaded photo:
- Capture filename and category
- Use AI vision to analyze and generate description (e.g., "Mature oak trees lining the south property line, 40+ feet tall, dense canopy. Open lawn area extends north toward building site.")
- Store in visual-context.json

Ask: "Any other details about the **exterior/site context** we should capture?" (free-form text)

Capture response.

### End of Phase 1

Summarize exterior context to user:
```
EXTERIOR CONTEXT SUMMARY
Setting: [type]
Terrain: [description]
Adjacent (N/S/E/W): [cardinal descriptions]
Vegetation: [description]
Climate: [zone/region/seasons]
Building Faces: [direction] | Entry: [direction]
Parking: [location]
Photos Uploaded: [count]
```

Ask: "Ready to proceed to **Interior Design Intent**?" (yes/continue)

---

## Phase 2: Interior Design Intent

### Step 2.1: Design Character

Ask: "What is the **design character** of this project?"

Display options and explain:
- **warm_residential** — comfortable, residential aesthetic, lived-in feeling
- **modern** — clean lines, minimalist, contemporary materials
- **clinical** — healthcare/lab aesthetic, hygienic, functional, bright
- **hospitality** — hotel/restaurant aesthetic, welcoming, refined, service-oriented
- **institutional** — public building aesthetic, durable, formal, rule-based
- **industrial** — factory/warehouse aesthetic, raw materials, exposed systems
- **corporate** — office aesthetic, professional, polished, branded
- **educational** — school/university aesthetic, flexible, inspiring, activity-focused
- **retail** — commercial aesthetic, product-focused, dynamic, customer-facing

Capture response.

### Step 2.2: Color Palette

Ask: "Describe the **primary color** for the interior" (e.g., "warm gray," "soft white," "warm beige," "sage green," "charcoal blue")

Ask: "What is the **secondary color**?" (e.g., "light gray," "warm cream," "natural wood tone," "accent blue")

Ask: "What is the **accent color** for highlights and features?" (e.g., "warm copper," "deep teal," "warm orange," "muted sage")

Ask: "Do you have **inspiration photos** or color references? (yes/no)"

If yes:
- Invite user to upload reference images
- Store filenames in color_palette.reference_images

Capture all color responses.

### Step 2.3: Materials by Room Type

Load room types from plans-spatial.json (e.g., "Bedroom," "Common Area," "Kitchen," "Restroom," "Corridor," "Mechanical," etc.)

For each major room type, ask:

**"For [Room Type] spaces, please provide:"**

#### Flooring
Ask: "What **flooring material**?" (e.g., "polished concrete," "ceramic tile," "luxury vinyl plank," "natural wood," "rubber")

Ask: "What **finish/color**?" (e.g., "light gray," "warm oak," "matte," "polished")

#### Walls
Ask: "How are **walls finished**?" (e.g., "painted gypsum board," "tile wainscot + paint," "wood paneling," "exposed CMU," "vinyl wallcovering")

Ask: "What **color/material**?" (e.g., "soft white," "warm gray," "natural wood tone")

#### Ceiling
Ask: "What is the **ceiling type**?" (e.g., "gypsum board," "suspended acoustic tile," "exposed structure," "open beam," "coffered," "drop ceiling")

Ask: "What **color/finish**?" (e.g., "bright white," "light gray," "natural wood," "black exposed steel")

#### Base
Ask: "What **base/trim material** and finish?" (e.g., "painted wood base," "cove base rubber," "natural wood trim," "anodized aluminum")

#### Casework / Millwork
*Only ask if applicable for room type (e.g., yes for kitchens, bathrooms, offices; no for open corridors)*

Ask: "Describe **casework, cabinets, built-ins**" (e.g., "natural wood cabinetry, soft-close drawers, open shelving in entry," "stainless steel shelving in prep area")

#### Countertops
*Only ask if applicable (kitchens, bathrooms, nursing stations)*

Ask: "What **countertop material and finish**?" (e.g., "quartz counters, white," "solid surface, warm gray," "stainless steel," "sealed wood")

#### Hardware Finish
Ask: "What is the **hardware finish**?" (e.g., "polished chrome," "brushed nickel," "bronze," "oil-rubbed bronze," "stainless steel")

#### Furniture & Fixtures
Ask: "Describe the **furniture style** for [Room Type]" (e.g., "modern minimalist," "warm residential," "clinical institutional," "hospitality-grade")

Ask: "Any **special features or equipment**?" (e.g., "picture rails," "display niches," "accent lighting," "accent wall," "window seat," "fireplace")

### Step 2.4: Brand Standards & Owner Preferences

Ask: "Are there **brand standards, owner preferences, or design guidelines** we should know about?" (yes/no/text)

If yes: "Please describe" (e.g., "Must use warm wood tones," "Specific furniture brand," "Accessible/universal design priorities," "Sustainable materials preference")

Capture response.

### Step 2.5: Special Notes

Ask: "Any **special design notes** or unique features to capture?" (free-form text)

Examples:
- "Historic renovation — preserve original exposed beams"
- "High-end hospitality — luxury finishes throughout"
- "Adaptable spaces — movable walls and flexible furniture"
- "Daylit atrium — important focal point"
- "Outdoor living emphasis — indoor-outdoor flow"

Capture response.

### End of Phase 2

Summarize interior design to user:
```
INTERIOR DESIGN SUMMARY
Character: [type]
Color Palette: [primary] / [secondary] / [accent]
Room Types Documented: [count]
Brand/Owner Notes: [yes/no]
Special Features: [summary]
```

Ask: "Ready to proceed to **Photo Documentation**?" (yes/continue)

---

## Phase 3: Photo Documentation

### Step 3.1: Review Uploaded Photos

If photos were uploaded in Phase 1, display them:

```
UPLOADED PHOTOS
[photo 1 filename] — [category] — [AI analysis]
[photo 2 filename] — [category] — [AI analysis]
...
```

Ask: "Would you like to upload **additional inspiration or reference photos**?" (yes/no)

If yes:
- Invite user to upload more photos
- Accept categories: aerial, street, adjacent, terrain, vegetation, conditions, interior_reference, inspiration
- For each new photo:
  - Capture filename, category, direction (if applicable)
  - Use AI vision to generate description
  - Store in visual-context.json

### Step 3.2: Photo Descriptions

For each uploaded photo, the skill uses AI vision to generate a detailed description capturing:
- **Scene composition** — what's in the photo, scale, perspective
- **Materials visible** — colors, textures, conditions
- **Atmospheric qualities** — lighting, weather, time of day
- **Context clues** — adjacent structures, vegetation, hardscape, utilities visible
- **Notable features** — architectural details, landscape elements, construction progress

Store descriptions in visual-context.json under `exterior.photos[].analysis`.

Example:
```
{
  "id": "photo_001",
  "file": "site_aerial_02_2026.jpg",
  "type": "aerial",
  "direction": "north",
  "analysis": "Aerial view of 10-acre rural site in winter condition. Building footprint is cleared and graded, with concrete foundation work in progress. Mature deciduous trees line the southern and eastern property boundaries. Open rolling topography slopes gently northward. Gravel access road enters from the west. No adjacent structures visible within 500 feet. Overcast sky, ground conditions appear slightly moist."
}
```

### Step 3.3: Missing Photos Alert

If Phase 3 completes with few/no photos uploaded, ask:

"No photos uploaded yet. For best rendering results, would you like to upload **site photos** now? (yes/no/skip)"

If no: "You can always re-run `/site-context` to add photos later."

### End of Phase 3

Summarize photos:
```
PHOTO DOCUMENTATION
Total Photos: [count]
Categories: [aerial: 2, street: 1, terrain: 1, ...]
AI Descriptions Generated: [count]
```

---

## Finalizing and Saving

### Step 4.1: Final Review

Display the complete visual-context summary:

```
═══════════════════════════════════════════════════════════
VISUAL CONTEXT COMPLETE
═══════════════════════════════════════════════════════════

PROJECT: [project_code]
Last Updated: [timestamp]

EXTERIOR CONTEXT
  Setting: [type]
  Terrain: [description]
  Adjacent Structures: [N/S/E/W summary]
  Vegetation: [description]
  Climate: [zone/region] — [default season]
  Building Orientation: Faces [direction] | Entry [direction]
  Photos: [count] uploaded

INTERIOR DESIGN
  Character: [type]
  Colors: [primary] | [secondary] | [accent]
  Room Types: [count] documented
  Special Notes: [summary or "none"]

DOCUMENTATION
  Total Photos: [count]
  Next Steps: Ready for `/render` command
═══════════════════════════════════════════════════════════
```

Ask: "Does everything look correct? (yes/edit/add)"

If user selects edit or add:
- Ask: "Which section would you like to update? (exterior / interior / photos / all)"
- Jump to relevant phase and allow incremental updates

If yes:
- Proceed to save

### Step 4.2: Save visual-context.json

The skill generates visual-context.json following the schema in `/references/visual-context-schema.json`.

Structure:
```json
{
  "version": "1.0.0",
  "project_code": "[from project-config]",
  "last_updated": "[ISO 8601 timestamp]",
  "exterior": {
    "setting": { ... },
    "vegetation": { ... },
    "climate": { ... },
    "orientation": { ... },
    "photos": [ ... ],
    "construction_status": { ... }
  },
  "interior": {
    "design_character": "...",
    "color_palette": { ... },
    "materials_by_room_type": { ... },
    "furniture_by_room_type": { ... },
    "brand_standards": "...",
    "special_notes": "..."
  }
}
```

Save to: `AI - Project Brain/visual-context.json`

Display confirmation:
```
✓ visual-context.json saved to: AI - Project Brain/
```

### Step 4.3: Next Steps

Display guidance:

```
NEXT STEPS

1. RUN RENDERINGS
   Use `/render` command with specific elevation, view, or space.
   Example: /render elevation=south, phase=frame-erection, season=summer

2. ITERATE & REFINE
   If rendering quality isn't meeting expectations:
   - Re-run `/site-context` to update specific sections
   - Upload additional reference photos
   - Clarify design details

3. ARCHIVE PROGRESS
   Visual context is now available for the rendering-generator skill.
   Export renderings to stakeholders for design review and approvals.
```

---

## Incremental Updates

If visual-context.json **already exists**, the skill workflow changes:

### Initial Prompt

```
Visual context already exists for this project (last updated: [date]).

What would you like to do?
  1. Update specific section (exterior / interior / photos)
  2. Full refresh (re-run entire interview)
  3. View current context
  4. Cancel

Select: (1/2/3/4)
```

### Workflow: Update Specific Section

If user selects "Update specific section":

Ask: "Which section?"
- **Exterior** — site setting, terrain, adjacent structures, climate, orientation, construction status
- **Interior** — design character, color palette, materials, furniture, special features
- **Photos** — add/replace photos and descriptions

Based on selection:
- Load current section from visual-context.json
- Display current values
- Ask: "What would you like to change?"
- Collect updates
- Merge into existing visual-context.json
- Re-save with updated `last_updated` timestamp

### Workflow: Full Refresh

If user selects "Full refresh":
- Clear visual-context.json
- Run the complete 3-phase interview as described above

### Workflow: View Current Context

If user selects "View current context":
- Display the entire visual-context.json in formatted, readable summary
- Ask: "Would you like to update anything?" (yes/no)
- If yes, return to "Update specific section" workflow

---

## Error Handling & Edge Cases

### Missing Project Data
If required project files don't exist (project-config.json, plans-spatial.json):
- Display warning: "Some project data is missing. The skill will work, but may require more manual input."
- Allow user to proceed
- Skip auto-population steps and ask for manual input instead

### No Room Types Found
If plans-spatial.json doesn't provide room types:
- Ask user to manually list major room types (e.g., "bedroom, bathroom, living area, kitchen")
- Proceed with materials/furniture interview for those types

### Single-Story vs. Multi-Story
If building has multiple stories:
- Ask: "Are material finishes the **same on all floors**? (yes/no)"
- If no: "Please specify any differences by floor" (e.g., "Residential finishes: warm residential, public areas: institutional")
- Adjust interview accordingly

### Renovation vs. New Construction
If project is a renovation:
- Ask: "Should we document **existing conditions**? (yes/no)"
- If yes: "Describe existing materials/finishes you plan to preserve or replace"
- Include in special_notes

### Photo Upload Failures
If user attempts to upload photos but upload fails:
- Display error: "Photo upload failed. Please check file format (JPEG, PNG accepted)."
- Offer to continue interview without photos (can add later)
- Provide retry option

---

## Universal Design Principles

This skill is designed to work for **ANY building type and project phase**.

### Building Type Adaptation
- **Healthcare/Senior Care** (e.g., MOSC) → Emphasizes clinical finishes, accessibility features, wayfinding
- **Commercial Office** → Emphasizes corporate character, brand standards, flexible spaces
- **Retail** → Emphasizes product display, customer experience, dynamic lighting
- **Educational** → Emphasizes collaborative spaces, durability, accessibility
- **Industrial** → Downplays residential warmth; emphasizes functional industrial aesthetic
- **Residential** → Full warm_residential focus; emphasizes comfort and livability

The skill adapts room types, material questions, and design character options based on the building type from project-config.json.

### Project Phase Adaptation
- **Schematic Design** → Focus on design intent, no construction details yet
- **Foundation/Sitework** — Emphasize site context, existing conditions, terrain
- **Frame Erection** → Include construction photos, current building progression
- **Finishes** → Deep dive into material finishes, color palette, furniture placement
- **Punch/Closeout** → Document final conditions and lessons learned

Construction status is auto-populated from schedule.json to reflect current phase.

### Multi-Story Adaptation
For buildings with 2+ stories:
- Ask if finishes differ by floor
- Collect separate material/furniture specs for each floor type if needed
- Store in materials_by_room_type with floor identifier (e.g., "Bedroom-L2" vs. "Bedroom-L1")

---

## Tips for Best Results

### For Site Photos:
- **Aerial** — Shows overall site context, topography, adjacent structures
- **Street level approach** — Shows how building appears to visitors/clients
- **Cardinal directions** — One photo from each direction gives rendering engine full context
- **Existing conditions** — If renovation, document current state

### For Design Intent:
- **Be specific with colors** — "warm gray" is better than "gray"; "sage green" better than "green"
- **Reference images** — Upload 3-5 inspiration photos if available for design character
- **Material samples** — If you have physical samples, describe accurately
- **Budget/Premium tiers** — If finishes vary (e.g., "entry is high-end marble, corridors are polished concrete"), specify

### For Best Renderings:
- Run this skill **before** major design decisions are locked
- Allow time to gather reference photos and finishes information
- Update context as design evolves (materials, color palette changes, design character shifts)
- Use renderings in design reviews to validate direction with stakeholders

---

## File Reference

**Reads from:**
- `project-config.json` — project basics, address, building type
- `plans-spatial.json` — room types, areas, dimensions, door schedule
- `specs-quality.json` — finish schedule, material specs
- `schedule.json` — current phase, milestone dates
- `directory.json` — architect, owner contacts

**Writes to:**
- `AI - Project Brain/visual-context.json` — complete visual context output

**References:**
- `/references/visual-context-schema.json` — JSON schema validation

---

## Commands & Quick Reference

```
/site-context              Start visual context interview (new or update existing)
/render                    Generate AI renderings using visual context
/visual-context-view       Display current visual-context.json
/visual-context-export     Export context to PDF or HTML report
```

---

## Troubleshooting

**Q: "I don't have photos. Can I skip this phase?"**
A: Yes. You can skip photo upload and add photos later by re-running `/site-context` → "Update specific section" → "Photos."

**Q: "Can I update just the color palette without re-doing the whole interior section?"**
A: If visual-context.json exists, yes. Run `/site-context` → "Update specific section" → "Interior," then ask to update only color palette.

**Q: "What if I don't know the design character yet?"**
A: The skill provides clear descriptions of each character type. Choose the closest fit. You can always update later.

**Q: "How detailed should material descriptions be?"**
A: Detailed enough to guide visual rendering — e.g., "polished concrete with gray sealer" rather than just "concrete." Include finish, sheen, approximate color.

**Q: "Should I provide room-by-room material specs?"**
A: No. The skill groups by room TYPE (e.g., "Bedroom," "Bathroom," "Corridor"). If a room type varies significantly, note that in special_notes.

---

## Version History

**v1.0.0** — Initial release for Foreman OS v3.0
- 3-phase interview: Exterior → Interior → Photos
- Auto-population from existing project data
- Incremental update support
- Universal design for any building type and project phase
- AI-powered photo analysis
- visual-context.json output for rendering-generator skill
