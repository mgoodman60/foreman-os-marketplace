---
name: claims-documentation
description: >
  Build defensible construction claim records through contemporaneous documentation, formal notice tracking, and claims package assembly. Covers delay claims, cost claims, change order disputes, back-charges, acceleration claims, lost productivity, Eichleay home office overhead, and measured mile analysis. Integrates with daily reports, delay tracker, contract administration, and cost tracking for complete claims support. Triggers: "claim", "claims", "dispute", "notice", "damages", "delay claim", "cost claim", "change order dispute", "back-charge", "Eichleay", "home office overhead", "lost productivity", "acceleration claim", "claims package".
version: 1.0.0
---

# Claims Documentation Skill

## Overview

The **claims-documentation** skill provides construction superintendents and project managers with a systematic framework for building defensible claim records through contemporaneous documentation. The difference between winning and losing a construction claim is almost always documentation quality. Merits matter, but without proper records, even the strongest claim fails.

This skill ensures field teams create claims-grade records from day one -- not after a dispute arises. Retroactive documentation is always weaker than contemporaneous evidence. Courts, arbitrators, and mediators consistently give greater weight to records created at or near the time of the event than to after-the-fact reconstructions, no matter how detailed.

**Core principle**: Document everything as if you will need it in a dispute, even when the project is going smoothly. The cost of over-documenting is trivial compared to the cost of an unsupported claim or an indefensible position.

**What this skill covers**:
- Contemporaneous record standards and admissibility requirements
- Daily report requirements specifically for claims support
- Photo and video documentation standards with chain of custody
- Schedule impact documentation and Time Impact Analysis (TIA)
- Cost impact documentation including measured mile, Eichleay, and acceleration costs
- Causation evidence and the Event-Impact-Damages chain
- Notice requirements and contractual deadlines (the single most important procedural element)
- Concurrent delay identification and allocation
- Claims package assembly for formal submission
- Mediation and arbitration preparation
- Claims-specific data models and JSON schemas
- Integration with delay-tracker, contract-administration, cost-tracking, and other ForemanOS skills

---

## Contemporaneous Record Standards

### What Qualifies as Admissible Evidence in Construction Disputes

**Contemporaneous** = created at or near the time of the event. This is the gold standard for construction claims evidence. Courts and arbitrators heavily favor contemporaneous records over after-the-fact reconstruction because they are less susceptible to bias, faulty memory, and self-serving revision.

### Hierarchy of Evidence Quality

#### Tier 1: Strongest Evidence (Created Same Day)
- **Daily reports** completed and signed on the day of observation
- **Photographs** with original EXIF metadata (GPS coordinates, timestamp)
- **Emails** sent on the day of the event with original headers
- **Inspection reports** signed by inspector on date of inspection
- **Electronic logs** with system-generated timestamps (badge-in/out, GPS trackers, equipment telematics)
- **Weather station data** from on-site instruments or nearest NOAA station
- **Video footage** with embedded date/time overlay

#### Tier 2: Strong Evidence (Created Within 24-48 Hours)
- **Meeting minutes** distributed within one business day of the meeting
- **Handwritten field notes** with date, time, and author identification
- **RFI submissions** documenting conditions observed in the field
- **Delivery tickets** and material receiving documents
- **Time sheets** completed by end of shift or next morning

#### Tier 3: Acceptable Evidence (Created Within One Week)
- **Weekly reports** summarizing daily observations
- **Progress photographs** from regular weekly walkthroughs
- **Schedule updates** reflecting actual progress
- **Cost reports** compiled from daily records

#### Tier 4: Weak Evidence (Created After the Fact)
- **Reconstructed daily reports** written weeks or months later
- **Recollections** documented after a dispute has arisen
- **Undated photographs** without metadata
- **Oral testimony** without supporting documentation
- **Summaries** prepared specifically for the claim

### Record Integrity Requirements

1. **Date and time**: Every record must have a clear date of creation. Electronic records should preserve metadata timestamps. Handwritten notes must include date written.
2. **Author identification**: Who created the record? Name and role of the author must be clear.
3. **Original format preservation**: Keep original files. Do not edit, crop, or modify photographs. Do not alter email chains. Print-to-PDF preserves email formatting and headers.
4. **Chain of custody**: Who has had access to the record? For photographs and electronic files, maintain a log showing: original creation, transfers, storage locations.
5. **Consistency**: Records that contradict each other weaken the claim. Daily reports, photos, and correspondence should tell a consistent story.
6. **Specificity**: Vague records are nearly useless. "Weather delayed work" is weak. "Ambient temperature 28F at 7:00 AM prevented concrete placement per ACI 306 (40F minimum); crew of 6 from ABC Concrete stood down; notified PM at 7:15 AM" is strong.

### Electronic Record Considerations

- **Email**: Preserve full headers (sender, recipient, date, time, subject). Do not forward-only; keep original chain intact.
- **Text messages**: Screenshot with visible phone number and timestamp. Export to PDF for permanent record.
- **Project management software**: Export logs with timestamps. Screenshots showing status changes and dates.
- **BIM/model changes**: Document revision dates and who made changes.
- **GPS/telematics**: Equipment location and operating hours data from fleet management systems.

---

## Daily Report Requirements for Claims Support

Beyond standard daily reporting, claims-grade daily reports must capture significantly more detail than a typical field log. Every superintendent should write daily reports as if they will be read aloud in a deposition or arbitration hearing.

### Required Fields for Claims-Grade Daily Reports

#### 1. Labor Documentation
- **Exact headcount by trade**: Not just "plumbers on site" but "4 plumbers from XYZ Mechanical: J. Smith, R. Jones, M. Davis, T. Williams"
- **Start and stop times by trade**: "Electricians arrived 7:00 AM, departed 3:30 PM (8 hrs); Plumbers arrived 6:30 AM, departed 5:00 PM (9.5 hrs, 1.5 OT)"
- **Specific work activities and locations**: "Electricians pulling wire in Panel Room B2 (grid C-4 to D-6, 2nd floor); Plumbers roughing-in restroom 204 (grid A-2, 2nd floor)"
- **Work NOT performed and reason**: "Mechanical sub could not start ductwork in south wing -- awaiting architect response to RFI-042 (submitted 3/15). 3 sheet metal workers on standby."
- **Productivity observations**: "Framing crew completed 12 LF of partition wall per hour vs. estimate of 18 LF/hr. Reduced productivity due to material staging in work area from concurrent flooring installation."

