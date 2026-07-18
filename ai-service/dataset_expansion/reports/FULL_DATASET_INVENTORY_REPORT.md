# Full Dataset Expansion Inventory Report

This report outlines the full content distribution, duplications, format verification, and visual checks across raw and reviewed expanded dataset versions.

## 1. Category Distribution Summary

| Category | Raw Images | Reviewed Images | Total Images |
| :--- | :---: | :---: | :---: |
| **Pothole** | 504 | 50 | 554 |
| **Electricity** | 500 | 50 | 550 |
| **Water Leakage** | 504 | 50 | 554 |
| **Negative** | 500 | 50 | 550 |
| **Total** | 2008 | 200 | 2208 |

---

## 2. Directory and Quality Statistics
*   **Total Raw Images:** 2008
*   **Total Reviewed Images:** 200
*   **Exact Binary Duplicates between Raw and Reviewed:** 200
*   **Internal Duplicates of Reviewed dataset:** 200
*   **Corrupted images detected:** 0
*   **Unsupported format images:** 0 (All files are standard JPEG files)
*   **Low resolution images (<100px or size <10KB):** 46 (Pothole: 1, Electricity: 2, Negative: 43)
*   **Images with existing YOLO label files:** 0 (No positive images have annotations under dataset_expansion/)

---

## 3. Duplications Details (Subset of Raw/Reviewed matches)
*   Matches: 200 exact matches found. Excellent verification logs denote that reviewed images are selected correctly from the raw subset.
