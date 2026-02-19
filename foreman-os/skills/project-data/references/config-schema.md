# Project Intelligence Config Schema

Full schema for the Foreman_OS multi-file data store. All files are stored in `folder_mapping.ai_output` (typically `AI - Project Brain/`).

---

## project-config.json

Master configuration — project identity, folder paths, document tracking, and change history.

```json
{
  "project_basics": {
    "project_name": "",
    "project_code": "",
    "project_number": "",
    "client": "",
    "superintendent": "",
    "architect": "",
    "project_manager": "",
    "engineers": {
      "structural": "",
      "mep": "",
      "civil": ""
    },
    "address": "",
    "building_type": "",
    "gross_sf": "",
    "stories": "",
    "logo_path": "",
    "claims_mode": false
  },

  "report_tracking": {
    "last_report_number": 0
  },

  "folder_mapping": {
    "daily_reports": "",
    "weekly_reports": "",
    "submittals": "",
    "rfis": "",
    "photos": "",
    "schedules": "",
    "safety": "",
    "subcontractors": "",
    "suppliers": "",
    "oac_reports": "",
    "change_orders": "",
    "ai_output": "",
    "spreadsheets": "",
    "bidding": "",
    "contracts": "",
    "sc_po_log": ""
  },

  "documents_loaded": [
    {
      "filename": "",
      "type": "",
      "discipline": "",
      "date_loaded": "",
      "sections_extracted": [],
      "coverage_notes": "",
      "confidence": ""
    }
  ],

  "version_history": [
    {
      "date": "",
      "source": "",
      "changes": [
        {
          "field": "",
          "old_value": "",
          "new_value": "",
          "reason": ""
        }
      ]
    }
  ]
}
```

### Project Basics

- `claims_mode` (boolean, default: false) — When true, the intake and report generation pipeline captures claims-grade detail: worker names and hours, equipment IDs, delivery ticket numbers, and delay timing. Enable with `/set-project claims-mode on`. Reports generated in claims mode are compatible with the claims-documentation skill's evidence requirements.

### Folder Mapping

The `folder_mapping` section tells the plugin where to save generated files. It maps output types to folder paths relative to the project root.

**Auto-detection:** During `/set-project`, the plugin scans the working directory for numbered folders matching the pattern `## - Name/` and auto-populates folder_mapping. The user confirms or adjusts.

**Standard W Principles mapping:**
| Key | Typical Folder | What Goes Here |
|-----|---------------|----------------|
| daily_reports | 11 - Daily Reports/ | Generated daily report .docx/.pdf files |
| weekly_reports | 12 - Weekly Reports/ (or 07 - OAC Reports/) | Weekly owner/PM reports |
| submittals | 06 - Submittals/ | Submittal transmittals and compliance docs |
| rfis | 09 - RFIs/ (or separate RFI folder) | RFI documents |
| photos | 10 - Project Photos/ | Site photos referenced in reports |
| schedules | 09 - Schedule/ | Lookahead schedules, CPM exports |
| safety | 14 - Safety/ | Safety documents, JHA, toolbox talks |
| subcontractors | 03 - Subcontractors/ | Sub contracts, contact info |
| suppliers | 04 - Suppliers/ | PO agreements, supplier docs |
| oac_reports | 07 - OAC Reports/ | OAC meeting minutes, owner reports |
| change_orders | 08 - Change Orders/ | Change order documents |
| ai_output | AI - Project Brain/ | Config files, dashboards, intelligence output |
| spreadsheets | 13 - Spreadsheets & Logs/ | SC/PO logs, tracking spreadsheets |
| bidding | 01 - Bidding Documents/ | Bid documents, proposals |
| contracts | 02 - Contract Documents/ | Contract documents |
| sc_po_log | (path to SC/PO Excel file) | Full path to the SC/PO Log spreadsheet |

**Usage rule:** Every command/skill that saves a file MUST read `folder_mapping` from `project-config.json` and route output to the correct subfolder. If folder_mapping is not populated (empty strings), fall back to the project root / AI - Project Brain/.

**sc_po_log:** This is a special entry — it stores the full path to the project's SC/PO Log spreadsheet (typically in the spreadsheets folder). The material-tracker skill reads this spreadsheet during project setup to auto-populate the procurement log.

---

## plans-spatial.json

Everything derived from plan sheets — spatial layout, quantities, drawing cross-references, and site utilities.