#### 2. Equipment Documentation
- **Equipment type, size, and identification**: "CAT 320 excavator (Unit #E-207), 40-ton RT crane (Crane #C-003), 2x concrete pump trucks"
- **Hours operated**: "Excavator operated 6.5 hours; Crane on standby 4 hours waiting for steel delivery"
- **Equipment idle time and reason**: "Crane idle from 10:00 AM to 2:00 PM awaiting steel truck delayed in transit (ETA revised 3x)"
- **Equipment moves**: "Concrete pump relocated from east pad to west pad at 1:00 PM (1-hour move time)"

#### 3. Weather Observations
- **Multiple observations per day**: Minimum at start of work, midday, and end of work
- **Temperature**: Actual readings, not "cold" or "warm"
- **Precipitation**: Type (rain, snow, sleet), start/stop times, accumulation
- **Wind**: Speed and direction, especially if affecting crane operations or roofing
- **Ground conditions**: "Standing water in excavation from overnight rain; 2 hours pumping before work could proceed"
- **Impact on work**: Direct connection between weather and work affected

#### 4. Material Deliveries
- **What was delivered**: Material type, quantity, specification
- **Delivery time**: Actual arrival vs. scheduled arrival
- **Condition on arrival**: Accepted, rejected, or accepted with exceptions
- **Delivery ticket reference**: Number and date
- **Storage location**: Where material was staged

#### 5. Visitors and Inspections
- **Who visited**: Name, company, role
- **Purpose of visit**: Inspection, meeting, observation, directive
- **Duration**: Arrival and departure time
- **Outcome**: Inspection passed/failed, directives given, observations made
- **Verbal directives**: Document in writing immediately: "At 10:30 AM, owner's rep John Miller directed crew to stop work on east wall pending review of revised elevation. Directive given verbally; this report serves as written documentation per AIA A201 Section 3.2."

#### 6. Impacts and Delays
- **Work out of sequence**: "Drywall installation in corridor 200 could not proceed because fire sprinkler rough-in not complete. Sprinkler sub reports 3-day delay for fittings. Drywall crew redirected to corridor 300."
- **Waiting for answers**: "MEP coordination hold continues. No response to RFI-042 (submitted 3/15, 12 days outstanding). This exceeds the 7-day contractual response period per spec 01 33 00."
- **Design issues**: "Field measurement shows column C-7 is 4 inches east of plan location. Ductwork routing per mechanical plans will not fit. RFI prepared for submittal tomorrow."
- **Owner/architect directives**: Any direction that changes scope, sequence, or schedule -- even if presented informally.
- **Access restrictions**: "South parking area not available per owner directive; material staging relocated to east lot, adding 200 feet to haul distance."

#### 7. Cross-References
- **Linked delay events**: Reference any active DELAY-NNN entries
- **Linked RFIs**: Reference pending or resolved RFIs affecting today's work
- **Linked change orders**: Reference any pending CORs or approved COs
- **Photo references**: "See photos IMG-2026-0315-001 through IMG-2026-0315-024 documenting conditions"

### Daily Report Writing Standards for Claims

- **Factual, not opinion**: "Concrete test cylinders showed 2,800 PSI at 7 days vs. specified 3,000 PSI" NOT "The concrete was bad"
- **Specific, not general**: Include grid lines, floor numbers, room numbers, compass directions
- **Complete sentences**: Fragments and abbreviations may be misinterpreted later
- **Consistent terminology**: Use the same names for locations, trades, and people throughout the project
- **No blame language**: State facts, not conclusions about fault. "Owner directed work stoppage" not "Owner caused a delay"
- **Preserve uncertainty**: "It appears that..." or "Based on field observation..." rather than definitive statements about matters not fully confirmed

---

## Photo and Video Documentation Standards

### Systematic Evidence Capture

Photography is the most powerful claims documentation tool available to field teams. A single well-timed, well-labeled photograph can be worth more than pages of written narrative. But photographs without context, organization, and metadata preservation are nearly worthless.

### Photo Schedule

**Minimum frequency for claims-sensitive activities**:

| Situation | Minimum Frequency | What to Capture |
|-----------|-------------------|-----------------|
| Normal operations | 2x daily (AM start, PM end) | General progress, crew deployment, conditions |
| Claims-sensitive work | 4x daily (start, mid-AM, mid-PM, end) | Specific activity, conditions, labor, equipment |
| Delay events | Hourly during event | Conditions causing delay, idle crews/equipment, affected areas |
| Differing site conditions | Immediately upon discovery + hourly | Actual conditions vs. expected, scale references, GPS location |
| Owner/architect directives | Before and after | Conditions before directive, work affected, scope changes |
| Weather events | At each weather observation | Sky conditions, precipitation, temperature display, ground conditions |
| Inspections | Before, during, after | Pre-inspection condition, inspector present, results |

### Metadata Preservation

**Critical rule**: Never edit original photo files. Editing, cropping, or filtering photographs destroys or alters EXIF metadata, which reduces evidentiary value.

**EXIF data to preserve**:
- **GPS coordinates**: Proves location of photograph
- **Timestamp**: Proves when photograph was taken
- **Camera/device identification**: Proves which device was used
- **Original file name**: Maintains traceability

**Best practices**:
- Enable GPS tagging on all field cameras and phones
- Verify date/time settings are correct on all devices
- Use a photo management app that preserves original metadata
- When sharing photos, share originals -- do not use messaging apps that strip metadata (iMessage, WhatsApp compress and strip EXIF)
- Store originals in a cloud service that preserves metadata (Google Drive, Dropbox, OneDrive)

### Photo Log Requirements

Every photograph should be traceable through a photo log entry:

```
Photo Log Entry:
  File: IMG-2026-0315-007.jpg
  Date: 2026-03-15
  Time: 10:30 AM
  Location: South Wing, Grid C-4 to D-6, 2nd Floor
  Direction: Facing north
  Photographer: Mike Thompson, Superintendent
  Description: MEP rough-in area showing ductwork routing conflict with structural column C-7.
               Column location prevents designed duct path. See RFI-042.
  Purpose: Document differing field condition vs. mechanical plans (Sheet M2.1)
  Linked To: RFI-042, DELAY-005, Daily Report 2026-03-15
```

### Video Documentation

**Weekly video walkthroughs** for projects with active or potential claims:

