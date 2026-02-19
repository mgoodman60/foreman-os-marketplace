---
name: contract-administration
description: >
  Manage construction contract administration from the field perspective. Covers AIA contract forms (A101, A201, A401), bond types and requirements, mechanics lien law, insurance verification, indemnification, dispute resolution, and subcontractor default procedures. Provides practical field guidance for notice requirements, lien waiver processing, COI verification, and claims documentation. Integrates with pay-application (lien waivers), change-order-tracker (constructive changes), delay-tracker (notice provisions), sub-performance (default triggers), and cost-tracking (back-charges). Triggers: "contract", "contract admin", "AIA", "A201", "A101", "bond", "performance bond", "payment bond", "lien", "lien waiver", "mechanics lien", "insurance", "COI", "certificate of insurance", "OCIP", "CCIP", "indemnification", "dispute", "mediation", "arbitration", "notice", "cure notice", "default", "sub default", "termination for cause", "claims", "ConsensusDocs", "EJCDC".
version: 1.0.0
---

# Contract Administration Skill

## Overview

The **contract-administration** skill provides construction superintendents with practical, field-level guidance on contract administration tasks that directly affect daily operations. This is not a law school course -- it is the working knowledge a superintendent needs to protect the project, keep subcontractors accountable, process pay applications correctly, and avoid the costly mistakes that happen when field personnel do not understand the contract documents sitting in the job trailer.

**Why superintendents need this:**
- You sign daily reports that become evidence in claims and disputes
- You accept or reject work that triggers payment obligations
- You direct subcontractors under contracts you may not have read cover-to-cover
- You are the first person to notice when a sub is failing, and the documentation you create (or fail to create) determines whether the project can terminate for cause or is stuck
- Your verbal directives can create constructive change orders worth hundreds of thousands of dollars
- Missing a notice deadline by even one day can waive the project's right to recover time or money

**What this skill covers:**
1. AIA contract forms that govern most commercial construction
2. How ConsensusDocs and EJCDC contracts differ (so you are not blindsided)
3. Bond types, requirements, and claims processes
4. Mechanics lien law and lien waiver processing
5. Insurance requirements and COI verification
6. Indemnification clauses and what they mean in the field
7. Dispute resolution procedures from notice through arbitration
8. Subcontractor default procedures from warning signs through replacement

**Critical principle:** In contract administration, **written notice is everything**. Verbal conversations do not preserve contractual rights. If it is not in writing, it did not happen.

---

## AIA Contract Forms Field Guide

The American Institute of Architects (AIA) publishes the most widely used standard contract forms in commercial construction. Three documents form the backbone of most projects.

### A101 -- Owner-Contractor Agreement

The A101 is the main agreement between the owner and general contractor. It establishes the deal: scope, price, time, and payment terms.

#### Key Clauses for Field Operations

| Article | Subject | What the Super Needs to Know |
|---------|---------|------------------------------|
| Art. 3 | Date of Commencement & Substantial Completion | Your schedule is contractually bound to these dates. Substantial Completion triggers retainage release, warranty periods, and liquidated damages cutoff. Know these dates cold. |
| Art. 4 | Contract Sum | The total price. Every dollar above this requires an approved change order. No verbal authorizations. |
| Art. 5 | Progress Payments | Pay application schedule (usually monthly), retainage percentage (typically 5-10%), and conditions for payment. The architect certifies payment -- you provide the supporting documentation. |
| Art. 6 | Dispute Resolution | Specifies whether disputes go to mediation, arbitration, or litigation. Check this BEFORE you have a dispute. |
| Art. 7 | Termination or Suspension | Owner can suspend work for convenience; contractor can stop work if payment is 7+ days late (after 7-day written notice). |
| Art. 8 | Miscellaneous | Insurance requirements, key personnel, governing law. |

**Field Impact:** The A101 sets the financial and time boundaries. When someone on site says "the owner told us to go ahead with the extra work," your response is: "Show me the signed change order or written authorization per Article 4."

#### Common Pitfalls
1. **Starting work before Notice to Proceed (NTP)** -- Work performed before NTP may not be compensable
2. **Missing Substantial Completion criteria** -- Review the definition; it is not "we think it is done" but rather "the owner can use it for its intended purpose"
3. **Retainage math errors** -- Track retainage held vs. retainage due on every pay application
4. **Liquidated damages ignorance** -- Know the daily LD rate; it starts accumulating the day after Substantial Completion deadline

### A201 -- General Conditions of the Contract for Construction

The A201 is the most important document for daily field operations. It contains the rules of engagement for how the project is built, administered, and disputes are resolved. Every superintendent should read Articles 3, 4, 7, 8, 9, 12, 14, and 15.

#### Article 1 -- General Provisions

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 1.1.1 | Contract Documents defined | Drawings, specs, A101, A201, addenda, modifications. All carry equal weight -- specs do not override drawings or vice versa. |
| 1.2 | Correlation of Documents | If something is shown on drawings but not in specs (or vice versa), contractor must provide it. This prevents "I did not see it in the specs" arguments. |
| 1.5 | Ownership of Documents | Drawings belong to the architect. You can use them for this project only. |

#### Article 2 -- Owner Responsibilities

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 2.2 | Evidence of Financial Arrangements | Contractor can request proof that the owner can pay. Use this if you suspect owner financial trouble. |
| 2.3 | Information and Services | Owner must provide surveys, legal descriptions, utility locations. If owner data is wrong and it causes delay or extra cost, that is an owner-caused issue. |

#### Article 3 -- Contractor Responsibilities

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 3.1.1 | General duty | Contractor shall perform work "consistent with the Contract Documents and reasonably inferable therefrom." The word "reasonably inferable" means you cannot claim ignorance of something obvious even if it is not explicitly shown. |
| 3.2 | Review of Documents | Contractor must review documents and report errors or inconsistencies. Failure to report a noticed error can shift responsibility to contractor. |
| 3.3 | Supervision and Construction Procedures | Contractor is solely responsible for means, methods, techniques, sequences, and procedures. The architect cannot tell you HOW to build -- only WHAT to build. |
| 3.4 | Labor and Materials | Contractor furnishes all labor, materials, equipment. Unless the contract says "Owner furnished," you provide it. |
| 3.5 | Warranty | Contractor warrants materials and workmanship free from defects and conforming to contract documents. This is not a time-limited warranty -- it covers the entire construction period. |
| 3.7 | Permits, Fees, Notices | Contractor obtains and pays for permits (unless contract says otherwise). You must comply with all codes regardless of what the drawings show. If code conflicts with drawings, notify the architect. |
| 3.9 | Superintendent | Contractor shall employ a competent superintendent who shall be present on site at all times work is being performed. The super represents the contractor in the field and is authorized to receive communications. |
| 3.10 | Contractor's Schedules | Must submit schedule promptly after contract execution and update regularly. Schedule must conform to contract time limits. |
| 3.12 | Shop Drawings and Submittals | Contractor reviews submittals for compliance before sending to architect. Architect review does not relieve contractor of responsibility for errors in submittals. |
| 3.18 | Indemnification | Contractor indemnifies owner and architect for claims arising from contractor's negligent acts or omissions. This is the key liability clause -- see Indemnification section below. |

#### Article 4 -- Architect's Role

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 4.2.1 | Administration | Architect administers the contract, visits site, keeps owner informed. Architect does NOT supervise construction -- that is the contractor's job. |
| 4.2.6 | Rejection of Work | Architect can reject work that does not conform to contract documents. This can happen at any time, even after you think the work is accepted. |
| 4.2.7 | Submittals | Architect reviews submittals for "limited purpose of checking for conformance with information given and the design concept." This is not a comprehensive check -- contractor retains responsibility. |
| 4.2.11-14 | Initial Decision Maker | Architect serves as the Initial Decision Maker (IDM) for claims and disputes. Claims must go through the architect before mediation or arbitration. |

#### Article 7 -- Changes in the Work

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 7.1 | General | Changes only by Change Order (signed by owner, contractor, architect), Construction Change Directive (CCD, signed by owner and architect), or minor change order (architect alone for changes not affecting cost or time). |
| 7.2 | Change Orders | Must be signed by all three parties. No verbal change orders. Period. |
| 7.3 | Construction Change Directives | Owner and architect can direct changes even without contractor agreement on cost/time. Contractor must proceed with the work. Cost determined later by: mutual agreement, unit prices, cost-plus, or architect's determination. |
| 7.4 | Minor Changes | Architect can order minor changes consistent with intent of contract documents, not involving cost or time adjustment. If you think a "minor change" actually affects cost or time, object in writing immediately. |

**FIELD CRITICAL:** If someone verbally directs you to do something different from the drawings, respond:
1. Acknowledge the request
2. State that it requires a written change directive or change order
3. Send written confirmation of what was requested (email is acceptable)
4. Do NOT proceed until you have written authorization unless the CCD process applies

#### Article 8 -- Time

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 8.1.1 | Time definitions | "Date of Commencement" starts the clock. Know this date. |
| 8.2.1 | Progress and Completion | Time limits are "of the essence." This legal phrase means deadlines are strict -- missing them is a material breach. |
| 8.3 | Delays and Extensions | If contractor is delayed by owner, architect, or separate contractor, contractor is entitled to time extension. BUT: contractor must submit a claim per Article 15 -- the extension is not automatic. |

