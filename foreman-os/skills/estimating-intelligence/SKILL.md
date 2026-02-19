---
name: estimating-intelligence
description: >
  Construction estimating knowledge for field superintendents — unit cost structure, assembly-based estimating, CSI MasterFormat cost coding, quantity takeoff methods, productivity rate validation, T&M pricing verification, bid review and leveling, and value engineering analysis. Provides cost awareness for daily decisions, change order pricing review, pay application verification, and budget-to-field reconciliation. Triggers: "estimate", "estimating", "cost", "unit cost", "unit price", "bid", "bid leveling", "takeoff", "quantity", "productivity", "labor rate", "equipment rate", "markup", "overhead", "profit", "CSI", "MasterFormat", "assembly", "waste factor", "T&M", "time and materials", "change order pricing", "value engineering", "VE".
version: 1.0.0
---

# Estimating Intelligence Skill

## Overview

The **estimating-intelligence** skill provides deep estimating knowledge for the field superintendent. This skill does not aim to replace a professional estimator -- it equips the superintendent with a working understanding of cost structure, quantity verification methods, productivity assumptions, and pricing validation so they can make informed daily decisions that protect the project budget.

Construction superintendents operate at the intersection of field execution and project financials. Every decision a superintendent makes -- crew sizing, equipment selection, work sequencing, material ordering, overtime authorization, change order acceptance -- has a direct cost impact. A superintendent who understands how estimates are built can:

- **Verify quantities** on pay applications and change orders rather than accepting them at face value
- **Validate productivity assumptions** against actual field conditions before committing to pricing
- **Identify scope gaps** between the estimate and the work being performed
- **Challenge unreasonable T&M charges** from subcontractors with data-backed pushback
- **Support value engineering** with practical alternatives that maintain quality while reducing cost
- **Code daily reports accurately** so cost tracking reflects reality
- **Anticipate cost overruns** by recognizing when field conditions deviate from estimate assumptions

This skill provides:
- Complete unit cost structure breakdown (labor, material, equipment, overhead, profit, contingency)
- Assembly-based estimating concepts with trade-specific component breakdowns
- CSI MasterFormat division structure with field-relevant cost coding guidance
- Quantity takeoff methods for every measurement type (area, linear, volume, count, weight)
- Comprehensive productivity rate tables by trade with crew compositions
- T&M pricing verification procedures and documentation requirements
- Bid review and leveling methodology for subcontractor selection
- Value engineering framework with common VE items by trade
- Waste factor tables by material category
- Productivity adjustment factors for field conditions

**Key Principle**: The superintendent's role in estimating is not to create estimates -- it is to validate them against field reality. The best estimates are built on assumptions. The superintendent is the person who knows whether those assumptions are correct.

---

## Unit Cost Structure

### The Total Cost Formula

Every line item in a construction estimate follows the same fundamental structure:

```
Total Cost = (Material + Labor Hours x Burdened Rate + Equipment) x (1 + OH%) x (1 + Profit%) + Contingency
```

Understanding each component allows the superintendent to dissect any price and determine whether it is reasonable.

### Labor Burden Breakdown

The "burdened" labor rate is the true cost of an hour of labor -- far more than the base wage. Subcontractors and self-perform crews carry these costs whether or not they appear on the bid breakdown.

**Labor Burden Components:**

| Component | Typical Rate/Percentage | Notes |
|-----------|------------------------|-------|
| Base Wage | Varies by trade/region | Journeyman rate, check prevailing wage if applicable |
| FICA (Social Security + Medicare) | 7.65% of base | Employer's matching portion |
| FUTA (Federal Unemployment) | 0.6% of first $7,000 | Effectively negligible on annualized basis |
| SUTA (State Unemployment) | 2-6% of first $7,000-$40,000 | Varies significantly by state and employer history |
| Workers' Compensation | 3-30% of base | Varies dramatically by trade classification |
| General Liability Insurance | 1-5% of labor cost | Trade-dependent, higher for roofing/structural |
| Health Insurance | $400-$1,200/month per employee | Union plans typically higher |
| Pension/401k | 3-8% of base | Union pension contributions often higher |
| Training/Apprenticeship | 0.5-2% of base | Required in many union agreements |
| Vacation/Holiday Pay | 3-6% of base | Paid time off, union holiday schedules |
| Small Tools/Consumables | 1-3% of base | Hand tools, blades, PPE replacement |

**Workers' Compensation Rates by Trade (Typical Ranges):**

| Trade | WC Rate Range | Classification Code |
|-------|---------------|-------------------|
| General Laborers | 8-15% | 5213 |
| Carpenters | 10-20% | 5403 |
| Ironworkers (structural) | 15-30% | 5040 |
| Electricians | 4-8% | 5190 |
| Plumbers | 5-10% | 5183 |
| Sheet Metal Workers | 6-12% | 5538 |
| Painters | 8-15% | 5474 |
| Roofers | 20-35% | 5551 |
| Equipment Operators | 6-12% | 3724 |
| Concrete Finishers | 10-18% | 5213 |

**Total Burden Multiplier by Trade (Typical):**

| Trade | Base Wage Example | Burden Multiplier | Fully Burdened Rate |
|-------|-------------------|-------------------|---------------------|
| Electrician | $45/hr | 1.40-1.50 | $63-$68/hr |
| Plumber | $48/hr | 1.40-1.50 | $67-$72/hr |
| Carpenter | $40/hr | 1.45-1.55 | $58-$62/hr |
| Laborer | $32/hr | 1.35-1.45 | $43-$46/hr |
| Ironworker | $50/hr | 1.55-1.65 | $78-$83/hr |
| Operator | $48/hr | 1.40-1.50 | $67-$72/hr |
| Sheet Metal | $46/hr | 1.42-1.52 | $65-$70/hr |
| Roofer | $38/hr | 1.55-1.65 | $59-$63/hr |
| Painter | $35/hr | 1.40-1.50 | $49-$53/hr |

**Field Application**: When a subcontractor submits T&M tickets at $95/hr for a journeyman electrician, you can check whether that rate is reasonable. If the base wage in your area is $45/hr and the burden multiplier is 1.45, the burdened rate is ~$65/hr. Add 10% overhead and 10% profit and you get ~$79/hr. The $95/hr rate may include a premium -- or may be inflated.

### Equipment Cost Components

Equipment costs consist of two major categories: ownership costs and operating costs.

**Ownership Costs (Fixed):**
- Depreciation: straight-line or hours-based over useful life
- Interest/cost of capital: financing cost of the asset
- Insurance: comprehensive, liability, physical damage
- Property tax: varies by jurisdiction
- Storage: when not deployed

**Operating Costs (Variable):**
- Fuel: consumption rate x fuel price x hours
- Maintenance and repair: planned PM + unplanned repairs
- Tires/tracks: replacement cost amortized over life
- Operator wages: if operated (included in some rates, not others)

**Ownership vs. Rental Decision Factors:**
- Utilization threshold: if equipment will be used >60-70% of available time, ownership is usually cheaper
- Duration: short-term (<3 months) favors rental; long-term (>6 months) favors ownership
- Maintenance capability: does the contractor have mechanics/shop capability?
- Mobilization: rental companies often include delivery; owned equipment requires transport
- Technology: rapidly changing technology (GPS grade control) may favor rental to avoid obsolescence

**Fuel Consumption by Equipment Class (Approximate):**

| Equipment | Fuel Consumption (gal/hr) | Notes |
|-----------|--------------------------|-------|
| Skid Steer Loader | 2-4 | Light duty |
| Backhoe Loader | 3-5 | Medium duty |
| Excavator (20-ton) | 4-7 | Varies with digging conditions |
| Excavator (35-ton) | 6-10 | Heavy excavation |
| Dozer (D5-D6) | 4-8 | Grade work |
| Dozer (D8-D9) | 8-15 | Heavy pushing |
| Wheel Loader (2-3 CY) | 4-7 | Loading trucks |
| Motor Grader | 4-7 | Fine grading |
| Vibratory Roller | 3-5 | Compaction |
| Concrete Pump (truck-mounted) | 5-8 | During pumping operations |
| Crane (50-100 ton) | 4-8 | Varies with load/swing |
| Crane (200+ ton) | 8-15 | Heavy lifts |
| Aerial Lift (60-80 ft) | 1-3 | Boom/scissor lift |