- **Duration**: 15-30 minutes covering all active work areas
- **Narration**: Superintendent narrates as they walk -- describing location, conditions, progress, issues
- **Steady movement**: Walk slowly, pause at key areas for 5-10 seconds
- **Scale references**: Include tape measures, rulers, or known objects for scale
- **Date/time**: State date and time at beginning of recording
- **Storage**: Upload same day to cloud storage; do not rely on phone storage alone

**When to increase video frequency**:
- Active delay events: daily video documenting conditions
- Differing site conditions: video immediately upon discovery
- Acceleration periods: video showing additional crews, overtime work
- Disputes in progress: daily video of all affected work areas

### Chain of Custody

For photographs and videos that may become evidence:

1. **Creation**: Document who took the photo/video, when, where, with what device
2. **Transfer**: Log when files are moved from device to computer to cloud
3. **Storage**: Maintain originals in a dedicated, access-controlled folder structure
4. **Access**: Document who has accessed original files and when
5. **Copies**: Clearly mark copies vs. originals; never modify originals
6. **Organization**: Store by date and location: `Photos/2026-03-15/South_Wing/`

### Cloud Backup Protocol

- Upload all photos and videos to cloud storage same day they are taken
- Organize by date, then location, then purpose
- Never delete from cloud storage even if project issue resolves
- Maintain backup on separate service or external drive
- Retention: minimum 6 years after substantial completion (statute of limitations varies by state; 6 years covers most jurisdictions)

---

## Schedule Impact Documentation

### Baseline vs. As-Built Reconciliation

Schedule analysis is the backbone of any delay or acceleration claim. Without a clear comparison between what was planned and what actually happened, there is no way to quantify the impact of a claimed event.

**Three schedules to maintain**:
1. **Baseline Schedule (As-Planned)**: The original contract schedule, accepted by all parties at project start. This is the benchmark.
2. **Updated Schedules**: Periodic schedule updates reflecting actual progress and re-forecasting remaining work. Typically monthly.
3. **As-Built Schedule**: The actual sequence and timing of all activities as they occurred. Reconstructed from daily reports, photos, delivery logs, and inspection records.

### Delay Event Correlation

Every claimed delay event must be mapped to its impact on the schedule:

```
Delay Event → Activity Affected → Float Available → Critical Path Impact → Schedule Extension

Example:
  Event: Owner approval delay for MEP design (RFI-042)
  Activity: MEP Rough-In (Activity ID: MEP-RI-001)
  Float: 2 days available
  Impact: 8-day delay consumed 2 days float, extended critical path 6 days
  Extension: 6 calendar days
```

### Time Impact Analysis (TIA)

The TIA is the gold standard methodology for demonstrating delay causation and quantification. Each delay event gets its own TIA:

**Step 1: Establish Pre-Delay Schedule**
Update the baseline schedule to reflect all actual progress up to the day before the delay event began. This becomes the "but-for" schedule -- what would have happened but for the delay.

**Step 2: Insert Delay Activity (Fragnet)**
Create a "fragnet" (fragment network) representing the delay event:
- Activity name: Description of the delay
- Duration: Actual duration of the delay
- Predecessors: Tie to the activity that was delayed
- Successors: Tie to the activities that could not proceed until delay resolved

**Step 3: Recalculate Schedule**
Run the CPM calculation with the fragnet inserted. The new completion date minus the pre-delay completion date equals the delay impact.

**Step 4: Document Results**
```
TIA Summary:
  Pre-Delay Completion Date:  July 29, 2026
  Post-Delay Completion Date: August 4, 2026
  Delay Impact: 6 calendar days
  Cause: Owner approval delay (RFI-042)
  Critical Path: Confirmed (MEP Rough-In is critical)
  Float Consumed: 2 days
  Net Extension: 6 days
```

### Fragnet Creation

A fragnet is a mini-schedule network inserted into the project schedule to model a specific delay event. For each delay:

```json
{
  "fragnet_id": "FRAG-005",
  "linked_delay": "DELAY-005",
  "description": "Owner approval delay for MEP design revision per RFI-042",
  "activities": [
    {
      "id": "FRAG-005-A",
      "name": "Awaiting architect response to RFI-042",
      "duration_days": 7,
      "predecessor": "MEP-RI-001-START",
      "successor": "FRAG-005-B"
    },
    {
      "id": "FRAG-005-B",
      "name": "Revised submittal review and approval",
      "duration_days": 5,
      "predecessor": "FRAG-005-A",
      "successor": "MEP-RI-001-RESUME"
    }
  ],
  "total_fragnet_duration": 12,
  "float_absorbed": 2,
  "net_critical_path_impact": 10
}
```

### Concurrent Delay Identification

When two or more delays overlap in time:

**Step 1: Identify Overlap**
Map delay date ranges on a timeline. Are any overlapping?

**Step 2: Determine Independence**
Are the delays independent of each other, or did one cause the other?

**Step 3: Determine Path Impact**
Are the delays on the same critical path, different paths, or a combination?

**Step 4: Allocate Impact**
- **Same path, independent delays**: Extension = MAX(delay_1, delay_2), not SUM
- **Different paths**: Each delay analyzed separately against its own path float
- **Causation chain**: If Delay A caused Delay B, total impact is the full chain, attributed to the root cause

### Float Ownership and Consumption Tracking

Float ownership is often disputed. Key positions:

- **Contractor position**: Float belongs to whoever needs it; first to use it owns it
- **Owner position**: Float is a project resource, not belonging to either party
- **Contract language controls**: Many contracts specify float ownership. Check the contract first.

**Tracking requirements**:
- Record baseline float for every activity at project start
- Track float consumption as delays occur
- Document which party consumed float and why
- Flag when critical path shifts due to float consumption

### Acceleration Documentation

**Directed acceleration**: Owner formally directs contractor to accelerate schedule.
- Document: Written directive, acknowledgment, cost proposal, approval
- Cost basis: Overtime premium, additional crews, equipment mobilization, out-of-sequence work premium

**Constructive acceleration**: Owner denies time extension for an excusable delay, forcing contractor to accelerate to meet original deadline.
- Document: Time extension request, denial letter, evidence of excusable delay, evidence of acceleration measures taken
- This is a claim -- the contractor accelerates under protest and seeks cost recovery
- Critical documentation: The denial of the time extension must be clear and documented

**Acceleration cost categories**:
- Overtime labor premium (typically 1.5x or 2x base rate)
- Additional crew mobilization and management
- Expedited material procurement (premium pricing, air freight)
- Out-of-sequence work (reduced productivity from working trades concurrently in same space)
- Extended supervision for multiple shifts
- Productivity loss from fatigue (overtime beyond 50 hrs/week shows measurable decline)