#### Article 9 -- Payments and Completion

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 9.2 | Schedule of Values | Submit SOV before first pay application. Break it down enough to track progress meaningfully. Front-loading the SOV (overvaluing early work) is a common dispute trigger. |
| 9.3 | Applications for Payment | Monthly, per contract schedule. Include: SOV progress, stored materials, change orders. Architect certifies within 7 days. |
| 9.4 | Certificates for Payment | Architect certifies payment to owner. Certificate is NOT acceptance of the work. |
| 9.5 | Decisions to Withhold | Architect can withhold certification for: defective work, third-party claims, failure to pay subs, damage to owner or another contractor, reasonable evidence work cannot be completed for unpaid balance, persistent failure to carry out work. |
| 9.6 | Payment to Subcontractors | Contractor must pay subs within 7 days of receiving payment from owner. **This is a field issue** -- sub performance problems and payment disputes are directly connected. |
| 9.8 | Substantial Completion | Architect inspects and issues Certificate of Substantial Completion (AIA G704). This document: lists incomplete items (punch list), establishes responsibilities for maintenance/utilities/insurance, fixes time for completing punch list, triggers retainage release timeline. |
| 9.9 | Partial Occupancy | Owner can occupy part of the project before Substantial Completion with mutual consent. Triggers insurance and warranty questions -- get these in writing. |
| 9.10 | Final Completion and Payment | After punch list complete, contractor submits final pay application. Owner must pay within 30 days of architect's final certificate. |

#### Article 10 -- Protection of Persons and Property

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 10.1 | Safety Precautions | Contractor responsible for safety. This is non-delegable. Even if a sub causes the unsafe condition, you are responsible for site safety. |
| 10.2 | Safety of Persons and Property | Contractor must protect: workers, the public, adjacent property, existing structures. Includes providing barricades, signage, flagging. |
| 10.3 | Hazardous Materials | If contractor encounters hazardous materials not addressed in contract documents, STOP WORK in the affected area and immediately notify owner and architect in writing. |

#### Article 11 -- Insurance and Bonds

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 11.1 | Contractor's Insurance | Contractor carries CGL, auto, workers comp, umbrella. Limits as specified. Owner and architect listed as additional insured. |
| 11.2 | Owner's Insurance | Owner carries property insurance (Builder's Risk) covering full insurable value. This is typically replacement cost, all-risk coverage. |
| 11.3 | Waivers of Subrogation | Both parties waive subrogation rights against each other to the extent covered by insurance. This prevents the insurance company from suing the other party after paying a claim. |
| 11.4 | Bonds | If required, contractor furnishes performance and payment bonds per AIA A312. |

#### Article 12 -- Uncovering and Correction of Work

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 12.1 | Uncovering of Work | If work is covered contrary to architect's request, contractor uncovers at own cost. If architect did not specifically request to observe and work is found compliant, owner pays cost of uncovering and restoration. If non-compliant, contractor pays. |
| 12.2 | Correction of Work | Contractor corrects defective work at no cost to owner. Correction period is 1 year after Substantial Completion (not 1 year after Final Completion). |

#### Article 14 -- Termination or Suspension

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 14.1 | Termination by Contractor | Contractor can terminate if: work stopped for 30+ consecutive days due to court order, government act, or architect's failure to certify payment (not contractor's fault); or if owner fails to pay for 60+ days after due date. Requires 7-day written notice. |
| 14.2 | Termination by Owner for Cause | Owner can terminate if contractor: persistently fails to supply enough workers or materials, fails to pay subs, persistently disregards laws or contract requirements, or is otherwise guilty of substantial breach. Requires 7-day written notice and opportunity to cure. |
| 14.3 | Suspension by Owner | Owner can suspend work without cause upon 7-day written notice. Contractor entitled to extension and cost adjustment. |
| 14.4 | Termination by Owner for Convenience | Owner can terminate for any reason upon 7-day written notice. Contractor receives payment for work completed plus reasonable overhead and profit on work not performed. |

#### Article 15 -- Claims and Disputes

| Section | Subject | Field Relevance |
|---------|---------|-----------------|
| 15.1.1 | Definition | A Claim is a demand seeking adjustment of the contract sum, contract time, or other relief. Written. With supporting documentation. |
| 15.1.3 | Notice of Claims | **CRITICAL**: Claims must be initiated within 21 days after occurrence of the event giving rise to the claim. Missing this deadline can waive the claim entirely. |
| 15.1.4 | Continuing Contract Performance | Pending final resolution, contractor must continue performing work. You cannot stop work because of a pending claim. |
| 15.2 | Initial Decision | Claims go to the Initial Decision Maker (architect). IDM must render decision within 10 days. If IDM fails to act within 30 days, claim proceeds to mediation. |
| 15.3 | Mediation | Mandatory before arbitration or litigation. Per AAA Construction Industry Mediation Procedures (or other agreed rules). Mediation is non-binding -- a settlement attempt, not a decision. |
| 15.4 | Arbitration | If A101 selects arbitration, disputes resolved per AAA Construction Industry Arbitration Rules. Arbitration is binding and final. Arbitration must be demanded within the applicable statute of limitations. |

**THE 21-DAY RULE:** This is the single most important deadline in the A201 for field personnel. When something happens on your project that could be a claim (delay, extra work, differing site conditions, design error), you have 21 days to submit written notice. Mark it on your calendar. Set a reminder. Do not let this deadline pass.

### A401 -- Contractor-Subcontractor Agreement

The A401 governs the relationship between the general contractor and each subcontractor. It incorporates the A201 by reference, meaning subs are bound by the same rules.

#### Key Clauses for Field Operations

| Article | Subject | What the Super Needs to Know |
|---------|---------|------------------------------|
| Art. 2 | Mutual Rights and Responsibilities | Sub is bound by same obligations to contractor that contractor has to owner. This "flow-down" means every A201 requirement applies to subs. |
| Art. 4 | Contractor's Responsibilities | Contractor must provide sub with copies of contract documents relevant to sub's work. Sub should have all drawings and specs for their scope. |
| Art. 5 | Subcontractor's Responsibilities | Sub furnishes labor, materials, equipment for their scope. Sub coordinates with other subs. Sub is responsible for their own safety program. |
| Art. 6 | Changes | Changes to sub's work require Change Order or Construction Change Directive. Sub cannot perform changed work without written authorization. Sub must notify contractor of claims for additional cost or time within 21 days. |
| Art. 7 | Sub's Applications for Payment | Sub submits pay apps per schedule. Contractor pays sub within 7 days of receiving owner payment. Retainage per contract terms. |
| Art. 8 | Progress Schedule | Sub must prepare schedule and update regularly. Sub must coordinate with master schedule. |
| Art. 9 | Sub's Recourse | If contractor does not pay within 7 days of receiving owner payment (and not due to sub's fault), sub can demand written explanation. If not resolved, sub can stop work after 7-day notice. |
| Art. 11 | Disputes | Claims between contractor and sub follow same mediation/arbitration process as A201. |
| Art. 12 | Termination | Contractor can terminate sub for cause if sub: fails to supply adequate workforce, fails to make payments to their own subs/suppliers, disregards laws or codes, fails to prosecute work, or is otherwise guilty of substantial breach. Requires 7-day notice and 7-day cure period. |

**Field Impact of A401:** When you are managing subs on site, you are enforcing the A401. When a sub is underperforming, the documentation you create is the foundation for any cure notice or termination. Your daily reports, emails, photos, and meeting minutes are the record.

---

## ConsensusDocs & EJCDC Comparison

Most superintendents learn on AIA contracts, but two other standard form families show up regularly: ConsensusDocs and EJCDC. Knowing where they differ from AIA prevents surprises.

### ConsensusDocs -- Key Differences from AIA

ConsensusDocs are developed by a coalition of 40+ construction industry organizations (AGC, ASA, DBIA, etc.). They are considered more balanced between owner and contractor than AIA documents.

| Topic | AIA A201 Approach | ConsensusDocs 200 Approach | Field Impact |
|-------|-------------------|---------------------------|--------------|
| **Document Ownership** | Architect owns drawings | Project team shares documents | Less restrictive on contractor use of drawings |
| **Differing Site Conditions** | Contractor bears risk unless Type I (differs from contract docs) or Type II (unusual, differs from known conditions) | Similar to AIA but with clearer language on what constitutes a differing condition | ConsensusDocs may give contractor slightly more protection on unforeseen conditions |
| **Consequential Damages** | Mutual waiver of consequential damages | Mutual waiver with clearer definition of what is consequential | Similar practical effect, but ConsensusDocs defines it more clearly |
| **Claims Notice** | 21 days after occurrence | 14 days after occurrence | **SHORTER DEADLINE** -- if your project uses ConsensusDocs, you have LESS time to file notice |
| **Dispute Resolution** | IDM (architect) first, then mediation, then arbitration | Direct negotiation first, then mediation, then arbitration | No architect as initial decision maker -- disputes go straight to party negotiation |
| **Owner Payment** | Owner must pay contractor, who then pays subs | Similar, but stronger "pay if paid" vs "pay when paid" language | Check the specific clause -- some ConsensusDocs versions provide stronger sub payment protection |
| **Termination for Convenience** | Owner can terminate for convenience with 7-day notice | Similar, but may include a profit component on unperformed work | Contractor may receive slightly better compensation for convenience termination |
| **Schedule** | Basic schedule requirement | More detailed CPM scheduling requirements | More administrative burden but better schedule documentation |

