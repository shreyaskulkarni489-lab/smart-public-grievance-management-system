# Sprint 5.9.16 — Final Dataset v4 Full 3-Class Validation

This validation report catalogs all deep analytics, coordinate ranges, format integrity, and isolation proofs for target v4 training splits.

---

## 1. Split Distribution Summary

| Split Fold | Image Count | Percentage Share (%) |
| :--- | :---: | :---: |
| **Train** | 193 | 75.98% |
| **Validation** | 37 | 14.57% |
| **Test** | 24 | 9.45% |
| **Total Images** | **254** | **100.00%** |

---

## 2. Bounding Box and Class Distributions

| Class Category (ID) | Train (Img / Box) | Validation (Img / Box) | Test (Img / Box) | Total Boxes (Sum) |
| :--- | :---: | :---: | :---: | :---: |
| **Pothole (0)** | 102 / 176 | 13 / 17 | 8 / 8 | **201** |
| **Electricity (1)** | 40 / 69 | 9 / 16 | 7 / 13 | **98** |
| **Water Leakage (2)** | 33 / 41 | 10 / 14 | 5 / 7 | **62** |

*   **Total Bounding Boxes:** 361
*   **Average Boxes per Image:** 1.421
*   **Zero-Box Background Images Count:** 27 / 254

---

## 3. Formatting, Matching, and Integrity Checks
*   **Missing Labels File pairs:** 0
*   **Orphan Label Files:** 0
*   **Corrupted or Unreadable Frames:** 0
*   **Invalid YOLO coordinate formats:** 1
*   **Preservation status of dataset_v3:** Preserved (100% intact)

---

## 4. Cross-Split Exact Duplicates and Leakage Log
*   **Exact duplicates detected:** 0

| File A | File B | Duplicate Type |
| :--- | :--- | :--- |
_No exact duplicates or cross-split leakage detected._


---

## 5. Cross-Split Perceptual Near-Duplicates Log (Hamming Distance <= 2)
*   **Near-duplicates detected:** 22

| File A | File B | Hamming Distance | Split Relation |
| :--- | :--- | :---: | :--- |
| `dataset_v4\images\train\electricity_019.jpg` | `dataset_v4\images\train\electricity_021.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\electricity_019.jpg` | `dataset_v4\images\train\electricity_022.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\electricity_025.jpg` | `dataset_v4\images\train\electricity_030.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\electricity_027.jpg` | `dataset_v4\images\train\electricity_030.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\electricity_037.jpg` | `dataset_v4\images\train\electricity_040.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\electricity_037.jpg` | `dataset_v4\images\train\electricity_042.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\electricity_040.jpg` | `dataset_v4\images\train\electricity_042.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\pothole_007.jpg` | `dataset_v4\images\train\pothole_012.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\pothole_016.jpg` | `dataset_v4\images\train\pothole_018.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\pothole_045.jpg` | `dataset_v4\images\train\pothole_046.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\pothole_046.jpg` | `dataset_v4\images\train\pothole_048.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\pothole_051.jpg` | `dataset_v4\images\train\pothole_052.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\pothole_051.jpg` | `dataset_v4\images\train\pothole_054.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\pothole_052.jpg` | `dataset_v4\images\train\pothole_054.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\pothole_069.jpg` | `dataset_v4\images\train\pothole_070.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\water_leakage_009.jpg` | `dataset_v4\images\train\water_leakage_012.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\water_leakage_016.jpg` | `dataset_v4\images\train\water_leakage_018.jpg` | 2 | train <-> train |
| `dataset_v4\images\train\water_leakage_037.jpg` | `dataset_v4\images\train\water_leakage_040.jpg` | 2 | train <-> train |
| `dataset_v4\images\val\water_leakage_031.jpg` | `dataset_v4\images\val\water_leakage_034.jpg` | 2 | val <-> val |
| `dataset_v4\images\val\water_leakage_031.jpg` | `dataset_v4\images\val\water_leakage_036.jpg` | 2 | val <-> val |
| `dataset_v4\images\val\water_leakage_034.jpg` | `dataset_v4\images\val\water_leakage_036.jpg` | 2 | val <-> val |
| `dataset_v4\images\test\electricity_013.jpg` | `dataset_v4\images\test\electricity_018.jpg` | 2 | test <-> test |


---

## 6. External Test Set Isolation Check
*   **Target:** Confirmed that the 20 isolated test images under `external_test/` are absent from `dataset_v4`.
*   **Matches Log:**
_Passed (20 test images completely isolated from v4)._


---

## 7. Actionable Validation Verdict
*   **Final Verdict:** **`NOT READY FOR TRAINING`**
*   **Summary Verdict Details:** The dataset validation failed due to one invalid annotation box formatting with a zero dimension:
    *   **File Path:** `dataset_v4/labels/train/ext_img-415_jpg.rf.2285ec32b9bdc584221e193dc135e3fd.txt`
    *   **Line:** `0 0.68 0.545 0 0.0033333333333333335`
    *   **Reason:** Bounding box width is exactly `0`, which violates YOLO requirement (width must be > 0).
    *   **dataset_v3 status:** Confirmed to be preserved.
    *   **Verdict Recommendation:** Fix the invalid coordinate line in next sprint before initiating training.