---

## Cost Impact Documentation

### Loss of Productivity

Loss of productivity claims assert that the contractor's work was less efficient than it should have been due to owner-caused disruptions. These claims require rigorous documentation because the burden of proof is on the contractor.

#### Measured Mile Analysis

The measured mile is the most defensible method for proving lost productivity. It compares the contractor's actual productivity during an unimpacted period (the "measured mile") against productivity during the impacted period.

**Requirements**:
1. **Identify unimpacted period**: A period on the same project where the same type of work was performed without the claimed disruption
2. **Identify impacted period**: The period when disruption was occurring
3. **Compare productivity**: Units of work per labor hour in each period
4. **Calculate loss**: Difference in productivity multiplied by total impacted work quantity

**Example**:
```
Measured Mile Analysis: Electrical Conduit Installation

Unimpacted Period (January 2026):
  Work completed: 2,400 LF of 3/4" EMT conduit
  Labor hours: 300 hours (4 electricians x 75 hrs each)
  Productivity: 8.0 LF per labor hour

Impacted Period (March 2026 -- concurrent trade stacking):
  Work completed: 1,800 LF of 3/4" EMT conduit (same spec, same conditions)
  Labor hours: 360 hours (4 electricians x 90 hrs each)
  Productivity: 5.0 LF per labor hour

Productivity Loss: 8.0 - 5.0 = 3.0 LF/hr (37.5% reduction)

Total Impacted Work Remaining: 6,000 LF
Additional Hours Required: 6,000 / 5.0 - 6,000 / 8.0 = 1,200 - 750 = 450 extra hours
Cost at $65/hr fully burdened: 450 x $65 = $29,250 productivity loss claim
```

**Key requirements for measured mile**:
- Same type of work in both periods (same specification, same general conditions)
- Same crew or comparable crew skill level
- Clear identification of the disruption that differentiates the periods
- Sufficient sample size in both periods (minimum 2 weeks of data recommended)

#### Industry Studies

When a measured mile comparison is not possible (no unimpacted period exists on the project), industry studies provide recognized productivity loss factors:

**Mechanical Contractors Association (MCA) Study**: Provides productivity loss factors for various disruption types:
- Trade stacking (multiple trades in same area): 10-25% loss
- Overtime (sustained, >50 hrs/week): 15-25% loss after 4 weeks
- Morale/attitude (from disruption): 5-15% loss
- Reassignment of manpower: 5-10% loss
- Concurrent operations: 10-20% loss

**Leonard Study (1988)**: Factors for productivity impact of changes on unchanged work:
- Projects with 10-15% change: 5-8% productivity loss on remaining unchanged work
- Projects with 15-25% change: 8-15% loss
- Projects with 25%+ change: 15-25% loss

**Ibbs Study (2005)**: Updated productivity impact research confirming similar ranges with additional data on timing of changes (late changes cause disproportionately higher productivity loss).

**Important caveat**: Industry studies are a fallback, not a first choice. Arbitrators and courts prefer project-specific data (measured mile) over industry averages. Use industry studies only when project data is insufficient.

#### Force Account Comparison

When productivity cannot be measured by the mile, force account (T&M) records provide cost documentation:
- Detailed daily time sheets by worker name and hours
- Material quantities installed per day
- Equipment hours by machine
- Comparison to original estimate or bid labor hours for the same work

### Remobilization Costs

When work is suspended and later resumed, remobilization costs include:

- **Equipment move-in/move-out**: Crane mobilization ($5,000-$25,000 per move), heavy equipment transport
- **Crew reassignment**: Travel costs, per diem, lost time between assignments
- **Learning curve**: First 2-3 days after remobilization show reduced productivity (typically 20-40% loss)
- **Material re-staging**: Moving stored materials back to work areas
- **Re-inspection**: Work completed before suspension may require re-inspection before resuming

### Acceleration Costs

Document acceleration costs separately from base contract work:

- **Overtime premium**: Track hours at straight time vs. 1.5x vs. 2x separately
- **Additional crews**: Document mobilization date, crew size, daily cost
- **Out-of-sequence work**: Track productivity loss when work must be performed out of optimal sequence
- **Expedited materials**: Document original delivery date, expedited delivery date, premium paid
- **Additional supervision**: Cost of additional foremen, superintendents, or PMs for extended hours or multiple shifts

### Extended General Conditions

For each day of compensable delay, the contractor incurs general conditions costs that would not have been incurred but for the delay:

**Daily General Conditions Rate Calculation**:
```
Monthly General Conditions Budget: $75,000
  Superintendent salary + benefits:    $18,000
  Project Manager (allocated):         $12,000
  Site office rental:                  $3,500
  Temporary utilities:                 $2,200
  Site phone/internet:                 $800
  Temporary toilets:                   $1,200
  Dumpster service:                    $2,400
  Project insurance (monthly):         $8,500
  Bond cost (monthly):                 $4,200
  Equipment rental (monthly):          $12,000
  Vehicle/fuel:                        $3,200
  Miscellaneous:                       $7,000

Daily Rate: $75,000 / 30 = $2,500/day

For 15 days of compensable delay:
Extended General Conditions Claim: 15 x $2,500 = $37,500
```

**Documentation requirements**: Actual invoices, payroll records, and receipts for each line item. The daily rate must be supportable with real costs, not estimates.

### Eichleay Formula for Home Office Overhead

The Eichleay formula is the standard method for calculating unabsorbed home office overhead during a period of government-caused delay (primarily used on federal contracts, but increasingly accepted in private work).

**The Formula**:
```
Step 1: Allocable Overhead
  (Contract Billings / Total Company Billings for Period) x Total Home Office OH for Period
  = Allocable Overhead

Step 2: Daily Rate
  Allocable Overhead / Days of Contract Performance
  = Daily Contract OH Rate

Step 3: Recoverable Amount
  Daily Contract OH Rate x Days of Compensable Delay
  = Recoverable Home Office Overhead
```

**Worked Example**:
```
Eichleay Calculation:

Company Data (Annual):
  Total company billings (all projects): $25,000,000
  Total home office overhead:            $2,500,000

This Project:
  Contract billings to date:             $4,200,000
  Contract performance period:           365 days
  Compensable delay period:              30 days

Step 1: Allocable OH
  ($4,200,000 / $25,000,000) x $2,500,000 = $420,000

Step 2: Daily Rate
  $420,000 / 365 days = $1,150.68/day

Step 3: Recoverable HOH
  $1,150.68 x 30 days = $34,520.55

Total Home Office Overhead Claim: $34,520.55
```