### EJCDC -- Key Differences from AIA

The Engineers Joint Contract Documents Committee (EJCDC) documents are common on heavy civil, infrastructure, and public works projects. They are used when an engineer (not an architect) is the lead designer.

| Topic | AIA A201 Approach | EJCDC C-700 Approach | Field Impact |
|-------|-------------------|---------------------|--------------|
| **Lead Designer** | Architect | Engineer | Communication flow goes through engineer, not architect |
| **Differing Site Conditions** | Two types recognized | Clearer enumeration of subsurface/physical conditions | Better protection for contractor on heavy civil with subsurface unknowns |
| **Unit Price Work** | Addressed briefly | Extensive unit price provisions with quantity variation clauses | Common on civil work -- know the quantity variation thresholds (typically +/- 15-25%) |
| **Claims Notice** | 21 days | 30 days (in some editions) | **LONGER DEADLINE** -- but verify your specific edition |
| **Substantial Completion** | Architect determines | Engineer recommends, owner decides | Slightly different process -- owner has more direct say |
| **Hazardous Materials** | Stop work, notify owner | More detailed hazardous waste procedures | More prescriptive requirements for environmental issues common on civil projects |
| **Progress Payments** | Monthly with architect certification | Monthly with engineer recommendation and owner approval | Two-step payment process instead of one |
| **Dispute Resolution** | IDM, mediation, arbitration | Engineer initial decision, mediation, then option for arbitration or litigation | Engineer plays a similar role to AIA architect as IDM |

### What Catches Superintendents Off Guard

1. **Claims notice deadlines vary** -- AIA is 21 days, ConsensusDocs is 14 days, EJCDC can be 30 days. Check YOUR contract.
2. **No architect as IDM in ConsensusDocs** -- You cannot send claims to the architect for initial decision. Negotiate directly.
3. **Unit price adjustments in EJCDC** -- Civil projects with unit pricing have automatic adjustment triggers. Track actual quantities against estimated quantities closely.
4. **Scheduling requirements** -- ConsensusDocs and EJCDC may require more detailed CPM schedule submissions than you are used to with AIA.
5. **Payment timelines differ** -- The number of days from pay app submission to payment varies. Know your contract's specific timeline.

---

## Bond Types & Requirements

Bonds are three-party agreements: the **principal** (contractor or sub), the **obligee** (owner or GC), and the **surety** (bonding company). The surety guarantees that the principal will perform its obligations.

### Bond Type Comparison

| Bond Type | Typical Amount | Who Requires It | What It Protects | When It Applies |
|-----------|---------------|-----------------|------------------|-----------------|
| **Bid Bond** | 5-10% of bid amount | Owner | Owner against contractor withdrawing bid after submission | Pre-award only |
| **Performance Bond** | 100% of contract value | Owner (or GC for subs) | Completion of the work per contract documents | Duration of contract + warranty period |
| **Payment Bond** | 100% of contract value | Owner (or GC for subs) | Payment to subs, suppliers, and laborers | Duration of contract |
| **Maintenance Bond** | 10-25% of contract value | Owner | Correction of defective work during warranty period | Warranty period (typically 1-2 years) |
| **Supply Bond** | 100% of supply contract | Contractor or Owner | Material delivery per supply agreement | Duration of supply contract |
| **Subdivision Bond** | Varies by jurisdiction | Municipality | Completion of public improvements (roads, utilities, sidewalks) | Until municipal acceptance |

### Bid Bonds -- Pre-Award Protection

**What they protect:** If a contractor submits the low bid and then refuses to enter the contract, the bid bond covers the difference between the low bid and the next acceptable bid (up to the bond amount).

**Typical amount:** 5% to 10% of the bid price.

**Field relevance for superintendents:** Minimal -- bid bonds are a pre-construction issue. But understand that your company's bonding capacity is a finite resource. Every bonded project reduces available capacity.

**Bonding capacity basics:**
- Bonding companies look at: working capital, net worth, work on hand, experience, and track record
- Typical aggregate capacity: 10x net worth (rough rule of thumb)
- Single project limit: usually 1/3 to 1/2 of aggregate capacity
- Slow pay apps, cost overruns, and claims eat into bonding capacity

### Performance Bonds -- Completion Guarantee

**What they protect:** If the contractor defaults (fails to complete the work), the surety must either:
1. Complete the work themselves (hiring a completion contractor)
2. Pay the obligee the cost to complete (up to bond amount)
3. Tender a new contractor to complete the work
4. Arrange financing to help the contractor complete

**Key provisions:**
- Bond amount is typically 100% of the contract value
- Bond follows contract modifications (change orders increase bond obligation)
- Surety has right to investigate before acting -- they do not pay automatically
- Obligee must give surety written notice of default
- Surety typically has 30-60 days to respond after notice

**Performance bond claim process:**
1. Contractor fails to perform
2. Owner sends written notice to contractor (per contract cure provisions)
3. If contractor fails to cure, owner declares contractor in default
4. Owner sends written notice of default to surety (with copies of all default documentation)
5. Surety investigates (typically 30-45 days)
6. Surety elects remedy: complete, pay, tender, or finance
7. If surety denies claim, litigation may follow

**What the super needs to know:** Your documentation of contractor or sub performance failures is the evidence used in a bond claim. Daily reports, photos, emails, and meeting minutes documenting the default are critical. Without contemporaneous documentation, the surety will deny the claim.

### Payment Bonds -- Protecting the Payment Chain

**What they protect:** Payment to subcontractors, sub-subcontractors, suppliers, and laborers who are not paid by the contractor.

**Federal projects -- Miller Act (40 U.S.C. 3131-3134):**
- Required on ALL federal construction projects over $35,000
- Performance and payment bonds both required
- Payment bond covers subs, suppliers, and laborers
- First-tier subs can make claim directly
- Second-tier subs/suppliers must give 90-day written notice to the contractor
- Claim must be filed within 1 year of last furnishing labor/materials

**State projects -- Little Miller Acts:**
- Most states have versions of the Miller Act for state/local public projects
- Thresholds vary by state ($5,000 to $100,000+)
- Notice and filing deadlines vary -- check your state statute
- Some states extend to private projects when bonds are required

**Private projects:**
- Payment bonds not required by law on private projects
- Owner or lender may require as a condition of the contract
- Bond provides alternative to mechanics lien rights on private projects
- Many payment bonds exclude suppliers more than two tiers removed from the principal

**Payment bond claim process:**
1. Claimant (sub/supplier) is not paid
2. Claimant sends written notice to the surety (and principal)
3. First-tier claimants: no preliminary notice required (federal Miller Act)
4. Second-tier claimants: must send 90-day notice (federal) or per state requirements
5. Claimant files suit on bond within deadline (1 year federal, varies by state)
6. Surety investigates and pays valid claims or litigates

**What the super needs to know:**
- Track sub payment status at every pay application cycle
- If a sub's suppliers or workers complain about non-payment, this is a red flag for payment bond exposure
- Lien waivers from subs should flow through every pay cycle (see Mechanics Lien section)
- If you are on a public project, there are no mechanics lien rights -- the payment bond is the sole remedy for unpaid parties

### Practical Bond Scenarios for Field Personnel

**Scenario 1: Sub is failing to perform**
- Before considering a performance bond claim against the sub, you must first exhaust the cure notice process under the subcontract
- Document everything: staffing shortages, missed milestones, quality deficiencies, failed inspections
- Send written cure notice per A401 (7-day notice, 7-day cure period)
- If sub fails to cure, terminate for cause and notify surety

**Scenario 2: Sub's workers approach you about non-payment**
- This is an early warning of sub financial distress
- Document the complaint (date, who, what they said)
- Notify your PM and corporate office immediately
- Check the sub's payment bond information
- Increase oversight of sub's pay applications and lien waiver submissions

**Scenario 3: Owner is not paying the GC**
- Review the GC's performance bond provisions
- After appropriate notice periods, GC may have right to stop work or terminate
- Subs affected by non-payment can pursue claims against the GC's payment bond

---

## Mechanics Lien Law

A mechanics lien is a legal claim against real property by someone who furnished labor, materials, or services to improve that property and was not paid. Mechanics liens are purely statutory -- the rules are set by state law and vary significantly by state.

### Why Superintendents Need to Understand Liens

1. **You manage the lien waiver process** -- Pay applications require lien waivers from subs and suppliers. If you collect the wrong type of waiver at the wrong time, the project is exposed.
2. **You verify work completion** -- Lien waivers are tied to pay apps. You certify the percentage complete. If you approve work that was not performed and a lien waiver is exchanged, you have created a problem.
3. **You see payment disputes first** -- When a sub's supplier threatens a lien, you are usually the first person on site to hear about it. Your response matters.
4. **Public projects have no lien rights** -- On public projects, the payment bond substitutes for lien rights. Know which you are on.

### Filing Deadline Ranges by State (General Guidance)

