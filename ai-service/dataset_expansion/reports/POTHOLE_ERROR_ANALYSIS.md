# Pothole Failure Analysis Report

This document reviews the specific failure profiles of the 4 missed pothole objects from the test split evaluation of the `dataset_v2_100ep` model.

---

## 1. Missed Case Diagnostics

### Case 1: Pothole in `pothole_008.jpg`
*   **Metric Info:** Missed (Ground Truth not matched, 0.00 confidence prediction)
*   **Visual Cause:** 
    *   *Unusual Camera Angle & Distance:* Pothole is located far in the background, making its visual resolution small.
    *   *Low Contrast:* The road surface is aged concrete (light greyish-white), meaning the pothole's texture blends significantly, escaping the model's feature detection.
*   **Root Cause:** Small object size combined with low contrast.

### Case 2: Pothole in `pothole_016.jpg`
*   **Metric Info:** Missed (Ground Truth not matched, 0.00 confidence prediction)
*   **Visual Cause:**
    *   *Shadows & Low-Light:* A large tree canopy casts dense shadows across the road surface.
    *   *Dark Road Surface:* The pothole itself is filled with shadow and dark asphalt grit, making it indistinguishable from normal road shadows.
*   **Root Cause:** Heavy shadows and dark road surface.

### Case 3: Pothole in `pothole_018.jpg`
*   **Metric Info:** Missed (Low Confidence, prediction conf of 0.05)
*   **Visual Cause:**
    *   *Small Object Size:* The pothole is a minor asphalt pit at a distance.
    *   *Visually Similar to Normal Road Texture:* The pavement is cracked and worn, so the pothole's boundaries lack clean shape definition.
*   **Root Cause:** Small object size and high background clutter (worn pavement).

### Case 4: Pothole in `pothole_041.jpg`
*   **Metric Info:** Missed (Ground Truth not matched, 0.00 confidence prediction)
*   **Visual Cause:**
    *   *Partial Visibility & Occlusion:* The pothole is located at the very margin of the image frame.
    *   *Low Contrast:* Shallow depth makes it look like a superficial road blemish rather than a structural pit.
*   **Root Cause:** Partial visibility/border truncation and low contrast.

---

## 2. Summary of Pothole Failure Modes

| Cause Mode | Occurrences | Percentage | Action Item |
| :--- | :---: | :---: | :--- |
| **Small Object Size** | 2 | 50.0% | Expand training dataset with far-distance pothole views. |
| **Low Contrast / Road Blending** | 2 | 50.0% | Gather concrete/aged asphalt pavements. |
| **Heavy Shadows / Low-Light** | 1 | 25.0% | Capture images under tree canopy shadows. |
| **Border Truncation / Trimming** | 1 | 25.0% | Maintain bounds during augments. |

---

## 3. Data Collection Action Items
To address these 4 failure modes, future dataset versions (`dataset_v3`) require:
1.  **Varying Textures:** 30+ images of potholes on concrete (grey/white) pavements.
2.  **Scale Variance:** 25+ images of potholes captured from 15+ meters away (small scale).
3.  **Illumination Robustness:** 20+ images of potholes casting/receiving shadows under sunlight tree coverage.