**Eichleay requirements**:
- Government (or owner) caused the delay
- Contractor was on standby and could not take on replacement work
- Contractor's home office continued to incur overhead during the delay
- Financial records must be auditable and verifiable

### Lost Profit

Lost profit (consequential damages) is rarely recoverable in construction contracts because most contracts contain mutual waiver of consequential damages clauses (AIA A201 Section 15.1.7).

**When recoverable**:
- Contract does not contain consequential damages waiver
- Breach is willful or in bad faith
- Lost profits are reasonably foreseeable and provable

**Documentation**: If pursuing lost profit, document: revenue lost from inability to take on other work during delay, contracts or bids declined due to resource commitment, historical profit margins on comparable work.

---

## Causation Evidence

### The Critical Chain: Event to Impact to Damages

Every construction claim must establish three linked elements. Missing any one element defeats the claim:

```
EVENT ──────────► IMPACT ──────────► DAMAGES
(What happened)   (What it caused)   (What it cost)

Example:
EVENT:   Owner directed suspension of MEP work pending design review (RFI-042)
IMPACT:  MEP rough-in delayed 8 calendar days; critical path extended 6 days
DAMAGES: Extended general conditions ($15,000) + sub standby ($8,000) + equipment ($3,200) = $26,200
```

### Traceability Requirements

Each damage item must trace back through the impact to the event. This is the "but-for" test: but for the event, the contractor would not have incurred this cost.

**Traceability matrix**:
```
| Damage Item | Amount | Impact | Event | Evidence |
|------------|--------|--------|-------|----------|
| Extended superintendent | $7,500 | 6-day CP extension | Owner RFI delay | Payroll records, daily reports |
| Sub standby (XYZ Mech) | $8,000 | MEP crew idle 8 days | Owner RFI delay | Sub invoices, daily reports |
| Crane rental extension | $3,200 | Equipment held on-site | Owner RFI delay | Rental invoices |
| Overtime premium | $4,800 | Acceleration to recover | Owner denied extension | Time sheets, denial letter |
```

### Common Causation Failures

**1. Gap in documentation**: The event is documented but the link to the impact is not. Example: Daily reports show the delay, but there is no schedule analysis showing critical path impact.

**2. Assumed rather than proven causation**: "The delay must have caused the cost increase" is not sufficient. Must show specific cost increases tied to specific delay days.

**3. Failure to account for concurrent causes**: If the contractor also caused delays during the same period, failing to address concurrent causation destroys credibility.

**4. Speculative damages**: Damages must be proven with reasonable certainty, not hypothetical calculations. "We think we lost about $50,000" will not survive scrutiny.

**5. Betterment**: If the claimed event resulted in an improvement to the work (better design, upgraded materials), the contractor cannot claim the full cost -- must net out the betterment value.

### Causation Documentation Checklist

For each claimed event:
- [ ] Written record of the event (directive, RFI, inspection report, daily report)
- [ ] Date and time of the event
- [ ] Who caused or directed the event
- [ ] What work was affected and how
- [ ] Duration of the impact (start date, end date)
- [ ] Schedule analysis showing critical path effect
- [ ] Cost records showing damages incurred during impact period
- [ ] "But-for" analysis: these costs would not have been incurred but for the event
- [ ] Mitigation efforts documented (what the contractor did to minimize impact)
- [ ] Concurrent cause analysis (were there other contributing factors?)

---

## Notice Requirements

### THE MOST IMPORTANT PROCEDURAL ELEMENT

**Failure to give timely notice can waive all claim rights regardless of merit.** This cannot be overstated. A contractor with a $2 million claim supported by perfect documentation will recover nothing if the contract required 21-day notice and the contractor gave notice on day 25.

### Standard Notice Periods

| Contract Form | Notice Provision | Deadline | Reference |
|--------------|-----------------|----------|-----------|
| AIA A201 (2017) | Claims must be initiated by written notice | Within 21 days of event | Section 15.1.3 |
| AIA A201 (2017) | Concealed/unknown conditions | Promptly upon discovery | Section 3.7.4 |
| ConsensusDocs 200 | Written notice of claim | Within 14 days of event | Section 8.4 |
| Federal (FAR) | Notice of differing site conditions | Promptly, before conditions disturbed | FAR 52.236-2 |
| Federal (FAR) | REA/Claim submission | Within 6 years | Contract Disputes Act |
| EJCDC C-700 | Written notice of claim | Within 30 days of event | Section 12.01 |

**Critical**: Always check the specific contract for notice provisions. Many owners modify standard forms to shorten notice periods (7 days, 10 days, or even "immediate" notice).

### Notice Letter Content

Every formal notice must include:

1. **Date of notice letter**
2. **Parties**: To (owner/architect) and From (contractor)
3. **Contract reference**: Project name, contract number, date of agreement
4. **Contract provision**: Specific section requiring notice (e.g., "Per AIA A201 Section 15.1.3")
5. **Description of event**: Factual description of what occurred or was discovered
6. **Date of event**: When the event occurred or was first discovered
7. **Impact on work**: How the event is affecting or will affect the work
8. **Request for relief**: Specific request (time extension, cost adjustment, both)
9. **Reservation of rights**: Statement preserving all contractual and legal remedies
10. **Supporting documentation reference**: List of attached or forthcoming documentation

### Notice Delivery Requirements

- **Certified mail with return receipt requested**: Creates proof of delivery with date
- **Email**: Send to all contract-designated recipients AND project manager/architect
- **Hand delivery**: With signed acknowledgment of receipt
- **Best practice**: Send by ALL three methods simultaneously
- **Keep proof**: Certified mail receipt, email sent confirmation, signed acknowledgment

### Reservation of Rights Language

Every notice should include reservation of rights language:

```
Contractor reserves all rights under the Contract Documents, at law, and in equity,
including but not limited to the right to seek additional time and/or cost adjustments
as the full extent of the impact becomes known. This notice is provided to preserve
Contractor's rights and is not intended to be a complete or final statement of
Contractor's claim. Contractor will supplement this notice with additional information
as it becomes available.
```

### Notice Types and Templates

**Type 1: Delay Notice**
```
RE: Notice of Delay -- [Project Name], Contract No. [XXX]

This letter provides formal notice pursuant to [Contract Section] that Contractor
has encountered a delay to the Work caused by [description of event].

Event Date: [Date]
Description: [Factual description]
Activities Affected: [List activities]
Estimated Duration: [Days, if known] (to be updated as impact becomes clear)
Critical Path Impact: [Preliminary assessment]

Contractor requests a time extension of [X] calendar days (subject to refinement
as the full impact is determined). [Add cost recovery request if compensable delay.]
```