Deadlines vary significantly. These are general ranges -- always verify the specific statute in your project's state.

| Requirement | Typical Range | Notes |
|-------------|--------------|-------|
| **Preliminary Notice** | 20-45 days after first furnishing labor/materials | Required in ~30 states. Failure to send can extinguish lien rights entirely. |
| **Lien Filing Deadline (After Last Work)** | 60-120 days after last furnishing | Some states start from substantial completion, others from last day of work. |
| **Lien Filing Deadline (After Completion)** | 30-90 days after project completion | Defined differently by state (substantial completion, final completion, cessation of work). |
| **Enforcement Deadline (After Filing)** | 6-24 months after lien filing | Must file a lawsuit to enforce the lien within this period or it expires. |
| **Owner's Bond to Release Lien** | Available in most states | Owner can post a bond to remove the lien from property while dispute is resolved. |

**CRITICAL:** These ranges are general guidance only. A 1-day error on a lien deadline can completely extinguish the lien right. Consult counsel for your specific project jurisdiction.

### Preliminary Notice Requirements

Many states require potential lien claimants to send a preliminary notice within a set number of days after first furnishing labor or materials to the project. This is a "heads-up" to the owner and general contractor that a specific party is furnishing to the project.

**Who must send preliminary notice:**
- Subcontractors (in most states requiring preliminary notice)
- Sub-subcontractors
- Material suppliers
- Equipment rental companies

**Why it matters to superintendents:**
- You may receive preliminary notices at the job site
- Log all preliminary notices received (date, sender, amount claimed)
- Forward copies to your PM and accounting immediately
- Preliminary notices identify everyone who could potentially file a lien
- Compare against your sub list and approved supplier list

### Lien Waiver Types -- Detailed Explanation

There are four standard lien waiver types, and using the wrong one at the wrong time is one of the most common mistakes in construction payment. Many states have statutory lien waiver forms -- using non-statutory forms in these states can make the waiver unenforceable.

#### 1. Conditional Waiver on Progress Payment

**When to use:** With each progress payment APPLICATION (before payment is received).

**What it means:** "I waive my lien rights for work through [date] IF AND ONLY IF I actually receive payment of $[amount]. If the check bounces or payment is not made, this waiver is void."

**Key characteristics:**
- Conditioned on actual receipt of payment
- Covers work through a specific date
- Does NOT cover retainage
- Becomes effective only when payment is actually received
- Safe to sign because it protects the signer if payment is not made

**Field use:** Collect this from every sub with every pay application. It is submitted as part of the pay app package. The sub signs it at the time of submitting their invoice.

#### 2. Unconditional Waiver on Progress Payment

**When to use:** AFTER payment has been received for a progress payment.

**What it means:** "I have been paid $[amount] for work through [date], and I unconditionally waive my lien rights for that work. This is effective immediately regardless of any other event."

**Key characteristics:**
- Effective immediately upon signing -- no conditions
- Should ONLY be signed after payment is actually in hand (check cleared, funds received)
- Covers work through a specific date
- Does NOT cover retainage
- **DANGER:** Signing this before receiving payment waives lien rights with no protection

**Field use:** Collect this from subs as proof of payment received. This is the "receipt" that confirms the prior conditional waiver is satisfied. Many GCs require the unconditional waiver from the previous month with the current month's conditional waiver.

#### 3. Conditional Waiver on Final Payment

**When to use:** With the final payment APPLICATION (before final payment is received).

**What it means:** "I waive ALL lien rights on this project -- including retainage -- IF AND ONLY IF I receive final payment of $[amount]."

**Key characteristics:**
- Conditioned on actual receipt of final payment
- Covers ALL work on the project (not just through a date)
- Includes retainage
- Becomes effective only when final payment is actually received
- Used only once, at the end of the project

**Field use:** Collect this from every sub with their final pay application. This must come in before you process the final payment.

#### 4. Unconditional Waiver on Final Payment

**When to use:** AFTER final payment has been received.

**What it means:** "I have been paid in full, including retainage, and I unconditionally waive ALL lien rights on this project. Effective immediately."

**Key characteristics:**
- Effective immediately upon signing -- no conditions
- Covers ALL work, ALL materials, ALL retainage
- Should ONLY be signed after final payment is actually in hand
- This is the final release -- there is no going back
- **DANGER:** Signing this before receiving final payment waives ALL lien rights permanently

**Field use:** Collect after final payment clears. This is the final document in the payment chain for each sub.

### Lien Waiver Collection Matrix

| Pay App Cycle | What You Collect From Sub | What Sub Should Have Received |
|---------------|---------------------------|-------------------------------|
| **Pay App #1** | Conditional Waiver on Progress Payment #1 | Nothing yet (first billing) |
| **Pay App #2** | Conditional Waiver on Progress Payment #2 + Unconditional Waiver on Progress Payment #1 | Payment for Pay App #1 |
| **Pay App #3** | Conditional Waiver on Progress Payment #3 + Unconditional Waiver on Progress Payment #2 | Payment for Pay App #2 |
| **Final Pay App** | Conditional Waiver on Final Payment + Unconditional Waiver on Progress Payment (last month) | Payment for previous pay app |
| **After Final Payment** | Unconditional Waiver on Final Payment | Final payment including retainage |

### Common Lien Waiver Mistakes

1. **Collecting unconditional waivers before payment is made** -- This is the most dangerous mistake. The sub waives rights before getting paid. If payment never comes, the sub has no lien rights.
2. **Not matching waiver amounts to pay app amounts** -- The dollar amount on the waiver must match the payment. Discrepancies create ambiguity.
3. **Accepting non-statutory forms in statutory states** -- If your state requires a specific waiver form, non-conforming forms may be unenforceable.
4. **Missing sub-tier waivers** -- First-tier sub waivers are not enough. You need waivers from their subs and suppliers too, especially for large scopes.
5. **Not tracking retainage separately** -- Progress waivers typically do not cover retainage. Track retainage waivers separately at final payment.
6. **Incomplete waiver packages** -- A single missing waiver in the pay app package can delay the entire payment cycle. Stay on top of collections.
7. **Letting subs submit waivers with "TBD" amounts** -- Every waiver must have a specific dollar amount.

---

## Insurance Requirements

Construction insurance is the financial safety net for the project. The superintendent's role is verification and compliance enforcement -- making sure every entity on site has the required coverage before they work.

### OCIP vs CCIP -- Owner-Controlled vs Contractor-Controlled Insurance Programs

On large projects ($50M+), the owner or contractor may purchase a "wrap-up" insurance program that covers all parties on the project under a single policy. This is more efficient and typically reduces total insurance cost by 10-20%.

| Feature | OCIP (Owner-Controlled) | CCIP (Contractor-Controlled) |
|---------|------------------------|------------------------------|
| **Who purchases** | Owner | General Contractor |
| **Who is covered** | Owner, GC, all enrolled subs | GC, all enrolled subs |
| **Premium funding** | Owner pays directly | GC pays, typically through contract sum |
| **Sub bid adjustments** | Subs deduct insurance cost from bids (typically 2-5% of labor cost) | Subs deduct insurance cost from bids |
| **Administration** | Owner's insurance broker | GC's insurance broker |
| **Enrollment required** | All subs must enroll | All subs must enroll |
| **Excluded parties** | Material suppliers, truckers, off-site fabricators (usually) | Same exclusions typically |
| **Claims management** | Owner's broker manages | GC's broker manages |
| **Safety requirements** | Owner sets safety standards | GC sets safety standards |
| **Project size threshold** | Typically $50M+ to be cost-effective | Typically $50M+ |

**What the super needs to know about wrap-ups:**
1. **Verify enrollment** -- Before a sub starts work, confirm they are enrolled in the wrap-up. Unenrolled subs are not covered.
2. **Maintain insurance deductions** -- Subs enrolled in the wrap-up have deducted their insurance costs from their bids. Verify this deduction was made.
3. **Report all incidents** -- Wrap-ups have specific incident reporting requirements. Report to the wrap-up administrator, not just your company's insurer.
4. **Safety program compliance** -- Wrap-ups typically impose stricter safety requirements. The wrap-up safety manual supersedes individual company safety programs for on-site operations.
5. **Post-project tail coverage** -- Wrap-ups include completed operations coverage for a period after project completion (typically 3-10 years). This covers claims arising from work performed during construction.

### General Liability Insurance (CGL)

**What it covers:** Third-party bodily injury, property damage, personal/advertising injury arising from operations. Does NOT cover the contractor's own workers (that is Workers Comp) or the contractor's own property.

**Typical minimum limits:**

| Coverage | Minimum Limit | Notes |
|----------|--------------|-------|
| Each Occurrence | $1,000,000 | Per event |
| General Aggregate | $2,000,000 | Total annual limit |
| Products/Completed Operations | $2,000,000 | Covers claims after project completion |
| Personal/Advertising Injury | $1,000,000 | Libel, slander, invasion of privacy |
| Damage to Rented Premises | $100,000 | Fire damage to rented premises |
| Medical Payments | $5,000 | No-fault medical for minor injuries |

