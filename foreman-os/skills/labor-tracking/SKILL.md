---
name: labor-tracking
description: >
  Track per-worker and per-crew labor hours by trade, calculate labor productivity ratios (output per labor-hour), support certified payroll compliance, and feed EVM actual cost calculations. Provides daily headcount validation against daily report crew counts and weekly labor summaries. Triggers: "time card", "timecard", "labor hours", "crew hours", "headcount", "man-hours", "labor productivity", "certified payroll", "labor tracking", "labor report", "overtime", "labor cost", "crew size", "work hours", "time tracking".
version: 1.0.0
---

# Labor Tracking Skill for Foreman OS

## Overview

The **labor-tracking** skill provides comprehensive labor hour management and productivity analysis for construction projects. It enables daily labor data entry, crew-level summary tracking, worker classification management, and automated cross-validation against daily reports. The skill calculates labor productivity ratios, supports Davis-Bacon certified payroll compliance, and integrates with earned-value management (EVM) for actual cost (AC) calculations.

### Core Functions

- **Daily Labor Entry**: Log worker hours by trade, classification, and cost code
- **Crew Management**: Track crew composition, headcount, and work accomplished
- **Productivity Metrics**: Calculate output-per-labor-hour ratios and efficiency factors
- **Weekly Summaries**: Aggregate hours, costs, and trends by trade
- **Daily Report Validation**: Cross-check labor entries against crew counts in daily reports
- **Certified Payroll**: Generate Davis-Bacon WH-347 form data and prevailing wage tracking
- **Cost Integration**: Feed actual labor costs into EVM and project dashboard

---

## 1. Labor Entry Data Model

### Primary Labor Entry Schema (JSON)

```json
{
  "entry_id": "LAB-2026-02-19-001",
  "date": "2026-02-19",
  "worker_name": "John Smith",
  "trade": "Concrete",
  "employer": "W Principles",
  "classification": "journeyman",
  "hours_regular": 8.0,
  "hours_overtime": 2.0,
  "hours_double_time": 0.0,
  "work_description": "Footing excavation and prep, rebar layout",
  "location_grid": "X2-Y3",
  "cost_code": "03-1000-02",
  "cost_code_description": "Concrete Foundations - Labor",
  "prevailing_wage_classification": "Concrete Worker - Journeyman",
  "hourly_rate_base": 52.50,
  "hourly_rate_burdened": 78.75,
  "weather": "Clear, 42F",
  "notes": "Overtime for footing critical path acceleration",
  "certified_payroll_flag": true,
  "fringe_benefits_included": true,
  "timestamp": "2026-02-19T16:45:00Z"
}
```

### Field Definitions