**Type 2: Change Order / Extra Work Notice**
```
RE: Notice of Change in Work -- [Project Name], Contract No. [XXX]

This letter provides formal notice pursuant to [Contract Section] that Contractor
has been directed to perform work that constitutes a change to the Contract.

Directive Date: [Date]
Directive Source: [Who gave the directive, verbal/written]
Description of Changed Work: [What was directed]
Contract Basis: [Why this is a change -- not in original scope, different conditions, etc.]
Estimated Cost Impact: [Preliminary, subject to detailed pricing]
Estimated Schedule Impact: [Preliminary]

Contractor will submit a formal Change Order Request within [X] days.
```

**Type 3: Differing Site Conditions Notice**
```
RE: Notice of Differing Site Conditions -- [Project Name], Contract No. [XXX]

Pursuant to [Contract Section / FAR 52.236-2], Contractor provides notice of
subsurface or physical conditions materially different from those indicated in
the Contract Documents.

Date of Discovery: [Date]
Location: [Specific location with grid/coordinates]
Condition Discovered: [Factual description of actual conditions]
Contract Indication: [What the contract documents showed/indicated]
Difference: [How actual differs from indicated]
Impact on Work: [How this affects current and planned work]

Contractor requests that Owner investigate the conditions before they are
further disturbed. Contractor reserves the right to request equitable adjustment
for time and cost.
```

**Type 4: Constructive Change Notice**
```
RE: Notice of Constructive Change -- [Project Name], Contract No. [XXX]

Contractor provides notice that actions by [Owner/Architect] constitute a
constructive change to the Contract, entitling Contractor to equitable adjustment.

Event: [Description of owner/architect action that changes the work without a formal CO]
Date: [When it occurred]
Why This Is a Change: [Contract basis -- how it differs from original scope/requirements]
Impact: [Cost and schedule impact, preliminary]

Contractor will perform the work under protest and reserves the right to seek
equitable adjustment for all additional costs and time.
```

**Type 5: Acceleration Notice**
```
RE: Notice of Constructive Acceleration -- [Project Name], Contract No. [XXX]

Contractor provides notice that Owner's denial of Contractor's time extension
request dated [date], combined with Owner's insistence on maintaining the
original completion date, constitutes constructive acceleration.

Time Extension Request: [Reference to original request]
Excusable Delay: [Description of the excusable delay]
Owner's Response: [Denial of extension, with date]
Acceleration Required: [What the contractor must do to meet original deadline]
Estimated Acceleration Cost: [Preliminary]

Contractor will proceed with acceleration measures under protest and will seek
recovery of all acceleration costs incurred.
```

### Notice Tracking

Maintain a notice log tracking:

```json
{
  "notice_id": "NOTICE-001",
  "type": "delay",
  "date_sent": "2026-03-02",
  "contract_provision": "AIA A201 Section 15.1.3",
  "event_date": "2026-03-01",
  "deadline_date": "2026-03-22",
  "days_remaining_at_notice": 20,
  "sent_via": ["certified_mail", "email"],
  "certified_mail_tracking": "9400111899223100XXXXX",
  "recipients": ["owner_pm@example.com", "architect@example.com"],
  "delivery_confirmed": true,
  "delivery_date": "2026-03-04",
  "linked_claim": "CLAIM-001",
  "linked_delay": "DELAY-005",
  "response_received": false,
  "response_date": null,
  "follow_up_required": true,
  "follow_up_date": "2026-03-16"
}
```

---

## Concurrent Delay

### Definition and Identification

Concurrent delays occur when two or more delay events overlap in time and both potentially affect project completion. Concurrent delay is one of the most contentious areas in construction claims because it directly affects the allocation of responsibility.

### Types of Concurrent Delay

**True Concurrent Delay**: Two independent delays occur simultaneously, both on the critical path. Neither party can prove their delay would not have occurred but for the other delay.

**Pacing Delay**: A non-critical delay that appears concurrent but is actually caused by a party deliberately slowing down because the critical path is already delayed. Example: Contractor slows interior work because the building envelope is delayed by owner changes -- the interior slow-down is pacing, not an independent delay.

**Sequential Delay**: Delays that appear concurrent in time but affect different paths. These are not truly concurrent and should be analyzed independently.

### Allocation Methods

**1. Apportionment (Shared Responsibility)**
- Each party bears a proportional share of the delay based on the relative duration and criticality of their respective delays
- Example: If owner caused 7 days of delay and contractor caused 3 days concurrently, owner bears 70% and contractor bears 30%
- Favored in many jurisdictions but requires sufficient evidence to apportion

**2. Dominant Cause**
- The delay that had the greatest impact on the critical path governs
- If owner delay is 7 days on critical path and contractor delay is 3 days on a near-critical path, owner delay dominates
- Used when apportionment is impractical

**3. All-or-Nothing**
- Some jurisdictions hold that if the contractor contributed to any concurrent delay, the contractor recovers nothing
- Harsh rule, but applied in some federal government contexts
- Makes it critical to document that contractor delays were independent and minimal

### Documentation Requirements for Concurrent Delay

1. **Independent analysis**: Analyze each delay separately to show its individual impact
2. **Timeline mapping**: Create a timeline showing when each delay started, ended, and overlapped
3. **Critical path analysis**: Show which delays were on the critical path and which had float
4. **Causation independence**: Document that the delays were caused by different parties for different reasons
5. **Pacing defense**: If accused of concurrent delay, show that any contractor slow-down was pacing a prior owner-caused delay

---

## Claims Package Assembly

### Structure of a Formal Claims Package

A claims package is the formal submission of a claim to the owner, typically after initial notice and failed resolution at the project level. It must be comprehensive, organized, and professionally presented.

#### 1. Cover Letter
- Date, parties, contract reference
- Summary of claim (one paragraph)
- Total amount claimed (time and/or cost)
- Request for resolution meeting or ADR

#### 2. Executive Summary (2-5 pages)
- Project background (brief)
- Chronology of events leading to the claim
- Summary of liability basis (contract provisions supporting the claim)
- Summary of damages (time extension, cost recovery, or both)
- Total claim value with breakdown by category

