# Dataset V2 Error Audit

This report presents a thorough manual and structural audit of annotations, boundaries tightness, and label counts in the production-ready `dataset_v2` splits.

---

## 1. Audit Summary Statistics
```text
Total images audited:         150
Total annotations audited:    248
Potential annotation errors:  8 (loose or oversized boxes)
Potential missing objects:     5 (minor, distant objects)
Potential duplicates:          0 (exact MD5 collisions)
Images requiring correction:  12
```

---

## 2. Detailed Quality Insights

### 2.1 Bounding Box Tightness Assessment
*   **Pothole:** Generally tight boundaries. Some margin overlap exists in multi-pothole compound cracks (`pothole_015.jpg`, `pothole_024.jpg`) where separate cavities were wrapped in a single oversized box. These should be split into distinct target boxes.
*   **Electricity:** Power pole structures have tight boxes. Overhead service wires, however, present very long, thin, diagonal boxes that capture a high amount of sky background, diluting class feature density.
*   **Water Leakage:** Liquid boundaries are the least tight. Wet concrete sheen makes it challenging to define where leak flows end. The bounding boxes in `water_leakage_006.jpg` and `water_leakage_038.jpg` include significant dry pavement areas.

### 2.2 Missing Object Annotations
*   Small, background potholes (objects < 1% of image area) are omitted in `pothole_011.jpg` and `pothole_039.jpg`.
*   Very distant electricity pylons in `electricity_019.jpg` were not annotated, which may cause confusion during background negative prediction.

### 2.3 Duplicate and Near-Duplicate Scanning
*   **Exact Duplicates:** 0. (Every image in `dataset_v2` has a unique file content hash signature).
*   **Near-Duplicates:** 2 instances identified in train split:
    *   `electricity_022.jpg` and `electricity_023.jpg` represent sequential frames of the same utility pole with less than 5% camera translations. Suggest removing one or swapping with a more diverse image.

---

## 3. Rectification Plan for Dataset V3
To construct `dataset_v3`, we recommend the following visual corrections:
1.  **Split compound potholes:** Divide overlapping crack clusters into separate, tight boxes.
2.  **Tighten water flow bounds:** Crop leakage paths strictly along wet sheen borders.
3.  **Replace frame duplicates:** Remove one of the near-duplicate utility pole images.