```json
{
  "grid_lines": {
    "columns": [],
    "rows": [],
    "spacing": "",
    "notes": ""
  },

  "building_areas": [
    {
      "name": "",
      "grids": "",
      "floors": "",
      "use": ""
    }
  ],

  "floor_levels": [
    {
      "name": "",
      "elevation": "",
      "description": ""
    }
  ],

  "room_schedule": [
    {
      "room_number": "",
      "room_name": "",
      "floor_level": "",
      "building_area": "",
      "department": ""
    }
  ],

  "site_layout": {
    "north_orientation": "",
    "access_points": [],
    "laydown_areas": [],
    "trailer_location": "",
    "dumpster_locations": [],
    "crane_locations": [],
    "haul_routes": [],
    "parking": {
      "construction": "",
      "permanent": ""
    }
  },

  "sheet_cross_references": {
    "drawing_index": [
      {
        "sheet_number": "A2.1",
        "title": "First Floor Plan",
        "discipline": "A",
        "type": "floor_plan|elevation|section|detail|schedule|cover|site",
        "revision": "",
        "date": ""
      }
    ],
    "detail_callouts": [
      {
        "id": "XREF-001",
        "source_sheet": "A2.1",
        "source_location": {"grid": "C-3", "zone": "plan_area"},
        "target_sheet": "A5.2",
        "target_detail": "3",
        "callout_type": "detail|section|elevation|interior_elevation|wall_type|enlarged_plan",
        "description": "Wall section at corridor",
        "linked_elements": ["room_107", "wall_type_2A"]
      }
    ],
    "schedule_references": [
      {
        "schedule_type": "door|window|finish|equipment|plumbing|electrical|room",
        "schedule_sheet": "A8.1",
        "plan_sheets": ["A2.1", "A2.2", "A2.3"],
        "item_count_schedule": 0,
        "item_count_plans": 0,
        "discrepancy": false,
        "discrepancy_notes": ""
      }
    ],
    "spec_references": [
      {
        "source_sheet": "S1.0",
        "spec_section": "03 30 00",
        "context": "Structural general notes — concrete requirements",
        "applies_to_sheets": ["S2.1", "S2.2", "S2.3", "S2.4"]
      }
    ],
    "assembly_chains": [
      {
        "id": "CHAIN-001",
        "description": "Footing F1 at Grid C-3",
        "links": [
          {"sheet": "S2.1", "element": "Footing F1 plan view", "data": "location, plan dimensions"},
          {"sheet": "S5.1", "element": "Detail 3 — Footing F1 section", "data": "depth, rebar, dowels"},
          {"sheet": "S1.0", "element": "Structural general notes", "data": "concrete PSI, rebar grade"},
          {"sheet": "A2.1", "element": "Room above footing", "data": "finish loads, occupancy"}
        ],
        "calculated_values": {
          "volume_cy": 0,
          "concrete_psi": "",
          "rebar_weight_lbs": 0,
          "source_priority": "dxf > visual > takeoff > text"
        }
      }
    ]
  },

  "quantities": {
    "rooms": [
      {
        "room_number": "107",
        "room_name": "Therapy",
        "area_sf": 0,
        "perimeter_lf": 0,
        "ceiling_height_ft": 0,
        "wall_sf": 0,
        "floor_level": "",
        "building_area": "",
        "source": "dxf|visual|takeoff|text",
        "source_sheet": "",
        "confidence": "high|medium|low",
        "validated": false
      }
    ],
    "walls": [
      {
        "wall_type": "2A",
        "description": "3-5/8\" Metal Stud, 5/8\" GWB ea. side",
        "total_lf": 0,
        "total_sf": 0,
        "height_ft": 0,
        "source": "dxf|visual|takeoff|text",
        "spec_section": "09 21 16",
        "fire_rating": ""
      }
    ],
    "concrete": [
      {
        "element": "Footing F1",
        "element_type": "footing|sog|wall|pier|grade_beam|curb",
        "count": 0,
        "length_ft": 0,
        "width_ft": 0,
        "depth_ft": 0,
        "volume_cy_each": 0,
        "volume_cy_total": 0,
        "area_sf": 0,
        "concrete_psi": "",
        "rebar_spec": "",
        "source": "dxf|visual|takeoff|text",
        "source_sheets": [],
        "assembly_chain_id": ""
      }
    ],
    "flooring": [
      {
        "material": "VCT",
        "spec_section": "09 65 00",
        "rooms": ["107", "108", "109"],
        "total_sf": 0,
        "source": "dxf|visual|takeoff|text"
      }
    ],
    "piping": [
      {
        "system": "domestic_water|sanitary|storm|fire_protection|natural_gas|medical_gas",
        "material": "",
        "size": "",
        "total_lf": 0,
        "source": "dxf|visual|takeoff|text",
        "spec_section": ""
      }
    ],
    "counts": [
      {
        "item": "Duplex Outlet",
        "csi_division": "26",
        "count": 0,
        "unit": "EA",
        "source": "visual|dxf|takeoff|text",
        "schedule_count": 0,
        "plan_count": 0,
        "discrepancy": false,
        "source_sheets": []
      }
    ],
    "aggregates": [
      {
        "csi_division": "03",
        "description": "Cast-in-Place Concrete",
        "items": [
          {"element": "Footings", "qty": 0, "unit": "CY"},
          {"element": "SOG", "qty": 0, "unit": "CY"},
          {"element": "Walls", "qty": 0, "unit": "CY"}
        ],
        "total_qty": 0,
        "unit": "CY"
      }
    ],
    "pemb": {
      "bay_areas_sf": [],
      "tributary_areas_per_column": [],
      "wall_panel_sf": 0,
      "roof_panel_sf": 0,
      "total_eave_lf": 0,
      "total_ridge_lf": 0,
      "gutter_lf": 0,
      "downspout_count": 0,
      "source": "dxf|visual|takeoff|text"
    },
    "data_sources": {
      "dxf_extracted": false,
      "visual_extracted": false,
      "takeoff_extracted": false,
      "text_extracted": false,
      "last_updated": "",
      "discrepancy_count": 0,
      "discrepancies": [
        {
          "item": "",
          "source_a": "",
          "value_a": "",
          "source_b": "",
          "value_b": "",
          "variance_pct": 0,
          "resolution": "",
          "resolved": false
        }
      ]
    }
  },

  "site_utilities": {
    "storm": [],
    "sanitary": [],
    "water": [],
    "fire": [],
    "gas": [],
    "electrical_ductbank": [],
    "telecom": []
  }
}
```