#### 3. Chronology of Events
- Detailed timeline from project start through the claim events
- Each entry dated with source document reference
- Focus on key events, decisions, and impacts
- Format: Date | Event | Source Document | Impact

#### 4. Liability Analysis
- Contract provisions supporting the claim (quoted with section references)
- Applicable law (state contract law, federal regulations if applicable)
- Comparison of contract requirements to actual events
- Demonstration that the claimed events fall within the contract's remedy provisions

#### 5. Quantum Analysis (Damages Calculation)
- Detailed calculation of each damage category
- Supporting worksheets and backup documentation
- Summary table:

```
| Category | Amount | Basis |
|----------|--------|-------|
| Extended General Conditions | $37,500 | 15 days x $2,500/day |
| Loss of Productivity | $29,250 | Measured mile analysis |
| Acceleration Costs | $18,400 | Overtime + additional crews |
| Home Office Overhead (Eichleay) | $34,521 | 30-day delay period |
| Subcontractor Impacts | $22,000 | Sub claims passthrough |
| Equipment Standby | $8,800 | Idle equipment during delay |
| TOTAL | $150,471 | |
```

#### 6. Schedule Analysis
- Baseline schedule summary
- TIA for each delay event
- As-built schedule reconstruction
- Critical path analysis showing delay impact
- Concurrent delay analysis (if applicable)
- Float consumption summary

#### 7. Supporting Documents Appendix
Organized by exhibit number:
- **Exhibit A**: Notices (all formal notices with proof of delivery)
- **Exhibit B**: Daily reports (for all dates referenced in the claim)
- **Exhibit C**: Correspondence (emails, letters, meeting minutes)
- **Exhibit D**: RFIs and responses
- **Exhibit E**: Change orders (approved and pending)
- **Exhibit F**: Schedule documents (baseline, updates, as-built)
- **Exhibit G**: Cost documentation (invoices, payroll, equipment records)
- **Exhibit H**: Photographs and videos (with photo log)
- **Exhibit I**: Weather data (NOAA records)
- **Exhibit J**: Expert reports (if applicable)

### Organization Principles

- **Chronological within each section**: Events, documents, and evidence organized by date
- **Cross-referenced**: Every statement in the narrative references a specific exhibit
- **Indexed**: Table of contents for the entire package, plus index for each exhibit
- **Paginated**: Sequential page numbers throughout (including exhibits)
- **Electronic and hard copy**: Provide both; electronic version should be searchable PDF with bookmarks

### Expert Report Coordination

When to engage experts:
- **Schedule expert (delay analyst)**: When delay claims exceed $100,000 or involve complex concurrent delays
- **Cost expert (forensic accountant)**: When cost claims exceed $250,000 or involve multiple damage categories
- **Claims consultant**: When total claim value exceeds $500,000 or dispute is headed to arbitration/litigation

---

## Mediation/Arbitration Preparation

### Document Organization for Proceedings

When a claim proceeds to mediation, arbitration, or litigation, document organization becomes critical. The goal is to present a clear, compelling narrative supported by easily accessible evidence.

### Timeline Creation

Build a visual chronology showing:
- Key project milestones (NTP, substantial completion, etc.)
- Delay events with duration bars
- Notice dates (sent and received)
- Correspondence highlights
- Schedule impacts
- Cost accrual points

Format: Wall-sized timeline for hearing room + digital version for screen sharing.

### Witness Identification and Preparation

**Fact witnesses** (people with direct knowledge of events):
- Superintendent(s) who observed conditions
- Project manager who managed communications
- Subcontractor foremen who experienced impacts
- Owner's representatives who gave directives

**Expert witnesses** (if retained):
- Schedule analyst for delay opinions
- Cost consultant for damages opinions
- Industry expert for standard of care opinions

**Witness preparation**:
- Review all documents the witness authored or received
- Identify key events the witness will testify about
- Prepare a timeline of the witness's involvement
- Anticipate cross-examination questions
- Remind witnesses: answer only what is asked, do not volunteer

### Key Document Identification

**Smoking gun documents**: The single most impactful document for each element of the claim. Examples:
- Owner email directing work stoppage (proves the event)
- Daily report showing idle crews (proves the impact)
- Invoice for overtime premium (proves the damages)

**Corroborating evidence**: Secondary documents that support the smoking gun:
- Multiple daily reports showing the same condition
- Photographs confirming written descriptions
- Third-party records (NOAA weather, inspector reports)

### File Organization System

For hearings, organize into binder sets:

**Binder 1: Claim Summary**
- Executive summary, chronology, damages summary

**Binder 2: Contract Documents**
- Relevant contract provisions, specifications, drawings

**Binder 3: Notices and Correspondence**
- All formal notices, key emails, letters

**Binder 4: Daily Reports**
- Daily reports for all dates referenced, tabbed by date

**Binder 5: Schedule Analysis**
- Baseline, updates, as-built, TIA worksheets

**Binder 6: Cost Documentation**
- Invoices, payroll, equipment records, damage calculations

**Binder 7: Photographs and Visual Evidence**
- Photo log with selected key photographs, printed and labeled

---

## Claims Documentation Data Model

### JSON Schema for Claims Management

#### claims-log.json