### Overhead Types

**Job Overhead (General Conditions) -- Typically 8-15% of Direct Cost:**

| Item | Typical Monthly Cost | Notes |
|------|---------------------|-------|
| Superintendent salary | $8,000-$15,000 | Fully burdened |
| Project manager (allocated) | $4,000-$8,000 | Partial allocation typical |
| Field office/trailer | $800-$2,500 | Lease + setup/teardown |
| Temporary utilities | $500-$2,000 | Power, water, phone, internet |
| Temporary facilities | $1,000-$3,000 | Toilets, dumpsters, fencing |
| Project insurance | Varies | Builder's risk, OCIP/CCIP |
| Bonds (P&P) | 1-3% of contract | Performance and payment |
| Small tools | $500-$2,000 | Consumables, replacement |
| Safety equipment | $500-$1,500 | Signs, barricades, PPE supply |
| Clean-up labor | $2,000-$5,000 | Daily/weekly clean-up crew |
| Testing and inspection | $1,000-$4,000 | Third-party testing coordination |
| Surveying and layout | $1,000-$3,000 | Survey crew or subcontractor |
| Winter protection | $2,000-$10,000 | Heating, hoarding (seasonal) |
| Temporary protection | $500-$2,000 | Floor/finish protection |

**Home Office Overhead -- Typically 5-10% of Revenue:**
- Executive salaries and benefits
- Estimating department
- Accounting and payroll
- Human resources
- Office rent and utilities
- Legal and professional services
- Marketing and business development
- IT and software
- Vehicle fleet (non-project)
- Corporate insurance

### Profit and Markup

**Typical Profit Ranges by Project Type:**

| Project Type | Typical Profit Range | Notes |
|-------------|---------------------|-------|
| Competitive hard bid (public) | 3-6% | Low margin, high volume strategy |
| Competitive hard bid (private) | 5-8% | Slightly higher than public |
| Negotiated (CM at-risk) | 8-12% | Pre-construction services add value |
| Design-build | 8-15% | Higher risk = higher reward |
| Specialty/niche work | 10-20% | Limited competition |
| Emergency/fast-track | 15-25% | Premium for acceleration |
| T&M work | 10-15% on labor, 10-15% on material | Per contract terms |

**Market Conditions Impact:**
- Hot market (high demand, low supply of subs): profit margins decrease due to higher sub pricing
- Slow market (low demand, high competition): profit margins decrease due to aggressive bidding
- Ideal conditions: moderate workload with selective bidding allows healthy margins
- Relationship work: repeat clients may accept higher margins for reliability and quality

### Contingency

**Design Contingency by Project Phase:**

| Design Phase | Contingency Range | Rationale |
|-------------|-------------------|-----------|
| Conceptual/programming | 15-25% | High uncertainty, scope undefined |
| Schematic design (30%) | 10-20% | Major systems defined, details unknown |
| Design development (60%) | 7-15% | Details emerging, some coordination gaps |
| Construction documents (90%) | 5-10% | Most details resolved, minor gaps |
| Bid documents (100%) | 3-5% | Final documents, known scope |

**Construction Contingency -- Typically 3-5%:**
- Covers unforeseen field conditions not identified in plans/specs
- NOT a slush fund for scope changes (those are change orders)
- Drawn down through formal approval process
- Common uses: unexpected rock, contaminated soil, hidden conditions in renovation
- Track remaining contingency monthly as percentage of original budget

**Owner Contingency -- Typically 5-10%:**
- Covers owner-initiated changes, market fluctuations, permitting changes
- Managed by owner, not contractor
- Should be separate from contractor contingency
- Reduces as design progresses and scope firms up

---

## Assembly-Based Estimating

### What Assemblies Are

An assembly is a pre-configured bundle that combines all materials, labor, equipment, and incidental items needed to complete one unit of a defined work element. Instead of pricing individual components (one stud, one screw, one piece of track), the estimator prices the entire assembly as a unit (one linear foot of interior partition wall).

Assemblies encode **productivity assumptions** -- the labor hours per unit reflect expected field conditions, crew composition, and work complexity. This is where the estimate meets the field: if the assembly assumes 0.08 labor hours per square foot of drywall hanging, and the field is achieving 0.12 hours (50% slower), the project will overrun labor.

### Assembly Examples by Trade

**Concrete Footing Assembly (per LF of continuous footing, 24" wide x 12" deep):**