**Site Utilities Note:** Each utility run is stored as an object with: from, to, size, material, slope, invert_in, invert_out, rim_cover, length, and notes. See `document-intelligence/references/civil-deep-extraction.md` for full field definitions.

---

## specs-quality.json

Everything from specs and quality documents — requirements, thresholds, testing, safety, contract, and mix designs.

```json
{
  "spec_sections": [
    {
      "division": "",
      "section": "",
      "title": "",
      "key_req": "",
      "weather_thresholds": {
        "min_temp": "",
        "max_temp": "",
        "wind_limit": "",
        "moisture_restrictions": "",
        "cold_weather_measures": "",
        "hot_weather_measures": ""
      },
      "testing": {
        "frequency": "",
        "type": "",
        "agency": "",
        "break_schedule": ""
      },
      "hold_points": [],
      "witness_points": [],
      "tolerances": {},
      "submittal_required": false,
      "notes": ""
    }
  ],

  "key_materials": [
    {
      "material": "",
      "spec_section": "",
      "specification": "",
      "manufacturer": "",
      "product": "",
      "testing_required": ""
    }
  ],

  "weather_thresholds": [
    {
      "work_type": "",
      "min_temp": "",
      "max_temp": "",
      "max_wind": "",
      "moisture_ok": true,
      "spec_reference": "",
      "mitigation_measures": ""
    }
  ],

  "hold_points": [
    {
      "work_type": "",
      "inspection_name": "",
      "trigger": "",
      "inspector": "",
      "spec_reference": "",
      "notes": ""
    }
  ],

  "tolerances": [
    {
      "material_or_system": "",
      "measurement": "",
      "tolerance": "",
      "spec_reference": ""
    }
  ],

  "contract": {
    "ntp_date": "",
    "completion_date": "",
    "liquidated_damages": "",
    "working_hours": {
      "start": "",
      "end": "",
      "days": ""
    },
    "noise_restrictions": "",
    "holidays": [],
    "documentation_requirements": {
      "daily_report_required": true,
      "photo_requirements": "",
      "submission_timing": "",
      "distribution_list": [],
      "special_certifications": []
    },
    "special_requirements": []
  },

  "safety": {
    "fall_protection_zones": [
      {
        "location": "",
        "trigger_height": "",
        "protection_type": ""
      }
    ],
    "confined_spaces": [
      {
        "location": "",
        "permit_required": true,
        "hazards": ""
      }
    ],
    "hot_work_areas": [
      {
        "location": "",
        "permit_required": true,
        "fire_watch_duration": ""
      }
    ],
    "crane_exclusion_zones": [],
    "overhead_power_lines": [
      {
        "location": "",
        "voltage": "",
        "clearance_required": ""
      }
    ],
    "emergency_assembly_point": "",
    "competent_persons": [
      {
        "activity": "",
        "person": "",
        "certification": ""
      }
    ]
  },

  "swppp": {
    "permit_number": "",
    "bmps": [
      {
        "type": "",
        "location": "",
        "install_date": "",
        "status": ""
      }
    ],
    "inspection_triggers": {
      "rainfall_threshold": "",
      "frequency": "",
      "inspector": ""
    },
    "documentation_requirements": "",
    "corrective_action_timeline": ""
  },

  "geotechnical": {
    "bearing_capacity": "",
    "allowable_soil_pressure": "",
    "water_table_depth": "",
    "frost_depth": "",
    "unsuitable_soils": "",
    "fill_requirements": {
      "material": "",
      "compaction_density": "",
      "lift_thickness": "",
      "testing_frequency": ""
    },
    "dewatering_required": false,
    "dewatering_notes": "",
    "special_foundations": ""
  },

  "mix_designs": [
    {
      "mix_id": "",
      "producer": "",
      "design_fc": 0,
      "wc_ratio": 0.0,
      "slump_range": "",
      "air_content": "",
      "cement_type": "",
      "cement_content_lbs_cy": 0,
      "coarse_aggregate": "",
      "fine_aggregate": "",
      "admixtures": [],
      "unit_weight_pcf": 0,
      "max_aggregate_size": "",
      "assigned_elements": [],
      "spec_section": "",
      "submittal_id": "",
      "approval_status": "",
      "lab_report_date": "",
      "cold_weather_modification": "",
      "hot_weather_modification": ""
    }
  ]
}
```

