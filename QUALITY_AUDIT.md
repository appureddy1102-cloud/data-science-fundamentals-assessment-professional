# Assessment coverage and quality audit

No external scoring rubric was provided; requirements below map to the user's stated objectives. Best practices are recommendations, not invented grading rules. Readiness: substantial and reproducible, but no score is guaranteed; Windows setup and evaluator acceptance remain unverified.

| Requirement | Evidence | Status | Remaining weakness | Corrective action |
|---|---|---|---|---|
| Requirement mapping | This table; report objectives | Complete | No external rubric | Compare to official rubric if supplied |
| Python concepts and exercises | Report §Python; script; notebook 1 | Executed | Examples are intentionally short | Practice extending and debugging them |
| Data types and structures | Report §Data types | Complete | No external schema | Validate schema for real data |
| Descriptive statistics | Report §Statistics; notebook 2 | Verified | Quartiles convention-dependent | State linear interpolation |
| Inference, probability, tests | Report §Statistics; SciPy outputs | Verified illustrative calculations | Small synthetic examples cannot support real-world inference | Use representative data and check assumptions |
| Cleaning and EDA | Notebook 3; cleaned CSV, summary JSON | Executed | Median imputations are uncertain | Validate with source data in real work |
| Six chart types | Notebook 4; figures; report | Rendered and embedded | Artificial fixed prices | Do not generalize to market |
| ML evaluation | Report §ML; notebook 5 | Metrics verified | No model experiment; ROC/PR curves described rather than plotted | Fit an optional model only if asked and preserve held-out test data |
| Industry practices | Report §Best practices; README | Complete | No organizational policy supplied | Apply local security policy |
| Report | DOCX, headings, TOC field, page numbers, charts | Programmatically reopened | Pagination and TOC field rendering depend on Word | Update TOC and visually review in Word |
| Reproduction | Requirements, README, notebook | Executed in current environment | Windows not tested; notebook tooling versions are ranged | Re-run on target machine |
| GitHub | Public project repository linked in README | Published; verify URL at delivery | Access can change later | Confirm evaluator can access the URL |
| Viva | VIVA_QUESTIONS.md | Complete | Candidate must practice | Rehearse with actual outputs |

Likely lost marks addressed: skipped formulas, no substitutions, confusing inference and causality, misleading accuracy on imbalanced data, leakage, and unsupported claims.