| Component | Quantity per LF | Unit | Unit Cost | Extended |
|-----------|----------------|------|-----------|----------|
| Formwork (2x material, ties, oil) | 4 SF | SF | $2.50 | $10.00 |
| Form labor (set and strip) | 0.15 | MH | $58.00 | $8.70 |
| Rebar (#5 @ 12" OC each way) | 3.5 LB | LB | $0.85 | $2.98 |
| Rebar labor (place and tie) | 0.04 | MH | $62.00 | $2.48 |
| Concrete (4000 PSI) | 0.074 | CY | $165.00 | $12.21 |
| Concrete placing labor | 0.03 | MH | $55.00 | $1.65 |
| Pump (amortized) | 0.074 | CY | $15.00 | $1.11 |
| Vibrating/finishing | 0.02 | MH | $55.00 | $1.10 |
| Curing compound | 1.0 | SF | $0.15 | $0.15 |
| **Total Direct Cost per LF** | | | | **$40.38** |

**Metal Stud Interior Partition Assembly (per SF, 3-5/8" studs @ 16" OC, one side GWB, Level 4 finish, painted):**

| Component | Quantity per SF | Unit | Unit Cost | Extended |
|-----------|----------------|------|-----------|----------|
| Floor/ceiling track | 0.25 | LF | $0.65 | $0.16 |
| Metal studs 3-5/8" 25ga | 0.75 | LF | $0.80 | $0.60 |
| Stud labor (layout, cut, install) | 0.018 | MH | $55.00 | $0.99 |
| 5/8" Type X GWB (one side) | 1.05 | SF | $0.55 | $0.58 |
| GWB screws | 0.05 | LB | $2.00 | $0.10 |
| Hanging labor | 0.008 | MH | $52.00 | $0.42 |
| Joint compound | 0.015 | GAL | $12.00 | $0.18 |
| Paper tape | 0.12 | LF | $0.02 | $0.00 |
| Taping labor (Level 4) | 0.012 | MH | $55.00 | $0.66 |
| Primer | 0.012 | GAL | $25.00 | $0.30 |
| Finish paint (2 coats) | 0.016 | GAL | $35.00 | $0.56 |
| Paint labor | 0.010 | MH | $48.00 | $0.48 |
| **Total Direct Cost per SF** | | | | **$5.03** |

**Plumbing Rough-In Assembly (per fixture, lavatory sink):**

| Component | Quantity | Unit | Unit Cost | Extended |
|-----------|----------|------|-----------|----------|
| 1/2" copper supply (H&C) | 12 | LF | $3.50 | $42.00 |
| Supply fittings (elbows, tees) | 6 | EA | $4.50 | $27.00 |
| 1-1/2" DWV pipe | 8 | LF | $5.00 | $40.00 |
| DWV fittings (P-trap, wye, vent) | 4 | EA | $8.00 | $32.00 |
| Hangers and supports | 6 | EA | $3.00 | $18.00 |
| Supply valves (angle stops) | 2 | EA | $12.00 | $24.00 |
| Pipe insulation | 12 | LF | $1.50 | $18.00 |
| Plumber labor (rough-in) | 6.0 | MH | $72.00 | $432.00 |
| Testing (pressure/DWV) | 0.5 | MH | $72.00 | $36.00 |
| **Total Direct Cost per Fixture** | | | | **$669.00** |

**Electrical Circuit Assembly (per 20A branch circuit, 120V, typical office):**

| Component | Quantity | Unit | Unit Cost | Extended |
|-----------|----------|------|-----------|----------|
| 12/2 MC cable | 75 | LF | $1.20 | $90.00 |
| 3/4" EMT conduit (exposed areas) | 15 | LF | $1.80 | $27.00 |
| EMT fittings (connectors, couplings) | 8 | EA | $1.50 | $12.00 |
| 4" square boxes | 4 | EA | $3.50 | $14.00 |
| Device rings/covers | 4 | EA | $1.25 | $5.00 |
| Receptacles (duplex, 20A) | 4 | EA | $4.50 | $18.00 |
| Wire nuts/connectors | 12 | EA | $0.30 | $3.60 |
| Circuit breaker (20A, 1-pole) | 1 | EA | $8.00 | $8.00 |
| Supports/hangers | 8 | EA | $2.00 | $16.00 |
| Electrician labor | 5.0 | MH | $68.00 | $340.00 |
| **Total Direct Cost per Circuit** | | | | **$533.60** |

**Roofing Assembly (per square = 100 SF, 60-mil TPO fully adhered):**

| Component | Quantity | Unit | Unit Cost | Extended |
|-----------|----------|------|-----------|----------|
| TPO membrane (60 mil) | 105 | SF | $1.10 | $115.50 |
| Polyiso insulation (2 layers, R-30) | 105 | SF | $1.80 | $189.00 |
| Cover board (1/2" HD polyiso) | 105 | SF | $0.65 | $68.25 |
| Insulation adhesive | 1 | unit | $35.00 | $35.00 |
| Membrane bonding adhesive | 2 | GAL | $28.00 | $56.00 |
| Termination bar and sealant | 4 | LF | $2.50 | $10.00 |
| Flashing (pre-formed corners, pipe boots) | Allow | | | $25.00 |
| Roofing labor (install) | 3.5 | MH | $58.00 | $203.00 |
| **Total Direct Cost per Square** | | | | **$701.75** |

### How Assemblies Encode Productivity

Every assembly contains embedded productivity assumptions:
- **Labor hours per unit**: the core assumption connecting estimate to field performance
- **Crew composition**: assumed skill mix (journeyman vs. apprentice ratio)
- **Work conditions**: assumed height, access, weather, congestion
- **Sequence**: assumed installation order and method
- **Equipment**: assumed equipment availability (crane, pump, lift)

**When field conditions differ from assembly assumptions, the estimate is wrong.** The superintendent's job is to recognize when actual conditions deviate and flag the impact early.

### Assembly-to-WBS Mapping

Assemblies in the estimate map to Work Breakdown Structure (WBS) elements in the schedule:
- Assembly = the cost of a work element
- WBS activity = the time to complete that work element
- The link: labor hours in the assembly / crew hours per day = activity duration

Example: 500 LF of continuous footing x 0.15 MH/LF forming labor = 75 man-hours. With a 4-person forming crew working 8 hours/day = 32 crew-hours/day. Duration = 75/32 = 2.3 days (round to 3 days with setup/cleanup).

### Assembly Adjustment Factors

| Factor | Adjustment Range | When to Apply |
|--------|-----------------|---------------|
| Location (urban premium) | +5-15% labor | Dense urban, limited staging, traffic |
| Location (rural premium) | +5-10% labor | Travel time, limited labor pool |
| Height above ground | +1-2% per 10 ft above grade | Scaffold/lift time, material handling |
| Weather (hot >95F) | +10-20% labor | Reduced productivity, hydration breaks |
| Weather (cold <32F) | +10-25% labor | Heated enclosures, material protection |
| Congestion/tight spaces | +15-30% labor | Renovation, occupied spaces |
| Overtime (>40 hr/week) | +15-25% per OT hour | Fatigue factor reduces productivity |
| Night/shift work | +10-20% labor | Lighting, coordination, fatigue |
| Learning curve (first units) | +15-25% labor | New crew, unfamiliar work |
| Repetitive work (later units) | -5-15% labor | Crew becomes efficient |

---

## CSI MasterFormat Cost Coding

### Division Structure

The Construction Specifications Institute (CSI) MasterFormat organizes all construction work into 50 divisions (00-49). The cost coding system used in estimates, budgets, cost reports, and pay applications follows this structure.

**Division 00 -- Procurement and Contracting Requirements:**
- Bidding requirements, contract forms, conditions
- Not typically a cost-bearing division in the estimate
- Contains general/supplementary/special conditions

**Division 01 -- General Requirements:**
- Summary of work, price and payment procedures, administrative requirements
- Project management and coordination, construction facilities, temporary controls
- Quality requirements, field engineering, cleaning, closeout
- **Field relevance**: This is where general conditions costs live

**Division 02 -- Existing Conditions:**
- Subsurface investigation, demolition, hazmat remediation
- **Field relevance**: Demolition scope, hazmat procedures, protection of existing work

**Division 03 -- Concrete:**
- Formwork, reinforcement, cast-in-place, precast, cementitious decks, grouting
- **Field relevance**: Major cost driver, superintendent directly manages concrete operations

**Division 04 -- Masonry:**
- Unit masonry (CMU, brick), stone, assemblies
- **Field relevance**: Production rate tracking, mortar consistency, reinforcement/grouting

**Division 05 -- Metals:**
- Structural steel, joists, decking, cold-formed framing, miscellaneous/ornamental metals
- **Field relevance**: Erection sequence, connection inspection, fireproofing coordination

**Division 06 -- Wood, Plastics, and Composites:**
- Rough/finish carpentry, millwork, structural plastics, FRP
- **Field relevance**: Framing inspection, blocking/backing, moisture content

**Division 07 -- Thermal and Moisture Protection:**
- Waterproofing, insulation, shingles, siding, roofing, fireproofing, joint sealants
- **Field relevance**: Weather-dependent work, warranty requirements, inspection holds

**Division 08 -- Openings:**
- Doors/frames, windows, skylights, hardware, glazing
- **Field relevance**: Long-lead procurement, hardware schedules, fire-rated assemblies

**Division 09 -- Finishes:**
- Plaster, gypsum board, tiling, ceilings, flooring, wall coverings, painting
- **Field relevance**: Finish level coordination, moisture testing, visual quality

**Division 10 -- Specialties:**
- Visual display, compartments, lockers, signage, toilet accessories, fire extinguishers
- **Field relevance**: Blocking locations, coordination with finishes

**Division 11 -- Equipment:**
- Commercial/institutional equipment, foodservice, athletic, medical
- **Field relevance**: Utility rough-in coordination, structural support

**Division 12 -- Furnishings:**
- Art, casework, countertops, seating, window treatments
- **Field relevance**: Final phase coordination, protection

**Division 13 -- Special Construction:**
- Swimming pools, aquariums, ice rinks, clean rooms, radiation protection
- **Field relevance**: Specialty subcontractor coordination

**Division 14 -- Conveying Equipment:**
- Elevators, escalators, dumbwaiters, lifts
- **Field relevance**: Shaft dimensions, pit depth, machine room, power requirements

**Divisions 21-28 -- Facility Services (MEP and Fire/Life Safety):**
- **Division 21**: Fire suppression (sprinklers, standpipes)
- **Division 22**: Plumbing (piping, fixtures, equipment)
- **Division 23**: HVAC (ductwork, piping, equipment, controls)
- **Division 25**: Integrated automation (BAS/BMS)
- **Division 26**: Electrical (power distribution, lighting, communications raceways)
- **Division 27**: Communications (data, voice, audio/video)
- **Division 28**: Electronic safety and security (fire alarm, access control, CCTV)
- **Field relevance**: MEP coordination drives critical path, BIM clash detection, above-ceiling coordination

**Divisions 31-35 -- Site and Infrastructure:**
- **Division 31**: Earthwork (clearing, excavation, fill, soil treatment)
- **Division 32**: Exterior improvements (paving, curbs, fencing, landscaping)
- **Division 33**: Utilities (water, sanitary, storm, gas, electrical distribution)
- **Division 34**: Transportation (roads, bridges, rail)
- **Division 35**: Waterway and marine construction
- **Field relevance**: Sitework is first and last -- controls project start and final completion

**Divisions 40-49 -- Process Equipment (Industrial):**
- Process interconnections, integration, instrumentation, pollution control
- **Field relevance**: Industrial/manufacturing projects only

### Cost Code Flow

The cost code system creates a continuous thread from estimate through project closeout:

```
Estimate → Budget → Cost Tracking → Pay Applications → Earned Value → Closeout
  |           |          |                |                  |            |
  CSI code → Budget    → Actual costs  → % complete       → CPI/SPI  → Final
  assigned   line item   charged to      by code            by code     cost
             created     cost code       verified                       analysis
```

### Common Cost Code Structure

Most contractors use a hierarchical structure based on MasterFormat:

```
XX.XX.XX.XXXX
|  |  |  |
|  |  |  +--- Contractor-specific detail (crew, phase, area)
|  |  +------ MasterFormat section (e.g., 30 = Cast-in-Place)
|  +--------- MasterFormat group (e.g., 3 = Concrete)
+------------ Division (e.g., 03 = Concrete)
```

Example: **03.30.53.0100**
- 03 = Concrete division
- 30 = Cast-in-Place Concrete
- 53 = Concrete placement
- 0100 = Contractor detail (e.g., Building A, Level 1)

### Superintendent's Cost Code Responsibilities

1. **Daily Report Coding**: Every labor hour, equipment hour, and material delivery on the daily report should be coded to the correct cost code. Mis-coded entries distort cost tracking and earned value.

2. **T&M Ticket Coding**: When approving T&M tickets, assign the correct cost code so the cost lands in the right budget line item. If a T&M ticket covers work in multiple cost codes, split it.

3. **Change Order Coding**: New cost codes may be needed for change order work. Coordinate with the project manager to establish new codes before work starts.

4. **Pay Application Verification**: When reviewing subcontractor pay applications, verify that the percent complete claimed matches field observation by cost code.

---

## Quantity Takeoff Methods

### Area Takeoff

Used for: flooring, roofing, painting, drywall, waterproofing, insulation, ceiling grid

**Floor Areas:**
- Measure gross building footprint from exterior face of wall to exterior face of wall
- Deduct large openings (stairwells, elevator shafts, atria) for net floor area
- For flooring takeoff, measure net floor area by finish type (tile, carpet, LVT, polished concrete)
- Include closets, alcoves, recesses -- anything that gets the same floor finish

**Wall Areas:**
- Perimeter (LF) x floor-to-floor height = gross wall area
- Deduct openings (doors, windows) for net wall area
- Interior walls: both sides get counted for painting/finishing
- Exterior walls: one side exterior finish, one side interior finish
- Track wall types separately (GWB on stud, CMU, curtain wall)

**Ceiling Areas:**
- Typically equals floor area minus wall thickness area
- Soffits and bulkheads add area
- Vaulted/sloped ceilings: actual surface area > plan area (multiply by slope factor)

**Painting Surfaces:**
- Walls: net wall area (gross minus openings)
- Ceilings: ceiling plan area
- Doors: both faces + edges = ~42 SF per standard 3070 door
- Door frames: ~16 LF per standard frame x width = ~8 SF per frame
- Trim/base: LF x height (typically 4-6" = 0.33-0.5 SF per LF)

### Linear Takeoff

Used for: piping, conduit, curb/gutter, baseboard, crown mold, fencing, handrails, wire

**Measurement Method:**
- Measure centerline length (not inside/outside face)
- Add fitting allowances: typically 2-3 LF per fitting for pipe/conduit
- Add rise and drop: vertical risers, drops from horizontal runs
- Add offset lengths: measure horizontal run + vertical offset using Pythagorean theorem
- Count fittings separately (elbows, tees, couplings, reducers)

**Common Linear Items:**
- Pipe runs: centerline length + fitting allowance + vertical drops
- Conduit: centerline length + fitting allowance + pull boxes
- Curb and gutter: LF along face of curb
- Baseboard/trim: room perimeter minus door openings
- Guard rail/handrail: LF along rail centerline + posts counted separately

### Volumetric Takeoff

Used for: concrete (CY), excavation (CY), fill (CY), grading, aggregate base

**Concrete Volume:**
- Footings: width x depth x length / 27 = CY
- Walls: thickness x height x length / 27 = CY
- Slabs: area x thickness / 27 = CY
- Columns: cross-section area x height / 27 = CY
- Beams: width x depth x length / 27 = CY (deduct slab thickness if monolithic)
- Always calculate in cubic feet first, then divide by 27 to get CY

**Earthwork Volume:**
Critical distinction between Bank Cubic Yards (BCY), Loose Cubic Yards (LCY), and Compacted Cubic Yards (CCY):

| Soil Type | Swell Factor (Bank to Loose) | Shrinkage Factor (Bank to Compacted) |
|-----------|------------------------------|--------------------------------------|
| Sand/Gravel | 10-15% swell | 5-10% shrinkage |
| Common Earth | 20-30% swell | 5-15% shrinkage |
| Clay | 30-40% swell | 10-20% shrinkage |
| Rock (blasted) | 40-65% swell | N/A (no compaction) |
| Topsoil | 15-25% swell | 5-10% shrinkage |

- **Excavation is paid in BCY** (bank measure, before digging)
- **Hauling capacity is in LCY** (loose measure, after digging)
- **Fill is verified in CCY** (compacted measure, after placement)

Conversion: 1 BCY of common earth = 1.25 LCY = 0.90 CCY (typical)

### Count Takeoff

Used for: doors, windows, fixtures, outlets, devices, equipment, specialties

**Method:**
- Use schedule sheets: door schedule, fixture schedule, equipment schedule
- Count by type/size/finish -- each variation is a separate line item
- Cross-reference plans, elevations, and schedules (discrepancies are common)
- Interior elevations often show items not visible on floor plans (wall-mounted items)
- Reflected ceiling plans show light fixtures, sprinkler heads, diffusers, speakers

### Weight Takeoff

Used for: structural steel (tons), rebar (tons)

**Structural Steel:**
- Beams and girders: weight per LF x length (W12x26 = 26 PLF x length)
- Columns: weight per LF x height
- Joists: weight per LF x span (varies by designation)
- Deck: PSF x area (1.5" 20ga deck ~ 2.5 PSF, 3" 20ga deck ~ 3.5 PSF)
- Connections: typically 8-12% of structural member weight
- Miscellaneous steel: stairs, handrails, lintels, embeds -- estimate as percentage or count

**Rebar:**
- Rule of thumb by element:
  - Footings: 50-80 LBS/CY
  - Walls: 80-150 LBS/CY
  - Columns: 150-300 LBS/CY
  - Elevated slabs: 80-120 LBS/CY
  - SOG: 30-60 LBS/CY (depending on reinforcement)
  - Grade beams: 100-200 LBS/CY

### Waste Factor Table

| Material Category | Waste Factor | Rationale |
|-------------------|-------------|-----------|
| Fine materials (tile, flooring) | 5% | Precise cutting, some breakage |
| Irregular cutting (drywall, plywood) | 5-7.5% | Cutoffs at openings, edges |
| Sheet goods (roofing membrane, vapor barrier) | 5-8% | Lap seams, cutting to shape |
| Flexible/site-cut (pipe, conduit) | 5-8% | End cuts, fittings waste |
| Lumber (framing) | 5-10% | End cuts, culls, damage |
| Brick/CMU | 3-5% | Breakage, cutting |
| Bulking materials (earth, aggregate) | 20-30% | Swell factor, spillage, over-excavation |
| Concrete | 3-5% standard forms | Over-pour, spillage |
| Concrete (irregular shapes) | 5-10% | Irregular forms, over-pour |
| Paint | 5-10% | Surface absorption, drips, uneven surfaces |
| Fasteners/connectors | 3-5% | Drops, defects, over-ordering |
| Insulation (batt) | 2-3% | Compression at edges |
| Insulation (rigid board) | 5-8% | Cutting to fit |
| Ceiling grid/tile | 3-5% | Perimeter cuts, breakage |
| Carpet | 5-10% | Pattern matching, seaming |
| Structural steel | 2-3% | Fabrication waste (shop, not field) |

### Takeoff-to-Procurement Connection

Quantities from the takeoff directly feed material procurement:
1. Takeoff quantity + waste factor = order quantity
2. Order quantity verified against submittal/shop drawing quantities
3. Delivery schedule aligned with installation schedule
4. Surplus management: return policy, restocking fees, on-site storage

### Takeoff-to-Pay App Connection

Quantities from the takeoff define the 100% baseline for pay application verification:
1. Schedule of values line item quantity = takeoff quantity
2. Monthly percent complete = installed quantity / total quantity
3. Superintendent verifies installed quantity against field measurement
4. Discrepancies between claimed and measured quantities are flagged before approval

---

## Productivity Rate Tables

### How to Use These Rates

These rates represent **average conditions**: moderate weather, experienced crews, adequate material supply, reasonable access, standard work hours. Actual field productivity will vary based on the adjustment factors listed at the end of this section.

**Rate Format**: Output per crew-day (8 hours) or output per man-hour (MH), with crew composition noted.

### Sitework and Earthwork

| Activity | Equipment/Crew | Output per Day | Unit |
|----------|---------------|----------------|------|
| Clear and grub (light) | D6 dozer + laborer | 1-2 acres | AC |
| Clear and grub (heavy) | D8 dozer + excavator + 2 laborers | 0.5-1 acre | AC |
| Topsoil strip (6") | Scraper or dozer | 400-800 CY | BCY |
| Mass excavation (common earth) | Excavator + 3 trucks | 300-600 CY | BCY |
| Mass excavation (rock) | Excavator + breaker + 2 trucks | 50-150 CY | BCY |
| Trench excavation (4' deep) | Backhoe + laborer | 150-300 LF | LF |
| Fine grading (subgrade) | Motor grader + roller | 3,000-6,000 SF | SF |
| Fill placement and compaction | Dozer + roller + water truck | 200-400 CY | CCY |
| Aggregate base (6") | Dozer + roller | 5,000-10,000 SF | SF |
| Paving (asphalt, 2") | Paver + roller + 3 trucks | 800-1,500 tons | TON |
| Curb and gutter | Slip-form machine + 4-person crew | 300-600 LF | LF |
| Concrete sidewalk (4") | 4-person crew | 400-800 SF | SF |

### Concrete

| Activity | Crew | Output per Day | Unit |
|----------|------|----------------|------|
| Footing formwork (set) | 4-person crew | 200-350 SF | SFCA |
| Footing formwork (strip) | 3-person crew | 400-600 SF | SFCA |
| Wall formwork (set, gang forms) | 4-person crew + crane | 300-500 SF | SFCA |
| Wall formwork (set, handset) | 4-person crew | 150-250 SF | SFCA |
| Slab formwork (elevated, flying forms) | 5-person crew + crane | 2,000-4,000 SF | SF |
| Rebar placement (footings) | 2-person ironworker crew | 1.5-2.5 tons | TON |
| Rebar placement (walls) | 2-person ironworker crew | 1.0-2.0 tons | TON |
| Rebar placement (elevated slab) | 3-person ironworker crew | 2.0-3.5 tons | TON |
| Concrete placement (footings) | 4-person crew, direct chute | 25-35 CY | CY |
| Concrete placement (walls, pump) | 4-person crew + pump | 20-30 CY | CY |
| Concrete placement (SOG, pump) | 5-person crew + pump | 80-150 CY | CY |
| Concrete placement (elevated slab) | 5-person crew + pump | 15-25 CY | CY |
| SOG finishing (broom) | 3-person crew | 2,000-3,000 SF | SF |
| SOG finishing (power trowel) | 3-person crew | 1,500-2,500 SF | SF |

### Structural Steel

| Activity | Crew | Output per Day | Unit |
|----------|------|----------------|------|
| Erection (beams/columns, bolted) | 4-person ironworker crew + crane | 8-15 pieces | EA |
| Erection (heavy sections >50 PLF) | 4-person crew + crane | 5-10 pieces | EA |
| Steel deck installation | 3-person crew | 2,000-4,000 SF | SF |
| Steel joist installation | 4-person crew + crane | 20-40 joists | EA |
| High-strength bolting | 2-person crew | 80-150 bolts | EA |
| Field welding (structural) | 1 welder | 15-30 LF | LF |
| Fireproofing (spray-applied) | 3-person crew | 3,000-6,000 SF | SF |
| Touch-up painting | 1 painter | 800-1,500 SF | SF |

### Masonry

| Activity | Crew | Output per Day | Unit |
|----------|------|----------------|------|
| CMU 8" standard (running bond) | Mason + laborer | 150-200 blocks | EA |
| CMU 8" (stack bond, reinforced) | Mason + laborer | 100-150 blocks | EA |
| CMU 12" (reinforced, grouted) | Mason + laborer | 80-120 blocks | EA |
| Brick veneer (running bond) | Mason + laborer | 300-450 bricks | EA |
| Brick veneer (pattern bond) | Mason + laborer | 200-350 bricks | EA |
| Stone veneer (natural) | Mason + laborer | 30-60 SF | SF |
| Grout fill (CMU cells) | Laborer + pump | 2-4 CY | CY |
| Masonry reinforcement | Laborer | 200-400 LF | LF |

### Wood Framing

| Activity | Crew | Output per Day | Unit |
|----------|------|----------------|------|
| Wall framing (exterior, 2x6) | 2-person crew | 200-350 SF | SF |
| Wall framing (interior, 2x4) | 2-person crew | 250-400 SF | SF |
| Floor framing (2x10 joists, 16" OC) | 2-person crew | 300-500 SF | SF |
| Roof framing (rafters, simple) | 2-person crew | 200-400 SF | SF |
| Roof trusses (set with crane) | 3-person crew + crane | 25-45 trusses | EA |
| Sheathing (wall, 1/2" plywood) | 2-person crew | 800-1,200 SF | SF |
| Sheathing (roof, 5/8" plywood) | 2-person crew | 600-1,000 SF | SF |
| Blocking/backing | 1 carpenter | 80-150 LF | LF |

### Metal Framing and Drywall

| Activity | Crew | Output per Day | Unit |
|----------|------|----------------|------|
| Metal stud framing (3-5/8", 16" OC) | 2-person crew | 300-500 SF | SF |
| Metal stud framing (6", 16" OC) | 2-person crew | 250-400 SF | SF |
| Metal stud framing (complex/curved) | 2-person crew | 100-200 SF | SF |
| Drywall hanging (1/2" standard) | 2-person crew | 1,800-2,800 SF | SF |
| Drywall hanging (5/8" Type X) | 2-person crew | 1,500-2,500 SF | SF |
| Drywall hanging (ceilings) | 2-person crew | 1,000-1,800 SF | SF |
| Drywall hanging (double layer) | 2-person crew | 1,200-1,800 SF | SF |
| Taping (Level 3) | 1 taper | 1,000-1,500 SF | SF |
| Taping (Level 4) | 1 taper | 800-1,200 SF | SF |
| Taping (Level 5) | 1 taper | 600-900 SF | SF |

### Roofing

| Activity | Crew | Output per Day | Unit |
|----------|------|----------------|------|
| TPO/PVC single-ply (mechanically attached) | 4-person crew | 12-18 squares | SQ |
| TPO/PVC single-ply (fully adhered) | 4-person crew | 10-15 squares | SQ |
| EPDM (ballasted) | 4-person crew | 15-22 squares | SQ |
| EPDM (fully adhered) | 4-person crew | 10-15 squares | SQ |
| Built-up roofing (3-ply) | 5-person crew | 8-12 squares | SQ |
| Modified bitumen (torch-applied) | 3-person crew | 10-15 squares | SQ |
| Standing seam metal | 3-person crew | 6-10 squares | SQ |
| Asphalt shingles | 3-person crew | 15-25 squares | SQ |
| Roof insulation (rigid board) | 3-person crew | 3,000-5,000 SF | SF |
| Flashing (base/counter) | 2-person crew | 80-150 LF | LF |

### MEP Rough-In

**Mechanical (HVAC):**

| Activity | Crew | Output per Day | Unit |
|----------|------|----------------|------|
| Rectangular ductwork (medium) | 2 sheet metal workers | 50-100 LF | LF |
| Round/spiral duct | 2 sheet metal workers | 80-150 LF | LF |
| Flex duct connections | 1 sheet metal worker | 20-35 connections | EA |
| Diffusers/grilles (install) | 1 sheet metal worker | 15-25 units | EA |
| VAV box installation | 2 workers | 4-8 units | EA |
| RTU setting (with crane) | 4-person crew + crane | 1-3 units | EA |
| Chilled water piping (4") | 2 pipefitters | 30-50 LF | LF |
| Refrigerant piping | 1 pipefitter | 40-70 LF | LF |
| Pipe insulation | 1 insulator | 80-150 LF | LF |

**Electrical:**

| Activity | Crew | Output per Day | Unit |
|----------|------|----------------|------|
| EMT conduit (3/4") | 1 electrician | 80-120 LF | LF |
| EMT conduit (2") | 1 electrician | 40-70 LF | LF |
| Rigid conduit (2") | 1 electrician | 25-40 LF | LF |
| MC cable (12/2) | 1 electrician | 200-350 LF | LF |
| Wire pulling (3 #12 in 3/4" EMT) | 2 electricians | 500-800 LF | LF |
| Receptacle installation | 1 electrician | 10-15 devices | EA |
| Switch installation | 1 electrician | 12-18 devices | EA |
| Light fixture (2x4 troffer) | 1 electrician | 10-15 fixtures | EA |
| Light fixture (recessed can) | 1 electrician | 15-25 fixtures | EA |
| Panel installation and termination | 2 electricians | 1-2 panels | EA |
| Motor connection | 1 electrician | 3-5 connections | EA |

**Plumbing:**

| Activity | Crew | Output per Day | Unit |
|----------|------|----------------|------|
| Copper pipe (1/2"-1") | 1 plumber | 40-70 LF | LF |
| Copper pipe (2"-4") | 1 plumber | 20-40 LF | LF |
| PVC DWV (2"-4") | 1 plumber | 50-80 LF | LF |
| Cast iron (hub, 4") | 1 plumber | 25-40 LF | LF |
| PEX tubing (1/2"-1") | 1 plumber | 80-150 LF | LF |
| Fixture rough-in (lav) | 1 plumber | 3-5 fixtures | EA |
| Fixture rough-in (toilet) | 1 plumber | 4-6 fixtures | EA |
| Fixture setting (trim-out) | 1 plumber | 4-6 fixtures | EA |
| Water heater installation | 2 plumbers | 1-2 units | EA |

**Fire Protection:**

| Activity | Crew | Output per Day | Unit |
|----------|------|----------------|------|
| Sprinkler main (4" black steel) | 2 fitters | 50-80 LF | LF |
| Sprinkler branch (1"-1.5") | 1 fitter | 100-180 LF | LF |
| Sprinkler head installation | 1 fitter | 25-45 heads | EA |
| Standpipe riser (4") | 2 fitters | 20-40 LF | LF |
| Fire department connection | 2 fitters | 1-2 connections | EA |
| Hydrostatic testing | 2 fitters | 1 zone/day | ZONE |

### Finishing Trades

| Activity | Crew | Output per Day | Unit |
|----------|------|----------------|------|
| Interior painting (walls, 2 coats) | 1 painter | 400-700 SF | SF |
| Interior painting (ceilings, 2 coats) | 1 painter | 300-500 SF | SF |
| Interior painting (doors, both sides) | 1 painter | 8-12 doors | EA |
| Trim painting (base, casing) | 1 painter | 200-400 LF | LF |
| Ceramic tile (floor, 12x12) | 1 tile setter + helper | 80-150 SF | SF |
| Ceramic tile (wall, subway) | 1 tile setter + helper | 50-100 SF | SF |
| LVT/LVP flooring (click) | 2-person crew | 400-700 SF | SF |
| Carpet tile | 2-person crew | 600-1,000 SF | SF |
| Sheet vinyl | 2-person crew | 300-500 SF | SF |
| ACT ceiling (2x4 grid + tile) | 2-person crew | 400-700 SF | SF |
| Casework installation | 2 carpenters | 20-40 LF | LF |
| Countertop (solid surface) | 2 installers | 30-50 LF | LF |

### Productivity Adjustment Factors

| Factor | Multiplier | Application |
|--------|-----------|-------------|
| **Weather - Hot (>95F)** | 0.80-0.90 | Reduce output 10-20% |
| **Weather - Cold (<32F)** | 0.75-0.90 | Reduce output 10-25% |
| **Weather - Rain (light)** | 0.85-0.95 | Reduce output 5-15% (exterior only) |
| **Weather - Rain (heavy)** | 0.00-0.50 | Many activities stop or severely impacted |
| **Height 10-20 ft** | 0.95 | Minor impact from scaffold/lift |
| **Height 20-40 ft** | 0.85-0.90 | Moderate impact, material handling |
| **Height >40 ft** | 0.75-0.85 | Significant impact, safety considerations |
| **Overtime (>40-50 hr/wk)** | 0.85-0.95 | Fatigue reduces per-hour productivity |
| **Overtime (>50-60 hr/wk)** | 0.75-0.85 | Significant fatigue factor |
| **Overtime (>60 hr/wk sustained)** | 0.65-0.75 | Severe productivity loss, safety risk |
| **Congested area** | 0.70-0.85 | Trade stacking, limited access |
| **Occupied/operational building** | 0.75-0.85 | Restrictions, protection, limited hours |
| **Night shift** | 0.85-0.95 | Lighting, coordination challenges |
| **Learning curve (first 20%)** | 0.75-0.85 | Crew learning new work type |
| **Repetitive (after 80%)** | 1.05-1.15 | Crew efficient, familiar with work |
| **Excellent supervision** | 1.05-1.10 | Good planning, material staging |
| **Poor supervision** | 0.80-0.90 | Re-work, waiting, inefficiency |

---

## T&M Pricing Verification

### Three Change Order Pricing Methods

| Method | When Used | Superintendent's Role |
|--------|-----------|----------------------|
| **Unit Price** | Pre-agreed rates for defined scope | Verify quantities only |
| **T&M (Time and Materials)** | Undefined scope, emergency work | Verify all costs daily |
| **Lump Sum (Estimate-Based)** | Defined scope, negotiated price | Review estimate for reasonableness |

### When Each Method Applies

**Unit Price:**
- Work is well-defined but quantity is uncertain
- Pre-established unit prices in the contract
- Examples: additional excavation (per CY), additional outlets (per EA), extra concrete (per CY)
- Superintendent's job: accurate quantity measurement and documentation

**T&M:**
- Scope cannot be defined in advance
- Emergency or urgent work
- Investigation/exploratory work
- When parties cannot agree on a lump sum
- Examples: unforeseen conditions, emergency repairs, design investigation
- Superintendent's job: daily verification of all labor, material, and equipment charges

**Lump Sum:**
- Scope is defined, price is negotiated
- Most common method for standard change orders
- Subcontractor or GC prepares a detailed estimate
- Superintendent's job: review estimate assumptions against field conditions

### T&M Documentation Requirements

**Daily Timesheets (Required for Every T&M Day):**
- Full names and classifications of all workers
- Hours worked (start time, end time, break deductions)
- Description of work performed (specific, not generic)
- Location/area of work
- Superintendent signature and date
- Subcontractor foreman signature and date

**Material Receipts:**
- Delivery tickets with material descriptions and quantities
- Invoices or pricing backup
- Verification that materials were actually used on T&M work (not stockpiled)
- Return credits for unused materials

**Equipment Logs:**
- Equipment type and size
- Hours operated (distinguish active vs. standby)
- Operator identified (if operator cost is separate)
- Mobilization/demobilization documented if applicable

### Rate Verification

**Labor Rate Verification Checklist:**
1. Compare submitted rate to contract-specified T&M rates
2. If no contract rates, compare to prevailing wage + burden + OH + profit
3. Verify worker classifications match work performed (journeyman vs. apprentice)
4. Check for unauthorized overtime premiums
5. Verify crew size is appropriate for the work (no "featherbedding")

**Material Markup Verification:**
- Typical markup: 10-15% on material cost
- Verify against contract terms (some contracts cap material markup)
- Require actual invoices, not list prices
- Check for bulk discounts that should be passed through
- Sales tax: verify rate is correct for jurisdiction

**Equipment Rate Verification:**
- Compare to published rates (Blue Book, rental house quotes)
- Verify hours are reasonable for work performed
- Check for standby time: is it authorized? At what rate?
- Mobilization/demobilization: one-time charge, verify distance
- Fuel: some rates include fuel, others charge separately -- verify against contract

### Markup Stacking

How markups compound (this is where disputes frequently arise):

```
Direct Cost:                    $10,000
+ Subcontractor OH (10%):       $1,000
+ Subcontractor Profit (10%):   $1,000
= Sub Total:                   $12,000
+ GC Markup on Sub (10%):       $1,200  ← Is this on $10,000 or $12,000?
= Total:                       $13,200
```

**Key Contract Language to Check:**
- "Markup on cost" = markup on direct cost only ($10,000)
- "Markup on amount" = markup on total sub amount ($12,000)
- "No markup on markup" = GC markup on sub's direct cost only
- Some contracts limit total markup to a fixed percentage (e.g., 15% total)

### T&M Daily Ticket Process

1. **Before Work Starts**: Get verbal or written authorization for T&M work
2. **During Work**: Monitor crew size, hours, materials, equipment
3. **End of Day**: Review and sign daily T&M ticket with subcontractor
4. **Critical Rule**: **Never sign a blank ticket.** Never sign a ticket you have not reviewed. Never back-date signatures. If you disagree with a line item, note your objection on the ticket and sign with qualifications.
5. **End of Week**: Reconcile daily tickets with weekly summary
6. **When Complete**: Compile all tickets, receipts, and logs for change order pricing

### Common T&M Disputes and Prevention

| Dispute | Prevention |
|---------|-----------|
| Worker classification (paying journeyman rate for apprentice) | Verify certifications at start |
| Crew size (too many workers for the task) | Monitor daily, challenge immediately |
| Hours (inflated time) | Sign tickets daily, note actual observed hours |
| Material quantity (over-ordering, stockpiling) | Track deliveries vs. installed quantities |
| Equipment standby (charging for idle equipment) | Document standby authorization, minimize standby |
| Scope creep (T&M expanding beyond authorized work) | Clear scope definition at authorization |
| Rate escalation (applying higher rates than contracted) | Reference contract rate schedule on every ticket |

---

## Bid Review and Leveling

### Scope Comparison Matrix

The most important tool in bid analysis is the scope comparison matrix -- a line-by-line comparison of what each bidder includes and excludes.

**Creating the Matrix:**

1. **List all scope items** from the specification section for the trade being bid
2. **Add common work items** that may not be explicitly specified (cleanup, protection, hoisting, layout)
3. **Review each bid** for explicit inclusions, explicit exclusions, and qualifications
4. **Mark each cell**: Included (I), Excluded (E), Qualified (Q), Not Addressed (N/A)
5. **Price excluded items separately** so you can make an apples-to-apples comparison

**Example Scope Matrix (Mechanical HVAC):**

| Scope Item | Bidder A | Bidder B | Bidder C |
|-----------|----------|----------|----------|
| Ductwork fabrication and install | I | I | I |
| Ductwork insulation | I | E | I |
| Piping (CHW/HHW) | I | I | Q - 4" and below only |
| Piping insulation | I | I | E |
| Equipment setting | I | I | I |
| Controls/BAS | I | E | I |
| Testing and balancing | I | I | E |
| Start-up and commissioning | I | Q - start-up only | E |
| Permits and fees | E | E | I |
| Hoisting | E | I | E |
| Protection of work | I | I | I |
| Clean-up | I | I | Q - rough only |

### Identifying Scope Gaps

**Red Flags in Bids:**
- "By others" or "NIC" (not in contract) statements
- Qualification letters longer than one page
- Substitution requests that change performance
- Schedule qualifications ("based on uninterrupted access")
- Payment terms that differ from contract ("paid when paid" vs. "30 days")
- Allowances embedded in the price
- Exclusions buried in the fine print

### Unit Price Reasonableness Check

**Comparing Unit Prices Across Bidders:**
- Calculate unit prices for major scope items (total price / quantity)
- Flag any unit price that deviates >20% from the average of all bidders
- Low outliers may indicate: scope gap, error, or "buy-in" pricing (intentionally low to win, then make profit on change orders)
- High outliers may indicate: conservative pricing, misunderstanding of scope, or overhead burden

**Benchmark Ranges (Order of Magnitude -- Verify Against Local Market):**

| Trade | Unit | Typical Range |
|-------|------|---------------|
| Concrete (CIP, all-in) | CY | $400-$900 |
| Structural steel (erected) | TON | $3,500-$6,500 |
| CMU wall (8", reinforced, grouted) | SF | $12-$22 |
| Metal stud + GWB (both sides, Level 4, painted) | SF | $8-$16 |
| ACT ceiling (2x4 grid + tile) | SF | $3-$7 |
| Ceramic floor tile (standard) | SF | $8-$18 |
| TPO roofing (60 mil, complete) | SQ | $600-$1,000 |
| HVAC (office, per ton) | TON | $3,000-$6,000 |
| Electrical (office, per SF) | SF | $12-$25 |
| Plumbing (office, per fixture) | FIX | $2,500-$5,000 |
| Fire sprinkler (light hazard) | HEAD | $200-$400 |
| Painting (interior, 2 coats, walls) | SF | $1.50-$3.00 |

### Pre-Qualification Criteria

**Financial Capacity:**
- Annual revenue should be >3x the contract value
- Net worth should be >50% of the contract value (projects >50% of net worth = elevated risk)
- Verify with audited financial statements (last 2-3 years)
- Check for liens, judgments, or bankruptcy history

**Bonding Capacity:**
- Aggregate bonding capacity should exceed current backlog + this project
- Single project bonding limit should exceed this contract value
- Bonding company rating: A.M. Best rating of A- or better preferred

**Safety Record:**
- EMR (Experience Modification Rate): <1.0 preferred, >1.5 = serious concern
- OSHA recordable rate: compare to industry average
- Fatalities in last 5 years: investigate thoroughly
- OSHA citations: check OSHA.gov for recent citations
- Safety program documentation: written safety plan, toolbox talks, training records

**Experience and References:**
- Minimum 3 comparable projects in last 5 years
- References checked with owner AND GC on each reference project
- Key personnel: who will be the foreman/superintendent? Verify their experience
- Geographic familiarity: have they worked in this area? Understand local conditions?

**Backlog Analysis:**
- Current committed work vs. capacity
- Can they staff this project adequately while maintaining other commitments?
- What percentage of their workforce would this project require?

### Best Value Selection

Moving beyond lowest price to select the best overall value:

**Weighted Evaluation Criteria (Example):**

| Criterion | Weight | Scoring Basis |
|-----------|--------|---------------|
| Price | 40% | Lowest = 100, others prorated |
| Relevant experience | 20% | Project portfolio, reference checks |
| Key personnel qualifications | 15% | Resumes, interview |
| Safety record | 10% | EMR, OSHA record, safety plan |
| Schedule capability | 10% | Realistic schedule, resource plan |
| Financial strength | 5% | Financial statements, bonding |
| **Total** | **100%** | |

### Bid Tabulation Format

Standard bid tab columns:
1. Bidder name
2. Base bid amount
3. Alternates (Add/Deduct for each)
4. Unit prices (for each specified unit price item)
5. Qualifications/exclusions summary
6. Bond included (Y/N)
7. Addenda acknowledged
8. Bid validity period
9. Adjusted total (base + selected alternates + scope gap pricing)
10. Rank

---

## Value Engineering

### Common VE Items by Trade

**Foundations:**
- Reduce footing depth where geotechnical report allows shallower bearing
- Eliminate over-designed footings (often designed for worst-case, not actual loads)
- Substitute driven piles for drilled piers (or vice versa, depending on soil)
- Use ground improvement (stone columns, rammed aggregate piers) vs. deep foundations
- Reduce slab thickness where structural loads allow
- Typical savings: 5-15% of foundation cost

**Structure:**
- Steel vs. concrete: evaluate for each project (steel faster, concrete may be cheaper in some markets)
- Pre-cast vs. cast-in-place: pre-cast faster, better quality control, higher material cost
- Composite deck vs. concrete pan joist: composite typically cheaper for office/commercial
- Post-tensioned slabs vs. mild steel reinforcement: PT allows thinner slabs, less concrete
- Optimize column grid spacing: larger bays = fewer columns = less formwork, but heavier beams
- Typical savings: 5-20% of structural cost

**Building Enclosure:**
- Curtain wall vs. storefront system: storefront 30-50% less than curtain wall
- EIFS vs. brick veneer: EIFS 40-60% less than brick, but durability/maintenance concerns
- Precast panels vs. masonry: precast faster installation, comparable or lower cost at scale
- Vinyl windows vs. aluminum: vinyl 30-50% less, limited to certain project types
- Modified bitumen vs. TPO: TPO typically 10-20% less with comparable performance
- Typical savings: 10-30% of enclosure cost

**MEP Systems:**
- VRF vs. chilled water: VRF lower installed cost for small/medium buildings (<80,000 SF)
- PEX vs. copper: PEX 30-50% less material and labor cost for domestic water
- LED vs. fluorescent: LED lower energy cost, often comparable installed cost now
- Sensor-based controls vs. time-clock: higher first cost, significant energy savings
- Condensing boilers vs. standard: 10-15% more, but 15-30% energy savings
- 2-pipe vs. 4-pipe fan coil: 2-pipe less piping, but no simultaneous heating/cooling
- Typical savings: 10-25% of MEP cost

**Finishes:**
- LVT vs. ceramic tile: LVT 30-50% less installed, good durability for commercial
- Painted CMU vs. GWB on stud: painted CMU less in industrial/back-of-house areas
- Standard vs. custom: standard fixtures, doors, hardware 20-40% less than custom
- Stained concrete vs. applied flooring: stained concrete 50-70% less, limited aesthetics
- ACT ceiling vs. GWB ceiling: ACT 30-50% less, easier access for above-ceiling work
- Typical savings: 15-35% of finish cost

### VE Proposal Format

Every VE proposal should contain:

1. **Description**: What is being changed and why
2. **Cost Impact**: Detailed cost comparison (original design vs. VE alternative)
3. **Schedule Impact**: Will this accelerate, delay, or be neutral to the schedule?
4. **Quality/Performance Impact**: Does the alternative meet the design intent? Any compromise?
5. **Code Compliance**: Does the alternative comply with all applicable codes?
6. **Maintenance Impact**: Long-term O&M cost comparison
7. **Warranty Impact**: Does the alternative change warranty terms?
8. **Risk Assessment**: What risks does the alternative introduce?

### Cost-Benefit Analysis Framework

For each VE item, calculate:
- **First Cost Savings**: One-time construction cost reduction
- **Life Cycle Cost Impact**: 20-30 year maintenance, energy, replacement cost comparison
- **Net Present Value**: Discount future costs to present value for true comparison
- **Payback Period**: If VE item has higher first cost but lower operating cost, how long to recoup?

### VE Timing

| Project Phase | VE Effectiveness | Notes |
|---------------|-----------------|-------|
| Programming/Conceptual | Highest | Can change systems, materials, configuration |
| Schematic Design | High | System selections still flexible |
| Design Development | Moderate | Major systems fixed, detail alternatives possible |
| Construction Documents | Low | Changes require redesign, coordination rework |
| Bidding | Very Low | Limited to material substitutions |
| Construction | Minimal | Changes are change orders, not VE |
| Post-Construction | None | Too late for construction cost savings |

**The 1-10-100 Rule**: A change that costs $1 in programming costs $10 in design and $100 in construction. VE is most effective when applied early.

---

## Integration with Other ForemanOS Skills

### change-order-tracker
- **T&M Verification**: Use estimating-intelligence productivity rates and unit costs to verify T&M ticket reasonableness
- **CO Pricing Review**: Compare change order pricing to assembly costs and productivity assumptions
- **Markup Verification**: Validate markup percentages against contract terms
- **Scope Gap Identification**: Use scope comparison techniques to identify items missing from change order pricing

### cost-tracking
- **Forecast Validation**: Compare actual unit costs to estimated unit costs for early warning of overruns
- **Earned Value**: Use productivity rates to validate percent complete claims
- **Cost Code Accuracy**: Ensure field coding matches estimate cost code structure
- **Budget-to-Actual Reconciliation**: Trace variances back to specific estimate assumptions (labor rate, productivity, material price)

### labor-tracking
- **Productivity Comparison**: Compare actual labor hours per unit to estimated productivity rates
- **Crew Efficiency**: Validate crew sizes against assembly assumptions
- **Overtime Impact**: Track productivity degradation from overtime against adjustment factors
- **Trade-Specific Analysis**: Use trade productivity tables as benchmarks for field performance

### pay-application
- **Quantity Verification**: Use takeoff methods to independently verify claimed quantities
- **Percent Complete Validation**: Cross-reference claimed progress with actual field measurement
- **Unit Price Checking**: Compare pay app unit prices to estimate and bid tab unit prices
- **Stored Material Verification**: Validate stored material quantities and pricing

### document-intelligence
- **Specification Cross-Reference**: Link CSI cost codes to specification sections for scope verification
- **RFI Cost Impact**: Estimate cost impact of RFI responses using assembly pricing
- **Submittal Review**: Verify submitted products match estimate assumptions (substitutions may change cost)

### quantitative-intelligence
- **Assembly Chain Verification**: Validate that quantity chains (takeoff → order → install → pay) are consistent
- **Waste Factor Tracking**: Compare actual waste to estimated waste factors
- **Production Rate Trending**: Use quantitative data to refine productivity rate assumptions

---

## Quick Reference

### Estimating Red Flags for the Superintendent

1. **Productivity assumptions that don't match field conditions** -- the estimate assumes ideal conditions, the field has restrictions
2. **Missing scope items** -- work required by the drawings that is not in any subcontractor's scope
3. **Unrealistic crew sizes** -- estimate assumes larger crews than available or practical
4. **No contingency** -- or contingency already spent early in the project
5. **Equipment rates above market** -- T&M equipment charges that exceed rental house quotes
6. **Markup on markup** -- GC charging markup on sub's marked-up price when contract prohibits it
7. **Waste factors too low** -- 0% waste assumption means the first cutoff is an overrun
8. **Escalation not included** -- on long-duration projects, material prices will increase
9. **Unit prices that are too low** -- invitation for change order claims later
10. **Schedule assumptions embedded in pricing** -- "price valid for 60 days" or "based on normal working hours"

### Cost Verification Checklist (For Any Price Submission)

- [ ] Labor rates match contract or market rates
- [ ] Productivity assumptions are reasonable for field conditions
- [ ] Material prices verified against current market (get independent quotes if >$25K)
- [ ] Equipment rates match Blue Book or rental quotes
- [ ] Overhead percentage within contract parameters
- [ ] Profit percentage within contract parameters
- [ ] Markup stacking follows contract terms
- [ ] Quantities verified against takeoff (independent measurement)
- [ ] Waste factors are reasonable
- [ ] Sales tax is correct rate
- [ ] Bond cost included only if required
- [ ] No duplicate charges (item in base scope AND change order)
- [ ] Escalation is reasonable for project timeline
- [ ] Contingency is justified and appropriate