---

## schedule.json

Schedule data, lookahead history, and activity-to-material mapping.

```json
{
  "current_phase": "",
  "percent_complete": "",
  "milestones": [
    {
      "name": "",
      "date": "",
      "status": "",
      "original_date": "",
      "notes": ""
    }
  ],
  "critical_path": [],
  "near_critical": [],
  "weather_sensitive_activities": [],
  "long_lead_items": [
    {
      "item": "",
      "supplier": "",
      "expected_delivery": "",
      "status": ""
    }
  ],
  "substantial_completion": "",
  "final_completion": "",
  "material_requirements_by_activity": [],
  "lookahead_history": [
    {
      "generated_date": "",
      "period_start": "",
      "period_end": "",
      "weeks": 3,
      "filename": "",
      "activity_count": 0,
      "subs_scheduled": []
    }
  ]
}
```

---

## directory.json

People, companies, and owner report archive.

```json
{
  "subcontractors": [
    {
      "name": "",
      "trade": "",
      "scope": "",
      "foreman": "",
      "phone": "",
      "email": "",
      "start_date": "",
      "end_date": "",
      "status": "",
      "notes": ""
    }
  ],

  "vendor_database": [
    {
      "id": "VENDOR-001",
      "company_name": "",
      "contact_person": "",
      "phone": "",
      "email": "",
      "website": "",
      "address": "",
      "capabilities": [],
      "certifications": [],
      "lead_time_typical": "",
      "materials_supplied": [],
      "spec_sections_served": [],
      "past_quotes": [
        {
          "date": "",
          "item": "",
          "amount": "",
          "notes": ""
        }
      ],
      "rating": "",
      "notes": ""
    }
  ],

  "owner_reports": [
    {
      "id": "WR-001",
      "week_ending": "",
      "generated_date": "",
      "pdf_filename": "",
      "daily_reports_included": [],
      "executive_summary": "",
      "schedule_status": "on_track|at_risk|behind|ahead",
      "percent_complete": "",
      "key_accomplishments": [],
      "upcoming_work": [],
      "active_issues": [],
      "weather_summary": "",
      "safety_summary": "",
      "inspection_summary": "",
      "photo_count": 0,
      "distribution_list": []
    }
  ]
}
```

