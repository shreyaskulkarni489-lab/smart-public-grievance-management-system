# Expanded Dataset Annotation Status Report

This report defines the annotation coverage, source priority checks, and validation metrics for the source reviewed images.

## Priority Source: **dataset_expansion/reviewed/**

## Category Annotation Summary

| Category | Total Images | Annotated (Empty/Valid) | Unannotated |
| :--- | :---: | :---: | :---: |
| **Pothole** | 50 | 0 | 50 |
| **Electricity** | 50 | 0 | 50 |
| **Water Leakage** | 50 | 0 | 50 |
| **Negative (Background)** | 50 | 50 | 0 |
| **Total** | 200 | 50 | 150 |

---

## Annotation Rules Applied
1.  **Negatives are background-only:** Negatives do not have bounding boxes. Their status is considered Completed / Annotated with empty files (Task 3).
2.  **Positives lack bounding boxes:** Positive classifications remain unannotated. No default or fake bounding boxes were generated to prevent training models on corrupt boundaries.