| Field | Type | Notes |
|-------|------|-------|
| entry_id | String | Unique identifier (format: LAB-YYYY-MM-DD-###) |
| date | Date | Labor date (YYYY-MM-DD) |
| worker_name | String | Full name (required for payroll) |
| trade | String | Primary trade (Concrete, Steel, Framing, MEP, Finishes, Sitework, etc.) |
| employer | String | Subcontractor name or "Self-Perform" |
| classification | Enum | journeyman, apprentice, foreman, superintendent, laborer, operator, inspector |
| hours_regular | Decimal | Standard hours (40-hr base week) |
| hours_overtime | Decimal | Overtime hours (1.5x multiplier) |
| hours_double_time | Decimal | Double-time hours (2x multiplier, typically premium OT or holidays) |
| work_description | String | Detailed work performed (ties to daily report) |
| location_grid | String | Building location (X1-Y2, etc.) |
| cost_code | String | CSI division code (e.g., 03-1000-02 for concrete labor) |
| prevailing_wage_classification | String | Davis-Bacon classification (if applicable) |
| hourly_rate_base | Decimal | Base hourly rate (before burdened costs) |
| hourly_rate_burdened | Decimal | Fully loaded rate (base + fringe + overhead) |
| fringe_benefits_included | Boolean | Davis-Bacon fringe flag |
| certified_payroll_flag | Boolean | Include in WH-347 report |
| timestamp | ISO 8601 | System-generated entry time |

---

## 2. Crew Summary Model

### Crew-Level Aggregation (JSON)

```json
{
  "crew_id": "CRW-2026-02-19-CONCRETE-01",
  "date": "2026-02-19",
  "trade": "Concrete",
  "employer": "W Principles",
  "crew_size": 6,
  "foreman_name": "Mike Johnson",
  "foreman_classification": "foreman",
  "total_hours": 48.5,
  "total_hours_regular": 46.0,
  "total_hours_overtime": 2.5,
  "total_hours_double_time": 0.0,
  "labor_cost_base": 2541.00,
  "labor_cost_burdened": 3817.50,
  "work_accomplished": {
    "description": "Footing rebar layout and tie, stem wall formwork setup",
    "quantity": 145.0,
    "unit": "linear feet of footing rebar"
  },
  "productivity_ratio": {
    "output": 145.0,
    "labor_hours": 48.5,
    "ratio": 2.99,
    "ratio_unit": "LF rebar per labor-hour"
  },
  "benchmark_ratio": 3.25,
  "efficiency_factor": 0.92,
  "performance_rating": "Good",
  "weather_impacts": "None",
  "equipment_used": ["Excavator", "Compressor", "Circular saw"],
  "daily_report_reference": "DR-2026-02-19",
  "notes": "Crew ahead of schedule on footing prep",
  "timestamp": "2026-02-19T17:30:00Z"
}
```

### Crew Summary Fields

| Field | Type | Notes |
|-------|------|-------|
| crew_id | String | Unique crew identifier |
| trade | String | Primary trade discipline |
| crew_size | Integer | Number of workers on site today |
| foreman_name | String | Crew foreman/lead |
| total_hours | Decimal | Sum of all worker hours (including OT multipliers) |
| labor_cost_burdened | Decimal | Total crew cost (hours × burdened rate) |
| work_accomplished | Object | What was produced (description, quantity, unit) |
| productivity_ratio | Object | Output per labor-hour calculation |
| benchmark_ratio | Decimal | Target/standard for this trade |
| efficiency_factor | Decimal | Actual ÷ Benchmark (100% = on track) |
| daily_report_reference | String | Cross-link to daily report document |

---

## 3. Productivity Metrics

### Labor Productivity Ratio Calculation

**Formula:**
```
Productivity Ratio = Units of Output ÷ Total Labor-Hours

Labor Efficiency Factor = Actual Productivity Ratio ÷ Benchmark Ratio
```

### Benchmark Standards by Trade

| Trade | Output Unit | Benchmark Ratio | Basis | Notes |
|-------|------------|-----------------|-------|-------|
| Concrete (Footings) | Linear feet of footing | 3.25 LF/hr | Industry standard | Excavation, rebar, formwork, pour |
| Concrete (SOG) | Square feet poured | 120 SF/hr | Structural slab | Finishing included |
| Steel Erection | Tons hoisted | 2.5 T/hr | PEMB assembly | Includes bolting |
| CFS Framing | Studs installed | 15 studs/hr | Metal framing @ 16" OC | Interior partitions |
| Drywall | Square feet hung | 85 SF/hr | Hanging only | Finishing separate |
| MEP Rough-In | Linear feet of pipe/ductwork | 45 LF/hr | Combined MEP | Average across trades |
| Roofing | Square feet installed | 35 SF/hr | Panel install + fastening | Metal standing seam |
| Finishes | Square feet finished | 120 SF/hr | Paint + trim | Both walls and trim |

### Weekly Productivity Tracking

```json
{
  "week": "2026-02-17 to 2026-02-23",
  "trade": "Concrete",
  "entries": 5,
  "productivity_data": [
    {
      "date": "2026-02-19",
      "crew": "CRW-2026-02-19-CONCRETE-01",
      "ratio": 2.99,
      "benchmark": 3.25,
      "efficiency": 0.92
    },
    {
      "date": "2026-02-20",
      "crew": "CRW-2026-02-20-CONCRETE-01",
      "ratio": 3.18,
      "benchmark": 3.25,
      "efficiency": 0.98
    }
  ],
  "weekly_average_efficiency": 0.95,
  "trend": "steady",
  "forecast": "On track for weekly target"
}
```

### Earned Hours vs Actual Hours (Labor Efficiency)

```
Earned Hours = Standard Hours × Efficiency Factor
Labor Cost Variance = (Actual Hours - Earned Hours) × Burdened Rate

If Crew 1: 50 actual hours, 3.0 ratio actual vs 3.25 benchmark
  Earned Hours = 50 × (3.0 ÷ 3.25) = 46.15 hours
  Over-run = 3.85 labor-hours
  Cost Variance = 3.85 × $78.75 = $303.19 unfavorable
```

---

## 4. Weekly Labor Summary

### Labor Summary Report (JSON)

```json
{
  "report_id": "LAB-WEEKLY-2026-W08",
  "week": "2026-02-17 to 2026-02-23",
  "project": "MOSC",
  "phase": "Foundation / Sitework",
  "generated_date": "2026-02-23",
  "summary_by_trade": [
    {
      "trade": "Concrete",
      "total_workers": 8,
      "total_hours_regular": 280.0,
      "total_hours_overtime": 12.0,
      "total_hours_double_time": 0.0,
      "total_labor_hours": 292.0,
      "ot_percentage": 4.1,
      "labor_cost_base": 14560.00,
      "labor_cost_burdened": 21840.00,
      "budget_labor_hours": 300.0,
      "variance_hours": -8.0,
      "variance_cost": -630.00,
      "status": "Favorable"
    },
    {
      "trade": "Sitework / Excavation",
      "total_workers": 4,
      "total_hours_regular": 152.0,
      "total_hours_overtime": 8.0,
      "total_hours_double_time": 0.0,
      "total_labor_hours": 160.0,
      "ot_percentage": 5.0,
      "labor_cost_burdened": 12600.00,
      "budget_labor_hours": 160.0,
      "variance_hours": 0.0,
      "status": "On Budget"
    }
  ],
  "weekly_totals": {
    "total_workers_active": 12,
    "total_labor_hours": 452.0,
    "total_overtime_hours": 20.0,
    "total_ot_percentage": 4.4,
    "total_labor_cost_burdened": 34440.00,
    "budget_total_hours": 460.0,
    "budget_total_cost": 36225.00,
    "variance_hours": -8.0,
    "variance_cost": -1785.00,
    "variance_percentage": -4.9
  },
  "headcount_trend": {
    "monday": 12,
    "tuesday": 12,
    "wednesday": 11,
    "thursday": 12,
    "friday": 12,
    "average": 11.8,
    "previous_week_average": 9.5,
    "change_percentage": 24.2
  },
  "top_overtime_contributors": [
    {
      "worker_name": "Mike Johnson",
      "trade": "Concrete",
      "ot_hours": 8.0,
      "reason": "Critical path footing acceleration"
    },
    {
      "worker_name": "Jim Wilson",
      "trade": "Concrete",
      "ot_hours": 4.0,
      "reason": "Rebar tie-off completion"
    }
  ],
  "alerts": [
    {
      "level": "info",
      "message": "OT at 4.4% - within acceptable range"
    },
    {
      "level": "success",
      "message": "Headcount increased 24.2% - good mobilization progress"
    }
  ]
}
```

---

## 5. Daily Report Cross-Validation

### Validation Workflow

The labor-tracking skill automatically compares daily labor entries against crew counts reported in daily reports. This ensures consistency and flags discrepancies for investigation.

#### Validation Rules

```json
{
  "validation_rules": [
    {
      "rule_id": "VR-001",
      "name": "Crew Size Match",
      "logic": "Count of unique workers logged in labor entries == reported crew size in daily report",
      "tolerance": 0,
      "action": "Flag if mismatch"
    },
    {
      "rule_id": "VR-002",
      "name": "Trade Completeness",
      "logic": "All active trades in daily report must have labor entries",
      "tolerance": 0,
      "action": "Alert if trade missing"
    },
    {
      "rule_id": "VR-003",
      "name": "Overtime Reporting",
      "logic": "Overtime hours logged must match overtime note in daily report",
      "tolerance": 0.5,
      "action": "Flag for reconciliation if >0.5 hr difference"
    },
    {
      "rule_id": "VR-004",
      "name": "Headcount Trend",
      "logic": "Crew size drop >30% from previous week triggers alert",
      "tolerance": 30.0,
      "action": "Alert - verify reason for reduction"
    }
  ]
}
```

#### Daily Validation Report

```json
{
  "validation_report_id": "VAL-2026-02-19",
  "date": "2026-02-19",
  "daily_report_id": "DR-2026-02-19",
  "validation_status": "PASS_WITH_NOTES",
  "checks_performed": {
    "crew_size_match": {
      "status": "PASS",
      "daily_report_count": 6,
      "labor_entry_count": 6,
      "discrepancy": 0
    },
    "trade_completeness": {
      "status": "PASS",
      "trades_in_daily_report": ["Concrete", "Sitework"],
      "trades_with_labor_entries": ["Concrete", "Sitework"],
      "missing_trades": []
    },
    "overtime_verification": {
      "status": "PASS",
      "ot_hours_in_daily_report": 2.5,
      "ot_hours_in_labor_entries": 2.5,
      "discrepancy": 0.0
    },
    "cost_code_alignment": {
      "status": "PASS",
      "work_description_match": true
    }
  },
  "discrepancies": [],
  "notes": "All labor entries align with daily report. Foreman signed off on accuracy.",
  "reconciliation_status": "COMPLETE",
  "timestamp": "2026-02-19T18:00:00Z"
}
```

---

## 6. Certified Payroll Support (Davis-Bacon)

### WH-347 Form Data Preparation

For Davis-Bacon and prevailing wage projects, the labor-tracking skill generates Certified Payroll report (WH-347) data by trade and classification.

```json
{
  "certified_payroll_report": {
    "report_period": "2026-02-17 to 2026-02-23",
    "project": "MOSC Job #825021",
    "contractor": "W Principles",
    "certifying_officer": "Andrew Eberle, PM",
    "workers_covered": [
      {
        "worker_name": "John Smith",
        "trade": "Concrete Worker",
        "classification": "Journeyman",
        "prevailing_wage_rate": 52.50,
        "fringe_benefits": 26.25,
        "total_burdened_rate": 78.75,
        "hours_worked": 42.0,
        "hours_overtime": 2.0,
        "gross_wages": 2285.00,
        "fringe_paid": 1102.50,
        "certified": true
      },
      {
        "worker_name": "James Davis",
        "trade": "Rebar Worker",
        "classification": "Journeyman",
        "prevailing_wage_rate": 51.00,
        "fringe_benefits": 25.50,
        "total_burdened_rate": 76.50,
        "hours_worked": 40.0,
        "hours_overtime": 0.0,
        "gross_wages": 2040.00,
        "fringe_paid": 1020.00,
        "certified": true
      }
    ],
    "apprentice_ratio_check": {
      "journeyman_count": 8,
      "apprentice_count": 2,
      "ratio": "1:4",
      "required_ratio": "1:5 or better",
      "status": "COMPLIANT"
    },
    "summary": {
      "total_workers": 10,
      "total_hours": 280.0,
      "total_gross_wages": 14560.00,
      "total_fringe_paid": 7280.00,
      "total_burdened_cost": 21840.00
    },
    "certification_statement": "I certify that the above information is true and correct and that all workers employed on this project have been paid not less than the prevailing wage rates.",
    "signature": "[Digital signature field]",
    "date_signed": "2026-02-23"
  }
}
```

### Compliance Checks

- **Prevailing Wage Rates**: Verify hourly rates match or exceed DA schedule
- **Fringe Benefits**: Confirm fringe benefits paid separately or added to wages
- **Classification Compliance**: Journeymen, apprentices, and other classifications tracked
- **Apprentice Ratio**: Verify apprentice-to-journeyman ratio (typically 1:5)
- **Hours and Overtime**: Confirm all hours reported and overtime premium applied

---

## 7. Command: /labor

### Command Structure

The `/labor` command provides direct access to all labor tracking functions.

#### /labor log
**Purpose**: Enter daily labor entries for workers

**Syntax**:
```
/labor log
```

**Interactive Form**:
```
Labor Entry Form
==================
Date: [2026-02-19]
Worker Name: [____________________]
Trade: [Concrete ▼]
Employer: [W Principles ▼]
Classification: [Journeyman ▼]
Hours Regular: [8.0]
Hours OT (1.5x): [0.5]
Hours DT (2x): [0.0]
Work Description: [________________________________]
Location Grid: [X2-Y3]
Cost Code: [03-1000-02]
Hourly Rate (Base): [52.50]
Prevailing Wage Classification: [Concrete Worker - Journeyman]

[Submit] [Save Draft] [Cancel]
```

**Output**:
```
✓ Labor entry LAB-2026-02-19-001 created
  Worker: John Smith
  Trade: Concrete, Journeyman
  Hours: 8.0 reg + 0.5 OT = 8.75 total
  Cost: $455.63 (burdened)
```

---

#### /labor summary [week|month]
**Purpose**: Generate labor summary by time period

**Syntax**:
```
/labor summary week
/labor summary month
```

**Output**:
```
Weekly Labor Summary - W08 (2026-02-17 to 2026-02-23)
======================================================

By Trade:
  Concrete ............. 292 hours (4.1% OT) - $21,840 cost
  Sitework ............. 160 hours (5.0% OT) - $12,600 cost
  ─────────────────────────────────────────────────────
  TOTAL ................ 452 hours (4.4% OT) - $34,440 cost

Budget vs Actual:
  Budget: 460 hours | Actual: 452 hours | Variance: -8 hours (-1.7%) ✓

Headcount Trend:
  Mon 12 | Tue 12 | Wed 11 | Thu 12 | Fri 12 (Avg: 11.8, +24.2% vs last week)

Top OT Contributors:
  1. Mike Johnson (Concrete) ... 8.0 OT hours
  2. Jim Wilson (Concrete) ...... 4.0 OT hours
```

---

#### /labor productivity [trade]
**Purpose**: Display productivity metrics for a specific trade

**Syntax**:
```
/labor productivity concrete
/labor productivity steel
/labor productivity mep
```

**Output**:
```
Productivity Report - Concrete
==============================

This Week (W08):
  Average Ratio: 3.04 LF/hour
  Benchmark: 3.25 LF/hour
  Efficiency: 93.5% (GOOD)
  Trend: ↗ Improving

Daily Breakdown:
  Feb 19 ... 2.99 LF/hr (92% efficiency) - Footing rebar
  Feb 20 ... 3.18 LF/hr (98% efficiency) - Stem wall formwork
  Feb 21 ... 3.04 LF/hr (94% efficiency) - Footing pour

Forecast:
  If this week's rate continues, weekly total: 145 LF
  If achieving 100% efficiency: 156 LF
  Variance: 11 LF shortfall
```

---

#### /labor validate
**Purpose**: Cross-check labor entries against daily reports

**Syntax**:
```
/labor validate
/labor validate date 2026-02-19
/labor validate trade concrete
```

**Output**:
```
Daily Labor Validation - 2026-02-19
===================================

Status: ✓ PASS (All checks passed)

Crew Size:
  Daily Report: 6 workers
  Labor Entries: 6 workers
  Match: ✓ PASS

Trade Completeness:
  Reported Trades: Concrete, Sitework
  Labor Entries: Concrete ✓, Sitework ✓
  Match: ✓ PASS

Overtime Verification:
  Daily Report OT: 2.5 hours
  Labor Entries OT: 2.5 hours
  Match: ✓ PASS

Work Alignment:
  Footing rebar & stem wall formwork ... ✓ Matches description

No discrepancies found. All entries reconciled.
```

---

#### /labor payroll
**Purpose**: Generate certified payroll (WH-347) data for Davis-Bacon projects

**Syntax**:
```
/labor payroll week 2026-02-17
/labor payroll month february
/labor payroll export csv
```

**Output**:
```
Certified Payroll Report - W08 (2026-02-17 to 2026-02-23)
=========================================================

Report Period: 2026-02-17 to 2026-02-23
Project: Morehead One Senior Care (MOSC) - Job #825021
Contractor: W Principles

Workers Covered:
  John Smith ............ Concrete Worker (Journeyman) ... 42 hrs + 2 OT ... $2,285
  James Davis ........... Rebar Worker (Journeyman) ...... 40 hrs ......... $2,040
  [8 more workers listed]

Summary:
  Total Workers: 10
  Total Hours: 280.0
  Total Gross Wages: $14,560
  Total Fringe Paid: $7,280
  Total Burdened Cost: $21,840

Apprentice Ratio Check:
  Journeymen: 8 | Apprentices: 2
  Ratio: 1:4 (Required: 1:5) ✓ COMPLIANT

[Export to PDF] [Email to Payroll] [Copy to Clipboard]
```

---

#### /labor cost
**Purpose**: Labor cost analysis and variance reporting

**Syntax**:
```
/labor cost summary
/labor cost by-trade
/labor cost by-division
/labor cost forecast
```

**Output**:
```
Labor Cost Analysis - Project to Date
====================================

Cost Summary:
  Total Labor (Burdened): $156,430
  Budget Allocation: $175,000
  Variance: -$18,570 (Favorable, -10.6%)
  Status: ON TRACK ✓

By Trade:
  Concrete ............. $87,360 (55.8% of total) Budget: $95,000
  Sitework ............. $42,100 (26.9% of total) Budget: $50,000
  Preliminary Trades ... $26,970 (17.3% of total) Budget: $30,000

Cost per CSI Division:
  03 - Concrete ........ $87,360
  31 - Sitework ........ $42,100
  04 - Masonry ......... $0 (Not yet started)

Productivity-Based Variance (Earned Value):
  Actual Hours Worked: 452
  Earned Hours (at std productivity): 438
  Over-run: 14 hours ... Cost Impact: +$1,103 unfavorable

  Status: Minor productivity dip this week; trend is improving

Forecast (to Substantial Completion):
  Current Burn Rate: $1,247/day
  Days Remaining: 162 (to 07/29/26)
  Projected Final Labor Cost: $201,954
  Budget: $200,000
  Projected Variance: +$1,954 (Slightly unfavorable)
  Mitigation: Monitor productivity metrics weekly
```

---

## 8. Integration Points

### 1. Daily Report Format
**Integration**: Labor crew counts from daily reports auto-populate crew summary forms. Labor entries cross-checked against crew counts to identify missing trades or discrepancies.

```
Daily Report → Crew Counts → Labor Entry Validation
                           ↓
                    Alert if mismatch
```

### 2. Cost Tracking / Earned Value Management (EVM)
**Integration**: Labor hours × burdened rate = Actual Cost (AC) for cost tracking. Productivity ratios feed into Earned Value (EV) calculations. Productivity variance impacts cost variance analysis.

```
Labor Entry (hours, rate) → Actual Cost (AC)
Labor Productivity Ratio → Earned Value (EV)
AC - EV = Cost Variance
```

### 3. Sub-Performance Scoring
**Integration**: Labor efficiency and productivity metrics feed into subcontractor performance scorecards. Weekly efficiency ratios track whether subs are meeting productivity benchmarks.

```
Weekly Labor Summary → Sub Performance Score
  • Efficiency Factor: 93.5% (Good)
  • On-Time Delivery: Yes
  • Quality Rating: Excellent
  → Overall Performance: 94/100 (Excellent)
```

### 4. Pay Application Support
**Integration**: T&M billing backed by detailed labor hour records. Labor summary provides actuals for progress payment invoices.

```
Labor Entries → Weekly Summary → Pay Application
  Supports: T&M invoices with labor detail backup
```

### 5. Look-Ahead Planner
**Integration**: Historical labor productivity ratios inform resource planning for upcoming work windows. Labor headcount trend helps plan crew mobilization.

```
Past Productivity: 3.04 LF/hour (concrete)
  ↓
Upcoming Footing (500 LF)
  = 164 labor-hours required
  = 1.5 weeks for 6-person crew
  → Schedule impact: May need 8-person crew
```

### 6. Project Dashboard
**Integration**: Weekly labor utilization charts, productivity trends, and cost variance displayed in real-time dashboard.

```
Dashboard Widgets:
  • Labor Cost Burn (actual vs budget)
  • Headcount Trend (week-over-week)
  • Productivity Efficiency by Trade
  • OT Percentage and Alert Flags
```

---

## 9. Data Store Schema

### labor-data.json

The primary data store for all labor entries and crew summaries.

```json
{
  "project_id": "825021",
  "project_name": "MOSC",
  "version": "1.0",
  "last_updated": "2026-02-23T18:00:00Z",
  "labor_entries": [
    {
      "entry_id": "LAB-2026-02-19-001",
      "date": "2026-02-19",
      "worker_name": "John Smith",
      "trade": "Concrete",
      "employer": "W Principles",
      "classification": "journeyman",
      "hours_regular": 8.0,
      "hours_overtime": 0.5,
      "hours_double_time": 0.0,
      "work_description": "Footing excavation and rebar layout",
      "location_grid": "X2-Y3",
      "cost_code": "03-1000-02",
      "cost_code_description": "Concrete Foundations - Labor",
      "prevailing_wage_classification": "Concrete Worker - Journeyman",
      "hourly_rate_base": 52.50,
      "hourly_rate_burdened": 78.75,
      "fringe_benefits_included": true,
      "certified_payroll_flag": true,
      "weather": "Clear, 42F",
      "notes": "Accelerated rebar for critical path",
      "timestamp": "2026-02-19T16:45:00Z"
    }
  ],
  "crew_summaries": [
    {
      "crew_id": "CRW-2026-02-19-CONCRETE-01",
      "date": "2026-02-19",
      "trade": "Concrete",
      "employer": "W Principles",
      "crew_size": 6,
      "foreman_name": "Mike Johnson",
      "total_hours": 48.5,
      "total_hours_regular": 46.0,
      "total_hours_overtime": 2.5,
      "labor_cost_burdened": 3817.50,
      "work_accomplished": {
        "description": "Footing rebar and formwork",
        "quantity": 145.0,
        "unit": "LF"
      },
      "productivity_ratio": 2.99,
      "benchmark_ratio": 3.25,
      "efficiency_factor": 0.92,
      "daily_report_reference": "DR-2026-02-19",
      "timestamp": "2026-02-19T17:30:00Z"
    }
  ],
  "weekly_summaries": [
    {
      "week_id": "LAB-W08-2026",
      "week_start": "2026-02-17",
      "week_end": "2026-02-23",
      "total_entries": 45,
      "total_workers": 12,
      "total_labor_hours": 452.0,
      "total_overtime_hours": 20.0,
      "total_labor_cost_burdened": 34440.00,
      "budget_hours": 460.0,
      "variance_hours": -8.0,
      "variance_cost": -1785.00,
      "summary_by_trade": []
    }
  ],
  "productivity_benchmarks": [
    {
      "trade": "Concrete",
      "output_unit": "LF",
      "benchmark_ratio": 3.25,
      "source": "Industry standard",
      "last_reviewed": "2026-01-01"
    }
  ],
  "alerts": [
    {
      "alert_id": "ALT-2026-02-23-001",
      "date_created": "2026-02-23",
      "severity": "info",
      "category": "productivity",
      "message": "Concrete efficiency at 93.5% of benchmark - trending upward",
      "action_required": false
    }
  ]
}
```

---

## 10. Alert Thresholds

### Automated Alert Rules

| Alert | Threshold | Action | Notes |
|-------|-----------|--------|-------|
| OT Exceeds Limit | >15% of total hours | Warning | May indicate schedule pressure or staffing gaps |
| Crew Size Drop | >30% reduction week-over-week | Alert | Verify planned reduction or investigate delays |
| Productivity Below Benchmark | <80% efficiency | Alert | Review crew performance and work conditions |
| Missing Labor Entries | Trade active in daily report but no labor entries | Error | Foreman must provide entries or explanation |
| High Fringe Variance | >5% variance from prevailing wage rate | Alert | Verify Davis-Bacon compliance |
| Cost Overrun | >10% variance unfavorable vs budget | Alert | Analyze root cause and forecast impact |
| Apprentice Ratio Violation | <1:5 ratio on Davis-Bacon projects | Error | Adjust crew composition immediately |

### Example Alert Trigger

```
ALERT: Overtime Exceeds 15%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Week: 2026-02-17 to 2026-02-23
Overtime Percentage: 18.2% (83 OT hours of 455 total)
Threshold: 15%
Overage: +3.2 percentage points

Contributing Factors:
  • Concrete crew: 2.5 OT hours (footing acceleration)
  • Steel crew: 4.0 OT hours (erection delay due to weather)
  • Sitework: 1.5 OT hours (cleanup/grading)

Recommendation:
  Review schedule for week of 02-24. Consider adding crew
  on Monday if steel erection continues to slip.
  Current forecast: 12% OT next week (within limits).
```

---

## 11. Best Practices for Construction Labor Tracking

### Daily Labor Entry Best Practices

1. **Timeliness**: Entries submitted within 24 hours of work date
2. **Accuracy**: Worker names and hours match time cards precisely
3. **Detailed Work Description**: Link labor hours to specific tasks and CSI divisions
4. **Weather Documentation**: Note weather conditions that impact productivity
5. **Prevailing Wage Compliance**: Ensure classifications match Davis-Bacon schedule

### Crew Management Best Practices

1. **Foreman Sign-Off**: Crew foreman reviews and validates daily entries
2. **Equipment Documentation**: Log equipment used each day (impacts productivity baseline)
3. **Site Conditions**: Document impacts (weather, access, material delays)
4. **Work Progress Quantification**: Always include measurable output (LF, SF, EA, etc.)
5. **Daily Report Reconciliation**: Cross-check labor entries against daily report before submission

### Productivity Tracking Best Practices

1. **Benchmark Validation**: Review industry benchmarks quarterly and adjust for project-specific conditions
2. **Weekly Trending**: Analyze weekly efficiency to spot trends early (improving vs declining)
3. **Crew Stability**: Track same crew over time to assess learning curve and crew cohesion
4. **Equipment Optimization**: Measure productivity impact of different tools/equipment
5. **Corrective Action**: When efficiency drops below 85%, investigate root cause within 48 hours

### Certified Payroll Best Practices

1. **Classification Accuracy**: Verify worker classifications match prevailing wage schedule monthly
2. **Fringe Benefit Tracking**: Maintain documentation of fringe benefit payments
3. **Apprentice Documentation**: Keep apprenticeship credentials on file and track ratios daily
4. **Wage Rate Compliance**: Subscribe to prevailing wage updates; implement rate changes immediately
5. **WH-347 Completeness**: Ensure all Davis-Bacon project weeks are reported within 7 days of week end

### Cost Integration Best Practices

1. **Burdened Rate Accuracy**: Update loaded rates quarterly with current overhead/fringe data
2. **Variance Analysis**: Review cost variance weekly and forecast final labor cost monthly
3. **Earned Value Tracking**: Calculate EV weekly to maintain cost and schedule forecasts
4. **Sub Cost Accountability**: Break out labor costs by subcontractor for performance tracking
5. **Budget Reconciliation**: True-up labor budget monthly with actual time cards and payroll

---

## 12. Integration with Other Foreman OS Skills

### Skill Dependencies and References

- **daily-report-format**: Crew counts and work descriptions feed labor validation
- **cost-tracking**: Labor hours drive actual cost (AC) for EVM
- **earned-value-management**: Productivity ratios calculate earned value
- **sub-performance**: Efficiency metrics feed performance scorecards
- **pay-application**: Labor summary supports T&M invoicing
- **look-ahead-planner**: Historical productivity informs resource planning
- **project-dashboard**: Labor charts and KPIs display in real-time dashboard

---

## 13. Implementation Notes

### Data Privacy and Security
- Labor entries contain worker names and hours; store securely
- Payroll data (WH-347) is confidential; restrict access to payroll and project managers
- PII (prevailing wage classifications) follows Davis-Bacon compliance requirements

### Calculation Engines
- **Total Hours Calculation**: Regular + (OT × 1.5) + (DT × 2.0) = Total Labor-Hours (for productivity ratio)
- **Labor Cost**: Hours × Burdened Rate = Cost
- **Productivity Ratio**: Output Quantity ÷ Total Labor-Hours = Ratio
- **Efficiency Factor**: Actual Ratio ÷ Benchmark Ratio = Efficiency (target: 100%)

### Migration and Onboarding
- Import labor entries from existing payroll systems (CSV/Excel format)
- Backfill productivity benchmarks from historical project data
- Train foremen on daily entry process; provide mobile-friendly form option
- Establish weekly reconciliation cadence with payroll department

---

## Triggers and Keywords

The labor-tracking skill responds to the following user inputs:

- "time card", "timecard"
- "labor hours", "crew hours", "man-hours"
- "headcount", "crew size"
- "labor productivity", "productivity ratio", "efficiency"
- "certified payroll", "WH-347", "Davis-Bacon"
- "labor tracking", "labor report", "labor summary"
- "overtime", "OT hours"
- "labor cost", "labor variance"
- "work hours", "time tracking"
- "crew performance", "labor efficiency"

---

## Example Workflows

### Workflow 1: Daily Labor Entry and Validation

```
1. Foreman logs labor entries for each worker
   /labor log
   → User enters worker data via interactive form
   → System creates labor entry records

2. System auto-validates against daily report
   /labor validate date 2026-02-19
   → Crew size check: PASS
   → Trade completeness: PASS
   → Overtime verification: PASS
   → Automatically reconciled

3. Weekly summary generated
   /labor summary week
   → Aggregates all entries
   → Calculates productivity metrics
   → Displays cost variance
   → Alerts for threshold violations
```

### Workflow 2: Davis-Bacon Certified Payroll Preparation

```
1. PM collects labor entries throughout week
2. Payroll specialist runs certification check
   /labor payroll week 2026-02-17
   → Verifies classifications
   → Checks apprentice ratios
   → Confirms fringe benefits
   → Generates WH-347 data export

3. Report signed by certifying officer
4. Copy retained with project files
5. Copy submitted to contracting officer (if required by contract)
```

### Workflow 3: Productivity Analysis and Corrective Action

```
1. Weekly productivity report generated automatically
   /labor productivity concrete
   → Actual: 2.95 LF/hour
   → Benchmark: 3.25 LF/hour
   → Efficiency: 91% (BELOW 85% threshold)
   → Alert triggered

2. PM investigates within 48 hours
   → Reviews work conditions, weather, staffing
   → Discusses with concrete foreman
   → Root cause identified: Missing equipment on site

3. Corrective action implemented
   → Equipment mobilized by following Monday
   → Revised forecast: 98% efficiency by end of week

4. Trend monitored weekly
   → Following week efficiency: 97% (Good)
   → Efficiency back on track
```

---

**End of SKILL.md**