**Additional insured requirements:**
- Owner must be listed as additional insured on contractor's CGL
- GC must be listed as additional insured on sub's CGL
- Additional insured status provides the additional insured with defense and indemnity under the named insured's policy
- Verify additional insured endorsement form (CG 20 10 or CG 20 37, or their equivalents)

### Builder's Risk Insurance

**What it covers:** Physical loss or damage to the project under construction, including materials stored on site and in transit.

**Key characteristics:**

| Feature | Details |
|---------|---------|
| **Who purchases** | Typically the owner (per AIA A201 Section 11.2) |
| **Coverage basis** | Replacement cost (preferred) vs. Actual Cash Value (less coverage due to depreciation) |
| **What is covered** | Buildings, structures, materials, equipment to be incorporated into the work |
| **What is NOT covered** | Contractor's tools and equipment, existing structures (unless endorsed), soft costs (unless endorsed) |
| **Deductible** | Varies ($5,000 - $100,000+); know who pays the deductible per contract |
| **Coverage form** | All-risk (covers everything except specific exclusions) vs. Named perils (covers only listed perils) |
| **Duration** | From project start through substantial completion or owner occupancy |

**Common Builder's Risk exclusions:**
- Faulty workmanship, design, or materials (the resulting damage may be covered, but the faulty work itself is not)
- Normal wear and weathering
- Earth movement, flood (require separate endorsements)
- Theft of materials not incorporated into the work (unless secured and endorsed)
- Testing and commissioning losses (unless endorsed)

**What the super needs to know:**
1. Report all property damage or theft immediately -- within 24 hours
2. Preserve the damaged conditions for the adjuster (photos, do not discard)
3. Secure the site to prevent further damage (this is a policy requirement)
4. Know the deductible amount and who is responsible per the contract
5. Builder's Risk claims can affect future premiums -- document circumstances thoroughly

### Workers Compensation Insurance

**What it covers:** Medical expenses, lost wages, rehabilitation, and death benefits for workers injured on the job. Required by law in all states except Texas (where it is optional but strongly encouraged).

**What the super verifies:**

| Check Item | What to Look For |
|------------|-----------------|
| **Coverage in effect** | Policy dates current, no lapses |
| **Correct state** | Policy covers the state where work is performed |
| **Experience Modification Rate (EMR)** | Typically required below 1.0 or 1.2; higher EMR = worse safety record |
| **Classification codes** | Correct NCCI codes for work being performed (misclassification affects premium and coverage) |
| **Monopolistic state rules** | Ohio, North Dakota, Washington, Wyoming have state-fund-only systems -- verify compliance |

**EMR (Experience Modification Rate) explained:**
- EMR of 1.0 = industry average for that classification
- EMR below 1.0 = better than average safety record (lower premium)
- EMR above 1.0 = worse than average safety record (higher premium)
- Many GCs require subs to have EMR below 1.0 or 1.2
- EMR is calculated based on 3 years of loss history, excluding the most recent year
- A single serious injury can spike EMR for 3+ years

### Professional Liability Insurance (Errors & Omissions)

**When required:** Design-build projects where the contractor has design responsibility, or when the contractor provides engineering services (value engineering, temporary works design, means-and-methods engineering).

**Typical limits:** $1,000,000 - $5,000,000 per claim, depending on project design value.

**Key difference from CGL:** Professional liability covers design errors and omissions. CGL covers construction operations. They are completely different policies with different insurers.

### COI Verification Checklist

When a subcontractor shows up on site, verify their Certificate of Insurance (COI) BEFORE they start work. Use this checklist:

- [ ] **COI is current** -- Policy effective dates cover the work period
- [ ] **Named insured matches sub entity** -- The entity name on the COI must match the subcontract. "ABC Plumbing LLC" is not the same as "ABC Plumbing Inc."
- [ ] **General Liability** -- Meets minimum limits per contract
- [ ] **Additional insured endorsement** -- Owner and GC listed as additional insured (not just certificate holder)
- [ ] **Workers Compensation** -- Coverage in effect for correct state, EMR acceptable
- [ ] **Auto Liability** -- If sub is driving vehicles on site or public roads for the project
- [ ] **Umbrella/Excess** -- If required by contract (typically $1M-$5M umbrella over CGL/auto/WC)
- [ ] **Professional Liability** -- If sub has any design responsibility (design-build mechanical, electrical engineering, etc.)
- [ ] **Waiver of Subrogation** -- Endorsement matching contract requirement
- [ ] **30-day cancellation notice** -- COI should state insurer will provide 30 days written notice of cancellation to certificate holder
- [ ] **Certificate holder** -- GC (and owner if required) listed as certificate holder
- [ ] **No exclusions for your project type** -- Some policies exclude specific operations (hot work, demolition, environmental). Verify no relevant exclusions.

**When to reverify:**
- At policy renewal (annual)
- Before each new phase of work
- After any gap in sub's site presence exceeding 30 days
- If you receive notice of policy cancellation or non-renewal
- After a significant claim or incident

---

## Indemnification & Additional Insured

Indemnification and additional insured status work together but are different things. Indemnification is a contractual obligation to reimburse another party for losses. Additional insured status provides insurance coverage under someone else's policy.

### Types of Indemnification Clauses

| Type | What It Means | Enforceability | Risk to Contractor |
|------|--------------|----------------|-------------------|
| **Broad Form** | Contractor indemnifies owner for ALL claims, even if 100% caused by owner's own negligence | Void/unenforceable in most states (anti-indemnity statutes) | Maximum -- contractor bears all risk |
| **Intermediate Form** | Contractor indemnifies owner for claims caused in whole OR IN PART by contractor's negligence | Enforceable in most states | High -- any contribution to the loss triggers full indemnity obligation in some jurisdictions |
| **Limited (Comparative Fault)** | Contractor indemnifies owner only to the extent of contractor's own negligence | Enforceable everywhere | Fair -- each party bears responsibility proportional to fault |

**AIA A201 Section 3.18 uses intermediate form indemnification:** Contractor indemnifies owner and architect for claims "caused in whole or in part by negligent acts or omissions of the Contractor." This means if the contractor is even 1% at fault, the indemnification obligation may be triggered.

**Anti-Indemnity Statutes:** Most states prohibit broad form indemnification in construction contracts. Some states also limit intermediate form. Check your state's anti-indemnity statute before relying on indemnification clauses.

**States with restrictive anti-indemnity laws (prohibit broad AND some intermediate forms):**
- California, Colorado, Connecticut, Florida, Georgia, Illinois, Louisiana, Maryland, Michigan, Minnesota, New York, Ohio, Oregon, Texas, Virginia, Washington (and others -- verify current law)

### Documentation Obligations for Field Personnel

Indemnification claims rely on proving who was at fault. As superintendent, your documentation determines the outcome:

1. **Daily reports must accurately describe conditions and activities** -- If an injury occurs, your daily report is the first document reviewed.
2. **Safety inspections with photos** -- Document hazards observed and corrective actions taken.
3. **Sub safety violations** -- Document in writing, not just verbal warnings. Include date, time, violation, who was notified, corrective action, and follow-up.
4. **Incident reports** -- Complete within 24 hours. Include: who, what, when, where, how, witnesses, conditions, equipment involved.
5. **Do not admit fault** -- After an incident, gather facts and report to your safety director and risk manager. Do not make statements about whose fault it was.

### How Additional Insured Status Works

When the GC is named as additional insured on a sub's CGL policy:
- If a claim arises from the sub's operations, the sub's insurer defends and indemnifies the GC
- The GC's own insurance is secondary (excess) over the sub's policy
- This reduces the GC's insurance costs and preserves the GC's loss history
- The sub's insurer provides defense counsel for the GC under the sub's policy

**Important limitation:** Additional insured coverage typically only applies to liability arising out of the named insured's (sub's) operations. If the claim is solely due to the GC's own negligence, the sub's policy may not respond.

---

## Dispute Resolution

Disputes are inevitable in construction. The key to successful resolution is **preserving your rights through timely written notice** and **maintaining comprehensive documentation** throughout the project.

### Notice Requirements -- The Most Important Thing

**Timely written notice is the foundation of all contract rights.** Without proper notice, claims can be waived entirely, regardless of their merit.

#### Notice Timeline Quick Reference

| Contract Form | Claims Notice Deadline | Notice Recipient | Required Content |
|---------------|----------------------|------------------|------------------|
| **AIA A201** | 21 days after occurrence | Architect (IDM) and other party | Written claim identifying: event, contract provisions, requested relief (time, money, or both) |
| **ConsensusDocs 200** | 14 days after occurrence | Other party directly | Written notice of claim with supporting documentation |
| **EJCDC C-700** | 30 days after occurrence (verify edition) | Engineer and other party | Written notice with facts, contract basis, and requested relief |
| **AIA A401 (Sub Claims)** | 21 days after occurrence | Contractor | Same as A201 -- flows down |

#### What Must Be in a Notice

Every contract notice should include:

1. **Date of notice**
2. **Project identification** (name, number, location)
3. **Contract reference** (document number, relevant article/section)
4. **Description of the event** giving rise to the claim
5. **Date the event occurred** (or was first discovered)
6. **Impact on cost** (quantified if possible, or "amount to be determined pending investigation")
7. **Impact on time** (quantified if possible, or "to be determined")
8. **Contract provisions** relied upon (specific article and section numbers)
9. **Relief requested** (time extension, additional compensation, or both)
10. **Statement of rights reserved** ("Contractor reserves all rights under the Contract Documents and applicable law")

