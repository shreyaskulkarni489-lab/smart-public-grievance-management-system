# Sprint 5.9.8 Report — Error-Driven Dataset Improvement

This report summarizes the results of the error-driven analytical audits and provides action plans for future dataset upgrades.

---

## 1. Current Baseline Test-Set Performance
*   **Model:** `training/runs/detect/civic_dataset_v2_100ep/weights/best.pt`
*   **Precision:** `86.36%` (at best operating threshold 0.50)
*   **Recall:** `76.00%`
*   **F1 Score:** `80.85%`
*   **Detection Accuracy:** `76.00%`

---

## 2. Main Error Sources
*   **Pothole:** 4 missed pothole targets (55.56% recall). Caused by small object sizes, background blend on light concrete, and heavy canopy shadows.
*   **Water Leakage:** 1 missed target (thin speculative stream) and 2 false positives (confusing shadows and general wet asphalt gloss).
*   **Electricity:** 1 missed pole target (cable wire against dark trees background) and 1 false positive (leaf contours matching overhead lines).
*   **False Positives:** Under-representation of non-faulty wet asphalt and shadow patterns.

---

## 3. Dataset Problems Found
*   **Annotation Errors:** 8 compound pothole crack annotations are too loose and should be split into individual boxes.
*   **Missing Annotations:** 5 small, distant background potholes and power pylons are unlabelled.
*   **Difficult Images:** `water_leakage_014.jpg` contains highly specular wet streams and foliage shadows.
*   **Duplicate Issues:** 0 exact duplicates; 2 near-duplicate utility line images identified (`electricity_022.jpg` / `electricity_023.jpg`).

---

## 4. Recommended Dataset changes
*   **Images to Add:**
    *   30+ concrete pothole images.
    *   25+ distant small potholes.
    *   20+ wet sheen asphalt roads (hard negs).
    *   20+ shadows on dry streets (hard negs).
*   **Images to Correct:** 12 image annotations under `dataset_v2` (tighten leakage borders, split composite potholes).
*   **Images to Remove:** 1 of the two near-duplicate utility pole frames (e.g. `electricity_022.jpg`).
*   **Classes requiring more data:** **Pothole** (Recall needs primary bootstrap) and **Water Leakage** (F1 needs stabilization).

---

**Sprint analytical phase completed successfully.**