---

## rfi-log.json

```json
{
  "rfi_log": [
    {
      "id": "RFI-001",
      "date_issued": "",
      "subject": "",
      "asking_party": "",
      "addressed_to": "",
      "drawing_references": [],
      "spec_references": [],
      "location": {
        "description": "",
        "building_area": "",
        "grid_lines": "",
        "floor_level": ""
      },
      "location_note": "For RFIs affecting multiple locations, use an array of location objects. Single-location RFIs can use a single object for backward compatibility.",
      "description": "",
      "urgency": "routine|urgent|critical",
      "status": "draft|issued|response_received|clarification_sent|resolved|void",
      "response_date": "",
      "response_text": "",
      "response_by": "",
      "schedule_impact": "none|minor|major",
      "schedule_impact_days": 0,
      "cost_impact": "",
      "related_submittals": [],
      "notes": ""
    }
  ]
}
```

---

## submittal-log.json

```json
{
  "submittal_log": [
    {
      "id": "SUB-001",
      "date_submitted": "",
      "spec_section": "",
      "spec_section_title": "",
      "item_description": "",
      "submitting_sub": "",
      "submitted_to": "",
      "product_name": "",
      "manufacturer": "",
      "model_number": "",
      "drawing_references": [],
      "submittal_type": "product_data|shop_drawings|samples|mix_designs|certifications|test_reports|closeout",
      "attachments": [],
      "status": "draft|submitted|under_review|approved|approved_as_noted|revise_and_resubmit|rejected|void",
      "review_comments": "",
      "reviewed_by": "",
      "review_date": "",
      "resubmission_of": "",
      "revision_number": 0,
      "reason_for_revision": "",
      "revision_comments_from_review": "",
      "compliance_matrix": [
        {
          "requirement": "",
          "spec_value": "",
          "submitted_value": "",
          "compliant": true,
          "notes": ""
        }
      ],
      "schedule_impact": "none|critical_path_blocked|lead_time_risk",
      "lead_time_weeks": 0,
      "related_rfis": [],
      "notes": ""
    }
  ]
}
```

---

## procurement-log.json

```json
{
  "procurement_log": [
    {
      "id": "PROC-001",
      "item": "",
      "spec_section": "",
      "spec_requirements": "",
      "category": "long_lead|standard|critical_path",
      "supplier": "",
      "supplier_contact": "",
      "supplier_phone": "",
      "supplier_email": "",
      "po_number": "",
      "po_date": "",
      "quantity_ordered": "",
      "unit_cost": "",
      "total_cost": "",
      "submittal_id": "",
      "submittal_status": "",
      "expected_delivery": "",
      "actual_delivery": "",
      "delivery_status": "not_ordered|ordered|in_production|shipped|delivered|partial|delayed|cancelled",
      "quantity_received": "",
      "condition_on_arrival": "",
      "storage_location": "",
      "verified_against_spec": false,
      "verification_notes": "",
      "verification_status": "pending|approved|conditional|rejected",
      "cert_status": "pending|partial|verified|waived",
      "certs_required": [],
      "certs_received": [],
      "schedule_activity_linked": "",
      "days_until_needed": 0,
      "lead_time_weeks": 0,
      "lead_time_notes": "",
      "notes": ""
    }
  ]
}
```

---

## change-order-log.json

```json
{
  "change_order_log": [
    {
      "id": "CO-001",
      "description": "",
      "originator": "owner|architect|field|sub",
      "originator_name": "",
      "date_submitted": "",
      "status": "draft|submitted|under_review|approved|rejected|void",
      "cost_estimate": "",
      "cost_approved": "",
      "schedule_impact_days": 0,
      "affected_spec_sections": [],
      "affected_subs": [],
      "linked_asis": [],
      "linked_rfis": [],
      "approved_by": "",
      "resolution_date": "",
      "notes": ""
    }
  ]
}
```

---

## inspection-log.json

Contains both inspection records and permit tracking.