#### Notice Delivery Methods

| Method | Acceptability | Documentation |
|--------|--------------|---------------|
| **Certified mail, return receipt** | Best -- creates independent proof of delivery | Keep the green card (return receipt) |
| **Email with read receipt** | Acceptable under most modern contracts | Save the read receipt; print and file |
| **Hand delivery with signed acknowledgment** | Good -- but must get signature | Keep the signed copy |
| **Regular mail** | Risky -- no proof of delivery | Send certified as backup |
| **Verbal** | NOT acceptable for contractual notice | Never rely on verbal notice alone |

### Initial Decision Maker (IDM) -- AIA A201

Under AIA A201, the architect serves as the Initial Decision Maker for claims between the owner and contractor.

**IDM Process:**
1. Claim submitted in writing to the IDM (architect) within 21 days
2. IDM may request additional supporting documentation
3. IDM renders initial decision within 10 days of receiving adequate information
4. If either party disagrees with the IDM's decision, they can request mediation
5. If IDM does not render a decision within 30 days, the claim proceeds directly to mediation
6. Pending resolution, contractor must continue performance (A201 Section 15.1.4)

### Mediation

Mediation is a non-binding, facilitated negotiation with a neutral third party (mediator). It is mandatory before arbitration under most AIA contracts.

**Mediation characteristics:**
- Non-binding -- neither party is forced to settle
- Confidential -- statements made in mediation cannot be used in subsequent arbitration or litigation
- Typically conducted per AAA Construction Industry Mediation Procedures
- Costs shared equally between parties (unless otherwise agreed)
- No formal rules of evidence
- Settlement rate: approximately 70-80% of construction mediations result in settlement

**Superintendent's role in mediation:**
- Provide organized project documentation (daily reports, photos, emails, meeting minutes)
- Be prepared to testify about field conditions and events
- Create a timeline of relevant events with supporting documents
- Be honest and factual -- credibility is your most valuable asset in dispute resolution

### Arbitration

Arbitration is a binding, private adjudication of the dispute by one or more arbitrators (typically retired judges or experienced construction attorneys). Under AIA A101, if the parties select arbitration, it is governed by the AAA Construction Industry Arbitration Rules.

**Arbitration characteristics:**
- Binding and final -- very limited grounds for appeal
- Arbitrator(s) selected by the parties from AAA panel
- More formal than mediation but less formal than court
- Rules of evidence are relaxed
- Discovery is limited compared to litigation
- Typical duration: 6-18 months from demand to award
- Arbitrator's fee: $500-$1,500+ per day per arbitrator
- AAA administrative fees based on claim amount

**Key differences from litigation:**
- No jury
- Limited discovery (fewer depositions, narrower document requests)
- Relaxed rules of evidence (hearsay may be admitted)
- Faster than litigation (typically)
- No right to appeal (except for narrow grounds like fraud, arbitrator misconduct)
- Consolidation of multiple parties is more difficult

### Litigation

When the contract does not include an arbitration clause, disputes are resolved through litigation in court.

**Litigation characteristics:**
- Takes place in state or federal court
- Full discovery (depositions, interrogatories, document requests, expert witnesses)
- Formal rules of evidence apply
- Jury trial available (in most cases)
- Right to appeal
- Duration: 1-3+ years from filing to trial
- Higher cost than arbitration (typically)
- Public record (not confidential)

### Dispute Resolution Escalation Path

```
Field Issue Identified
    |
    v
Document Everything (daily reports, photos, emails)
    |
    v
Written Notice to Other Party (within contract deadline)
    |
    v
Direct Negotiation (try to resolve at project level)
    |
    +---> Resolved? --> Document settlement, proceed
    |
    v (Not resolved)
Submit Claim to IDM (AIA) or Formal Claim Letter (ConsensusDocs/EJCDC)
    |
    v
IDM Decision (10 days) / Direct Response (varies)
    |
    +---> Accepted? --> Implement, proceed
    |
    v (Not accepted or no response within 30 days)
Mediation (mandatory under most AIA contracts)
    |
    +---> Settled? --> Execute settlement agreement, proceed
    |
    v (Not settled)
Arbitration (if contract selects) or Litigation (if no arbitration clause)
    |
    v
Binding Decision / Judgment
```

---

## Subcontractor Default Procedures

Subcontractor default is one of the most disruptive and expensive events on a construction project. The superintendent is the first line of defense -- early identification and proper documentation determine whether the GC can terminate for cause (cost borne by the sub/surety) or is stuck with a convenience termination (cost borne by the GC).

### Warning Signs of Sub Distress

Watch for these indicators and document them in daily reports when observed:

**Workforce Issues:**
- [ ] Declining crew sizes without explanation
- [ ] High turnover -- different workers every week
- [ ] Foreman removed or reassigned frequently
- [ ] Workers complaining about late paychecks
- [ ] Using day laborers instead of regular employees
- [ ] Key tradespeople (journeymen) replaced by apprentices or helpers

**Financial Red Flags:**
- [ ] Late pay app submissions
- [ ] Requests for early payment or increased payment frequency
- [ ] Suppliers delivering COD instead of on account
- [ ] Material deliveries slowing or stopping
- [ ] Sub-subcontractors or suppliers contacting GC about non-payment
- [ ] Preliminary lien notices from parties you have never heard of
- [ ] Equipment being repossessed from site

**Performance Indicators:**
- [ ] Falling behind schedule without recovery plan
- [ ] Increasing quality deficiencies and failed inspections
- [ ] Not attending project meetings
- [ ] Not responding to RFIs or submittals
- [ ] Not correcting punch list items or deficient work
- [ ] Missing coordination deadlines with other trades
- [ ] Safety violations increasing in frequency

**Communication Breakdown:**
- [ ] Not returning phone calls or emails
- [ ] Superintendent or foreman avoiding project meetings
- [ ] Evasive answers about schedule, staffing, or financial condition
- [ ] Promises to "catch up next week" repeated for multiple weeks
- [ ] Corporate office not responding to formal correspondence

### Escalation Procedure: Verbal Warning Through Termination

#### Step 1: Verbal Communication (Day 0)

**Action:** Pull the sub's foreman or superintendent aside. Discuss specific concerns. Give them a chance to explain and commit to a corrective action plan.

**Documentation:** Note the conversation in your daily report: date, time, who was present, what was discussed, what the sub committed to, follow-up date.

**Key phrases to use:**
- "We are concerned about [specific issue] on your scope"
- "What is your plan to address this?"
- "When can we expect to see improvement?"
- "I need to see [specific corrective action] by [date]"

#### Step 2: Written Warning Letter (Day 3-7)

**Trigger:** Sub has not improved after verbal communication, or issue is serious enough to warrant immediate written notice.

**Action:** Send a formal letter to the sub's project manager and corporate office identifying:
- Specific deficiencies observed (with dates, locations, details)
- Contract provisions being violated (reference specific articles)
- Expected corrective actions
- Deadline for correction
- Statement that failure to correct may result in further action per the contract

**Delivery:** Certified mail AND email to both the sub's on-site representative and corporate office.

**Documentation:** Keep copies of the letter, certified mail receipt, and email confirmation.

#### Step 3: Formal Cure Notice (Day 14-21)

**Trigger:** Written warning has not produced adequate improvement.

**Action:** Issue a formal Cure Notice per the subcontract. Under AIA A401 Article 12:

**AIA A401 Cure Notice Requirements:**
1. Written notice to the sub stating the specific basis for the proposed termination
2. Sub has **7 calendar days** from receipt of notice to commence and continue satisfactory cure
3. The cure must be "satisfactory" -- token effort does not count
4. Notice must identify the specific contract provisions being violated
5. Notice must be sent to the sub's registered business address (check the subcontract)

**What the cure notice must contain:**
- Project name, number, and subcontract reference
- Specific deficiencies (list each one with dates, contract references, and documentation)
- Statement that this constitutes formal notice of intent to terminate per [specific contract article]
- Requirement that sub commence cure within 7 calendar days
- Statement of what constitutes satisfactory cure (specific, measurable outcomes)
- Deadline for achieving satisfactory cure
- Statement that failure to cure will result in termination for cause and backcharging of all replacement costs
- cc: Sub's surety (if bonded), owner, architect

**CRITICAL:** The cure notice must go to the sub's corporate office at the address listed in the subcontract. Handing it to the sub's foreman on site may not satisfy contractual notice requirements.

#### Step 4: Terminate for Cause (Day 21-30)

**Trigger:** Sub has failed to cure within the cure period.

**Prerequisites before termination:**
- [ ] Verified that all notice requirements have been satisfied
- [ ] Confirmed cure period has expired
- [ ] Documented that sub's cure efforts were insufficient (specific evidence)
- [ ] Consulted with corporate/legal counsel
- [ ] Notified the sub's surety (if bonded)
- [ ] Identified replacement contractor(s)
- [ ] Prepared cost estimate for completion by replacement
- [ ] Notified the owner and architect
- [ ] Photographed and documented all work in place at termination date