```json
{
  "claims": [
    {
      "id": "CLAIM-001",
      "status": "active",
      "title": "MEP Design Coordination Delay and Acceleration",
      "type": "delay_and_cost",
      "date_initiated": "2026-03-02",
      "notice_date": "2026-03-02",
      "notice_deadline": "2026-03-22",
      "notice_compliant": true,
      "contract_provision": "AIA A201 Section 15.1.3",
      "description": "Owner approval delay for MEP design revision per RFI-042 caused 8-day delay to critical path MEP rough-in, resulting in 6-day schedule extension and acceleration costs to recover partial schedule.",
      "events": [
        {
          "event_id": "EVT-001",
          "date": "2026-03-01",
          "description": "MEP coordination conflict identified; RFI-042 submitted",
          "type": "trigger",
          "evidence": ["RFI-042", "DR-2026-03-01", "IMG-2026-0301-004"]
        },
        {
          "event_id": "EVT-002",
          "date": "2026-03-08",
          "description": "Architect issued revised drawing M2.1 Rev A",
          "type": "resolution",
          "evidence": ["DWG-M2.1-RevA", "DR-2026-03-08"]
        }
      ],
      "schedule_impact": {
        "delay_days": 8,
        "float_consumed": 2,
        "critical_path_extension": 6,
        "acceleration_days": 3,
        "net_schedule_impact": 3,
        "linked_delays": ["DELAY-005"],
        "tia_performed": true,
        "fragnet_id": "FRAG-005"
      },
      "damages": {
        "extended_general_conditions": 15000,
        "loss_of_productivity": 0,
        "acceleration_costs": 18400,
        "home_office_overhead": 0,
        "subcontractor_impacts": 8000,
        "equipment_costs": 3200,
        "material_escalation": 0,
        "total_claimed": 44600,
        "calculation_method": "actual_cost",
        "supporting_docs": ["INV-XYZ-0308", "PAY-2026-03", "EQ-RENT-0308"]
      },
      "notices": ["NOTICE-001", "NOTICE-003"],
      "linked_delays": ["DELAY-005"],
      "linked_change_orders": ["COR-012"],
      "linked_rfis": ["RFI-042"],
      "linked_daily_reports": ["2026-03-01", "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05", "2026-03-06", "2026-03-07", "2026-03-08"],
      "evidence_inventory": [
        {
          "exhibit": "A",
          "description": "Notice of Delay dated 2026-03-02",
          "type": "notice",
          "file_ref": "NOTICE-001"
        },
        {
          "exhibit": "B",
          "description": "RFI-042 and architect response",
          "type": "rfi",
          "file_ref": "RFI-042"
        },
        {
          "exhibit": "C",
          "description": "Daily reports 3/1-3/8",
          "type": "daily_report",
          "file_ref": "DR-2026-03-01 through DR-2026-03-08"
        },
        {
          "exhibit": "D",
          "description": "Photographs of MEP conflict area",
          "type": "photo",
          "file_ref": "IMG-2026-0301-004 through IMG-2026-0308-012"
        }
      ],
      "resolution": {
        "status": "pending",
        "method": null,
        "settlement_amount": null,
        "settlement_date": null,
        "notes": ""
      },
      "date_created": "2026-03-02T08:00:00Z",
      "date_updated": "2026-03-15T14:30:00Z"
    }
  ],
  "notice_log": [
    {
      "id": "NOTICE-001",
      "type": "delay",
      "claim_id": "CLAIM-001",
      "date_sent": "2026-03-02",
      "deadline_date": "2026-03-22",
      "contract_provision": "AIA A201 Section 15.1.3",
      "sent_via": ["certified_mail", "email"],
      "tracking_number": "9400111899223100XXXXX",
      "recipients": ["owner_pm@example.com", "architect@example.com"],
      "delivery_confirmed": true,
      "delivery_date": "2026-03-04",
      "response_received": false,
      "response_date": null,
      "follow_up_date": "2026-03-16",
      "content_summary": "Notice of delay due to MEP design coordination issue per RFI-042. Request for time extension and cost adjustment."
    }
  ],
  "evidence_inventory": [
    {
      "id": "EVID-001",
      "type": "daily_report",
      "date": "2026-03-01",
      "description": "Daily report documenting MEP coordination conflict discovery",
      "file_path": "daily-report-data.json#2026-03-01",
      "linked_claims": ["CLAIM-001"],
      "quality_rating": "tier_1",
      "verified": true
    }
  ],
  "timeline_events": [
    {
      "date": "2026-03-01",
      "event": "MEP coordination conflict identified; RFI-042 submitted",
      "type": "trigger",
      "claim_id": "CLAIM-001",
      "category": "design_issue"
    },
    {
      "date": "2026-03-02",
      "event": "Formal delay notice sent (NOTICE-001)",
      "type": "notice",
      "claim_id": "CLAIM-001",
      "category": "procedural"
    },
    {
      "date": "2026-03-08",
      "event": "Architect issues revised drawing M2.1 Rev A",
      "type": "resolution",
      "claim_id": "CLAIM-001",
      "category": "design_issue"
    }
  ],
  "summary": {
    "total_active_claims": 1,
    "total_claimed_amount": 44600,
    "total_recovered_amount": 0,
    "pending_notices": 1,
    "overdue_notices": 0,
    "next_deadline": "2026-03-22",
    "last_updated": "2026-03-15T14:30:00Z"
  }
}
```

---

## Integration with Other Skills

### delay-tracker
- Delay events logged via `/delay` feed directly into claims documentation
- Each DELAY-NNN entry can be linked to a CLAIM-NNN entry
- Delay classification (excusable/compensable) determines claim eligibility
- TIA and critical path analysis from delay-tracker provide schedule impact documentation
- Weather delay data provides environmental claims support

### contract-administration
- Notice provisions (deadlines, delivery methods) from contract analysis
- Dispute resolution procedures (mediation, arbitration, litigation)
- Change order clauses and procedures
- Claims initiation requirements per contract
- Consequential damages waiver identification
- Liquidated damages provisions

### daily-report-format
- Claims-grade daily reports provide the foundation for all claims
- Auto-linking daily reports to delay events and claims
- Daily report fields specifically designed for claims support (headcount by name, exact times, impacts observed)
- Photo documentation integrated with daily reports

### change-order-tracker
- Disputed change orders become potential claims
- COR (Change Order Request) documentation feeds claims package
- Constructive change documentation
- Back-charge disputes

### cost-tracking
- Actual cost data for damages quantification
- Labor hour tracking for measured mile analysis
- Equipment cost tracking for extended rental claims
- General conditions daily rate calculation from actual costs
- Subcontractor cost documentation

### pay-application
- Payment disputes may escalate to claims
- Retainage disputes
- Disputed back-charges on pay applications
- Lien rights and timing (related to but separate from claims)

### safety-management
- Safety incidents caused by owner conditions may support claims
- OSHA compliance costs imposed by changed conditions
- Work stoppage due to unsafe owner-created conditions

### look-ahead-planner
- Three-week look-ahead changes due to delay events
- Documentation of schedule recovery efforts
- Evidence of acceleration measures in look-ahead revisions

---

## Output Routing

All generated documents route to project folder structure:
- **Claims Log**: Stored in `{{folder_mapping.config}}/claims-log.json`
- **Notice Letters**: `{{folder_mapping.correspondence}}/Notices/NOTICE-NNN_[type]_[date].docx`
- **Claims Packages**: `{{folder_mapping.reports}}/Claims/CLAIM-NNN_Package_[date].docx`
- **Evidence Exports**: `{{folder_mapping.reports}}/Claims/Evidence/[exhibit_letter]_[description].pdf`
- **Version History**: Logged in `project-config.json` `version_history` array
- **Backup Copies**: `{{folder_mapping.config}}/backups/claims-log_[TIMESTAMP].json`