```json
{
  "inspection_log": [
    {
      "id": "INSP-001",
      "type": "",
      "date_scheduled": "",
      "date_completed": "",
      "inspector": "",
      "inspector_company": "",
      "result": "scheduled|pass|fail|conditional|cancelled",
      "deficiencies": [],
      "re_inspection_required": false,
      "re_inspection_id": "",
      "linked_schedule_activity": "",
      "linked_hold_point": "",
      "linked_spec_section": "",
      "location": {
        "description": "",
        "room_number": "",
        "building_area": "",
        "grid_reference": "",
        "floor_level": ""
      },
      "photos": [],
      "notes": ""
    }
  ],

  "permit_log": [
    {
      "permit_id": "",
      "type": "",
      "issuing_authority": "",
      "issue_date": "",
      "expiration_date": "",
      "status": "",
      "linked_inspections": [],
      "notes": ""
    }
  ]
}
```

---

## meeting-log.json

```json
{
  "meeting_log": [
    {
      "id": "MTG-001",
      "type": "OAC|progress|safety|pre_install|coordination",
      "date": "",
      "time": "",
      "location": "",
      "attendees": [
        {
          "name": "",
          "company": "",
          "role": ""
        }
      ],
      "discussion_items": [
        {
          "topic": "",
          "summary": "",
          "decisions": [],
          "action_items": []
        }
      ],
      "action_items": [
        {
          "id": "AI-001",
          "description": "",
          "assignee": "",
          "assignee_company": "",
          "due_date": "",
          "status": "open|in_progress|closed|deferred",
          "linked_rfi": "",
          "linked_co": "",
          "linked_submittal": "",
          "created_meeting": "",
          "closed_meeting": "",
          "notes": ""
        }
      ],
      "previous_meeting_id": "",
      "notes": ""
    }
  ]
}
```

---

## punch-list.json

```json
{
  "punch_list": [
    {
      "id": "PUNCH-001",
      "location": {
        "room_number": "",
        "room_name": "",
        "building_area": "",
        "grid_reference": "",
        "floor_level": ""
      },
      "description": "",
      "trade": "",
      "responsible_sub": "",
      "date_identified": "",
      "date_completed": "",
      "photos": [],
      "status": "open|in_progress|completed|back_charge|disputed",
      "priority": "A|B|C",
      "identified_by": "",
      "completed_by": "",
      "back_charge_amount": "",
      "back_charge_sub": "",
      "punch_type": "pre_final|final",
      "notes": ""
    }
  ]
}
```

---

## Notes on Schema Usage

- **Empty strings** indicate fields that haven't been populated yet. Don't remove them — they serve as placeholders for future data.
- **Empty arrays** indicate lists that haven't been populated. Same rule — keep the structure.
- **Nested objects** with all empty fields should be kept in place. The structure guides extraction.
- **Status fields** on milestones and subs use: "complete", "in_progress", "upcoming", "active", "mobilized", "demobilized"
- **Date format**: Always ISO 8601 (YYYY-MM-DD) in the data store. Display format (MM/DD/YYYY) is handled by the report generation skill.

## Audit Gap Amendments

### Gap 8.1: RFI Location Multi-Location Support
The `rfi_log` location field now includes a note indicating that multiple locations can be captured as an array of location objects for RFIs affecting multiple areas. Single-location RFIs use a single object for backward compatibility.

### Gap 8.2: Procurement Lead Time Fields
The `procurement_log` now includes:
- **lead_time_weeks**: Captures the supplier's stated manufacturing/delivery lead time (numeric)
- **lead_time_notes**: Additional notes about lead time considerations
These fields are useful for future project planning and reorder timing analysis.

### Gap 8.3: Submittal Revision Tracking
The `submittal_log` now includes:
- **reason_for_revision**: Documents why resubmission was required (product non-conformance, documentation issue, etc.)
- **revision_comments_from_review**: Captures the reviewer's specific comments that prompted the resubmission

### Concrete Mix Designs (specs-quality.json)
The `mix_designs` array captures complete concrete mix design specifications including mix proportions, aggregate information, admixtures, design strength, slump, air content, assigned elements, submittal tracking, and weather-specific modifications. See `document-intelligence/references/concrete-mix-design-extraction.md` for full extraction reference.

### Site Utilities (plans-spatial.json)
The `site_utilities` object organizes utility runs by system type: storm, sanitary, water, fire, gas, electrical_ductbank, telecom. Each utility run has: from, to, size, material, slope, invert_in, invert_out, rim_cover, length, and notes. See `document-intelligence/references/civil-deep-extraction.md` for full field definitions.

### Permit Log (inspection-log.json)
The `permit_log` has standardized fields for permit tracking: permit_id, type, issuing_authority, issue_date, expiration_date, status, linked_inspections.