**Termination notice must include:**
- Reference to the cure notice (date sent, delivery confirmation)
- Statement that sub has failed to cure
- Effective date of termination
- Demand that sub: remove equipment from site, secure their work areas, provide as-built documentation for work completed, submit final pay application for work completed and accepted
- Statement that GC will complete the work and back-charge all excess costs
- Reservation of all rights including bond claims and damages

#### Step 5: Replace and Document (Day 30+)

**Replacement sub procurement:**
1. Contact at least 3 qualified replacement subs for competitive bids
2. Provide replacement subs with: scope of remaining work, current conditions (walk the site), schedule requirements, contract terms
3. Select replacement based on: ability to mobilize quickly, qualifications, cost, schedule compliance
4. Document the replacement procurement process (shows good faith effort to mitigate costs)

**Back-charge documentation:**
- Total cost to complete by replacement sub
- Minus remaining unpaid subcontract balance for defaulted sub
- Equals net back-charge to defaulted sub (and surety)
- Include: mobilization costs, premium time/overtime required to recover schedule, additional GC supervision, material cost increases, extended general conditions due to delay
- Support every dollar with documentation: invoices, time sheets, material tickets, photos

### Surety Bond Claims Process After Sub Default

If the defaulted sub has a performance bond:

1. **Notify the surety** -- Written notice of default, copies of all cure notices, termination notice, and supporting documentation
2. **Surety investigation** -- Surety will investigate (30-60 days typically). They may:
   - Agree the default was proper and fund completion
   - Provide a replacement contractor of their choosing
   - Deny the claim (if they believe termination was improper)
   - Attempt to get the defaulted sub back on track (with surety oversight)
3. **GC cooperation** -- Cooperate with the surety's investigation. Provide all documentation requested. Allow surety access to the site.
4. **If surety funds completion** -- Surety typically pays the difference between the remaining subcontract balance and the actual cost to complete.
5. **If surety denies claim** -- GC may need to pursue litigation against both the sub and the surety.

**Key risk:** If the GC's termination is found to be improper (not properly documented, notice requirements not met, insufficient grounds for cause), the termination may be converted to a termination for convenience. In that case, the GC owes the sub for work completed plus lost profits on the remaining scope. This is why documentation and strict compliance with notice procedures is critical.

---

## Contract Administration Data Model

The following JSON schema defines the data model for tracking contract administration events. This integrates with the pay-application, change-order-tracker, delay-tracker, sub-performance, and cost-tracking skills.

### Contract Event Tracking Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ContractAdministrationLog",
  "description": "Tracks contract administration events for a construction project",
  "type": "object",
  "properties": {
    "project_id": {
      "type": "string",
      "description": "Unique project identifier"
    },
    "contract_type": {
      "type": "string",
      "enum": ["AIA", "ConsensusDocs", "EJCDC", "Custom"],
      "description": "Standard form family used for this project"
    },
    "contract_documents": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "document_id": { "type": "string" },
          "form_number": { "type": "string", "description": "e.g., A101-2017, A201-2017, A401-2017" },
          "execution_date": { "type": "string", "format": "date" },
          "parties": {
            "type": "array",
            "items": { "type": "string" }
          },
          "contract_sum": { "type": "number" },
          "substantial_completion_date": { "type": "string", "format": "date" },
          "liquidated_damages_rate": { "type": "number", "description": "Daily LD rate in dollars" },
          "retainage_percentage": { "type": "number" },
          "dispute_resolution_method": {
            "type": "string",
            "enum": ["arbitration", "litigation", "mediation_then_arbitration", "mediation_then_litigation"]
          }
        },
        "required": ["document_id", "form_number", "execution_date"]
      }
    },
    "notices": {
      "type": "array",
      "description": "All contractual notices sent or received",
      "items": {
        "type": "object",
        "properties": {
          "notice_id": { "type": "string", "pattern": "^NTC-[0-9]{3}$" },
          "date_sent": { "type": "string", "format": "date" },
          "date_received": { "type": "string", "format": "date" },
          "direction": {
            "type": "string",
            "enum": ["sent", "received"]
          },
          "notice_type": {
            "type": "string",
            "enum": [
              "claim_notice",
              "cure_notice",
              "termination_notice",
              "delay_notice",
              "change_notice",
              "insurance_deficiency",
              "stop_work",
              "suspension",
              "payment_demand",
              "lien_notice",
              "bond_claim",
              "general"
            ]
          },
          "from_party": { "type": "string" },
          "to_party": { "type": "string" },
          "subject": { "type": "string" },
          "contract_reference": { "type": "string", "description": "e.g., A201 Section 15.1.3" },
          "delivery_method": {
            "type": "string",
            "enum": ["certified_mail", "email", "hand_delivery", "regular_mail", "overnight_courier"]
          },
          "delivery_confirmation": { "type": "boolean" },
          "response_deadline": { "type": "string", "format": "date" },
          "response_received": { "type": "boolean" },
          "response_date": { "type": "string", "format": "date" },
          "linked_claim_id": { "type": "string" },
          "linked_co_id": { "type": "string" },
          "linked_delay_id": { "type": "string" },
          "attachments": {
            "type": "array",
            "items": { "type": "string" }
          },
          "notes": { "type": "string" }
        },
        "required": ["notice_id", "date_sent", "direction", "notice_type", "from_party", "to_party", "subject"]
      }
    },
    "lien_waivers": {
      "type": "array",
      "description": "Lien waiver tracking for all subs and suppliers",
      "items": {
        "type": "object",
        "properties": {
          "waiver_id": { "type": "string", "pattern": "^LW-[0-9]{4}$" },
          "sub_name": { "type": "string" },
          "waiver_type": {
            "type": "string",
            "enum": [
              "conditional_progress",
              "unconditional_progress",
              "conditional_final",
              "unconditional_final"
            ]
          },
          "pay_app_number": { "type": "integer" },
          "through_date": { "type": "string", "format": "date" },
          "amount": { "type": "number" },
          "date_received": { "type": "string", "format": "date" },
          "date_verified": { "type": "string", "format": "date" },
          "verified_by": { "type": "string" },
          "statutory_form": { "type": "boolean", "description": "Whether state-required statutory form was used" },
          "status": {
            "type": "string",
            "enum": ["pending", "received", "verified", "deficient", "missing"]
          },
          "deficiency_notes": { "type": "string" },
          "linked_pay_app_id": { "type": "string" }
        },
        "required": ["waiver_id", "sub_name", "waiver_type", "pay_app_number", "amount", "status"]
      }
    },
    "insurance_tracking": {
      "type": "array",
      "description": "Insurance certificate tracking for all parties",
      "items": {
        "type": "object",
        "properties": {
          "insurance_id": { "type": "string", "pattern": "^INS-[0-9]{3}$" },
          "entity_name": { "type": "string" },
          "entity_type": {
            "type": "string",
            "enum": ["subcontractor", "supplier", "consultant", "owner", "gc"]
          },
          "policy_type": {
            "type": "string",
            "enum": ["general_liability", "workers_comp", "auto", "umbrella", "professional_liability", "builders_risk", "pollution"]
          },
          "carrier": { "type": "string" },
          "policy_number": { "type": "string" },
          "effective_date": { "type": "string", "format": "date" },
          "expiration_date": { "type": "string", "format": "date" },
          "limits": {
            "type": "object",
            "properties": {
              "each_occurrence": { "type": "number" },
              "general_aggregate": { "type": "number" },
              "products_completed_ops": { "type": "number" }
            }
          },
          "additional_insured": { "type": "boolean" },
          "waiver_of_subrogation": { "type": "boolean" },
          "emr": { "type": "number", "description": "Experience Modification Rate (Workers Comp only)" },
          "coi_on_file": { "type": "boolean" },
          "coi_verified_date": { "type": "string", "format": "date" },
          "coi_verified_by": { "type": "string" },
          "status": {
            "type": "string",
            "enum": ["compliant", "expiring_soon", "expired", "deficient", "not_received"]
          },
          "deficiency_notes": { "type": "string" },
          "renewal_reminder_date": { "type": "string", "format": "date" }
        },
        "required": ["insurance_id", "entity_name", "entity_type", "policy_type", "expiration_date", "status"]
      }
    },
    "bonds": {
      "type": "array",
      "description": "Bond tracking for project and subcontractors",
      "items": {
        "type": "object",
        "properties": {
          "bond_id": { "type": "string", "pattern": "^BND-[0-9]{3}$" },
          "bond_type": {
            "type": "string",
            "enum": ["bid", "performance", "payment", "maintenance", "supply", "subdivision"]
          },
          "principal": { "type": "string", "description": "Contractor or sub providing the bond" },
          "obligee": { "type": "string", "description": "Party protected by the bond" },
          "surety": { "type": "string", "description": "Bonding company" },
          "bond_amount": { "type": "number" },
          "bond_number": { "type": "string" },
          "effective_date": { "type": "string", "format": "date" },
          "expiration_date": { "type": "string", "format": "date" },
          "status": {
            "type": "string",
            "enum": ["active", "released", "claimed", "in_dispute"]
          },
          "claim_filed": { "type": "boolean" },
          "claim_date": { "type": "string", "format": "date" },
          "claim_amount": { "type": "number" },
          "claim_status": {
            "type": "string",
            "enum": ["pending", "under_investigation", "approved", "denied", "settled"]
          },
          "notes": { "type": "string" }
        },
        "required": ["bond_id", "bond_type", "principal", "obligee", "surety", "bond_amount", "status"]
      }
    },
    "disputes": {
      "type": "array",
      "description": "Dispute and claims tracking",
      "items": {
        "type": "object",
        "properties": {
          "dispute_id": { "type": "string", "pattern": "^DSP-[0-9]{3}$" },
          "title": { "type": "string" },
          "parties": {
            "type": "array",
            "items": { "type": "string" }
          },
          "claim_amount": { "type": "number" },
          "time_impact_days": { "type": "integer" },
          "date_initiated": { "type": "string", "format": "date" },
          "notice_deadline": { "type": "string", "format": "date" },
          "notice_sent": { "type": "boolean" },
          "notice_id": { "type": "string" },
          "current_stage": {
            "type": "string",
            "enum": [
              "notice_sent",
              "idm_review",
              "direct_negotiation",
              "mediation_scheduled",
              "mediation_in_progress",
              "arbitration_demanded",
              "arbitration_in_progress",
              "litigation_filed",
              "settled",
              "resolved",
              "withdrawn"
            ]
          },
          "idm_decision_date": { "type": "string", "format": "date" },
          "idm_decision": { "type": "string" },
          "mediation_date": { "type": "string", "format": "date" },
          "mediation_outcome": {
            "type": "string",
            "enum": ["settled", "impasse", "scheduled", "not_yet_scheduled"]
          },
          "resolution_amount": { "type": "number" },
          "resolution_time_days": { "type": "integer" },
          "resolution_date": { "type": "string", "format": "date" },
          "linked_co_ids": {
            "type": "array",
            "items": { "type": "string" }
          },
          "linked_delay_ids": {
            "type": "array",
            "items": { "type": "string" }
          },
          "documentation_files": {
            "type": "array",
            "items": { "type": "string" }
          },
          "notes": { "type": "string" }
        },
        "required": ["dispute_id", "title", "parties", "date_initiated", "current_stage"]
      }
    },
    "sub_default_tracking": {
      "type": "array",
      "description": "Subcontractor default procedure tracking",
      "items": {
        "type": "object",
        "properties": {
          "default_id": { "type": "string", "pattern": "^DEF-[0-9]{3}$" },
          "sub_name": { "type": "string" },
          "subcontract_id": { "type": "string" },
          "current_stage": {
            "type": "string",
            "enum": [
              "monitoring",
              "verbal_warning",
              "written_warning",
              "cure_notice_issued",
              "cure_period_active",
              "cure_failed",
              "terminated_for_cause",
              "terminated_for_convenience",
              "replacement_procurement",
              "replacement_active",
              "backcharge_processing",
              "bond_claim_filed",
              "resolved",
              "cured"
            ]
          },
          "deficiencies": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "description": { "type": "string" },
                "date_observed": { "type": "string", "format": "date" },
                "contract_reference": { "type": "string" },
                "evidence": { "type": "array", "items": { "type": "string" } }
              }
            }
          },
          "verbal_warning_date": { "type": "string", "format": "date" },
          "written_warning_date": { "type": "string", "format": "date" },
          "written_warning_notice_id": { "type": "string" },
          "cure_notice_date": { "type": "string", "format": "date" },
          "cure_notice_id": { "type": "string" },
          "cure_deadline": { "type": "string", "format": "date" },
          "cure_status": {
            "type": "string",
            "enum": ["pending", "in_progress", "satisfactory", "unsatisfactory", "not_attempted"]
          },
          "termination_date": { "type": "string", "format": "date" },
          "termination_type": {
            "type": "string",
            "enum": ["for_cause", "for_convenience"]
          },
          "termination_notice_id": { "type": "string" },
          "replacement_sub": { "type": "string" },
          "replacement_contract_amount": { "type": "number" },
          "original_remaining_balance": { "type": "number" },
          "backcharge_amount": { "type": "number" },
          "bond_claim_filed": { "type": "boolean" },
          "bond_claim_amount": { "type": "number" },
          "bond_claim_status": {
            "type": "string",
            "enum": ["not_filed", "filed", "under_investigation", "approved", "denied", "settled"]
          },
          "notes": { "type": "string" }
        },
        "required": ["default_id", "sub_name", "current_stage"]
      }
    }
  },
  "required": ["project_id", "contract_type"]
}
```

### Schema Usage Notes

**Notice tracking:** Every notice sent or received must be logged with delivery confirmation. Set calendar reminders for response deadlines. Link notices to related claims, change orders, and delay events.

**Lien waiver tracking:** Integrate with the pay-application skill. Each pay application cycle should trigger a lien waiver collection check. Status must be updated as waivers are received, verified, and filed.

**Insurance tracking:** Set renewal reminders 60 days before expiration. Check COIs against the COI Verification Checklist. Flag any deficiencies immediately.

**Bond tracking:** Update bond status when claims are filed or resolved. Link to sub-default tracking when performance bonds are involved.

**Dispute tracking:** Maintain a complete chain from initial notice through resolution. Link to all supporting documentation, change orders, and delay events. Track deadlines rigorously.

**Sub default tracking:** Document every step of the escalation process. Link to notices, cure notices, and termination notices. Track replacement procurement and back-charge calculations.

---

## Integration with Other Skills

The contract-administration skill connects to multiple other ForemanOS skills because contract provisions govern nearly every aspect of field operations.

### pay-application

**Connection:** Lien waiver processing is a core part of every pay application cycle.

**Data flow:**
- Pay application submission triggers lien waiver collection from `lien_waivers` array
- Each pay app requires: conditional progress waiver (current month) + unconditional progress waiver (prior month)
- Final pay app requires: conditional final waiver + unconditional progress waiver (last month)
- Post-final payment requires: unconditional final waiver
- Missing or deficient waivers block payment certification

**Shared fields:** `pay_app_number`, `sub_name`, `amount`, `through_date`

### change-order-tracker

**Connection:** Change orders are contract modifications. Constructive changes (verbal directives, drawings that conflict with specs) require timely notice to preserve claim rights.

**Data flow:**
- Change order requests may generate `claim_notice` entries in `notices` array
- Disputed change orders escalate to the `disputes` tracking
- Notice deadlines from contract-administration apply to change order claims (21 days AIA, 14 days ConsensusDocs)
- Back-charges from sub defaults generate change order entries

**Shared fields:** `linked_co_id`, `claim_amount`, `time_impact_days`

### delay-tracker

**Connection:** Delay claims require timely written notice per the contract. The notice provisions in contract-administration define the deadlines and requirements for delay claims.

**Data flow:**
- Delay events from delay-tracker trigger `delay_notice` entries in `notices` array
- Notice deadline tracking ensures delay claims are filed within contractual time limits
- Delay claims that are not resolved at project level escalate to `disputes` tracking
- Dispute resolution outcomes update delay-tracker claim status

**Shared fields:** `linked_delay_id`, `time_impact_days`, `notice_deadline`

### sub-performance

**Connection:** Sub-performance monitoring feeds into the subcontractor default procedure. Performance scores and tracking from sub-performance provide the evidence base for cure notices and termination.

**Data flow:**
- Low performance scores in sub-performance trigger `monitoring` status in `sub_default_tracking`
- Continued poor performance escalates through the default procedure stages
- Sub-performance documentation (daily reports, quality records, schedule adherence) becomes evidence in cure notices
- Default outcomes (cure, termination, replacement) update sub-performance records

**Shared fields:** `sub_name`, `deficiencies`, `cure_status`

### cost-tracking

**Connection:** Back-charges from sub defaults, bond claims, dispute settlements, and insurance deductibles all flow through cost tracking.

**Data flow:**
- Sub default back-charges (`backcharge_amount`) feed into cost-tracking as cost events
- Dispute resolution amounts update the project cost forecast
- Insurance deductibles from Builder's Risk claims are tracked as costs
- Bond claim recoveries offset default costs in cost tracking

**Shared fields:** `backcharge_amount`, `resolution_amount`, `claim_amount`

### daily-report-format

**Connection:** Daily reports are the primary contemporaneous documentation used in contract claims, disputes, and sub defaults.

**Data flow:**
- Daily report entries documenting delays, deficiencies, and events become supporting evidence in `notices` and `disputes`
- Contract administration events (notices sent, meetings held, verbal warnings given) should be recorded in the daily report
- Daily weather observations support delay claims
- Workforce counts support sub-performance and default documentation

### safety-management

**Connection:** Insurance requirements (Workers Comp, CGL) and indemnification obligations connect directly to safety program compliance.

**Data flow:**
- EMR verification from insurance tracking informs safety risk assessment
- Safety incidents trigger incident reports that may become part of insurance claims or indemnification actions
- OCIP/CCIP enrollment status affects safety reporting requirements
- Sub safety violations documented through safety-management become evidence in default proceedings

### meeting-minutes

**Connection:** Meeting minutes document discussions about contract issues, disputes, change orders, and sub performance.

**Data flow:**
- Meeting minutes documenting contract discussions become supporting evidence in disputes
- Action items from meetings may trigger notice deadlines
- Sub performance discussions documented in meeting minutes support default proceedings
