# Water Leakage Failure Analysis Report

This document reviews the failure profiles of water leakage prediction errors from the isolated test split evaluation, assigning data-improvement priority classifications.

---

## 1. Missed and False Positive Case Reports

### Case 1: Missed Ground Truth in `water_leakage_014.jpg`
*   **Metric Info:** Missed (Ground Truth not matched, 0.00 confidence prediction)
*   **Visual Analysis:**
    *   *Small/Subtle Leakage Region:* The fluid leak is a thin, winding stream rather than a wide pool.
    *   *Lighting & Reflection:* Bright overcast reflection on the pavement creates high specularity that obscures the dark color of the water.
*   **Difficulty Classification:** **DIFFICULT**  
    *Decision:* Retain for future training. This representation is vital for early leak identification.

### Case 2: False Positive at center (0.87, 0.50) in `water_leakage_014.jpg`
*   **Metric Info:** False Positive (Water Leakage predicted with 0.86 confidence, but mismatching GT location)
*   **Visual Analysis:**
    *   *Reflection & Shadow:* A dark shadow cast by roadside foliage mimics the exact geometric shape of a water puddle on the asphalt.
    *   *Lack of Color Cues:* Monochromatic pavement features make shadows look identical to liquid spills.
*   **Difficulty Classification:** **AMBIGUOUS**  
    *Decision:* Review and add negative background control samples to distinguish shadow segments.

### Case 3: False Positive at center (0.50, 0.48) in `water_leakage_046.jpg`
*   **Metric Info:** False Positive (Water Leakage predicted with 0.53 confidence, but no matching GT)
*   **Visual Analysis:**
    *   *Reflection & Wet Road Texture:* An area of the asphalt is wet/shiny but does strictly not represent a leakage grievance (just standard wet road sheen).
    *   *Context Cues:* The model confuses general sun glare/shine on wet asphalt with actual domestic pipe or sewage leaks.
*   **Difficulty Classification:** **DIFFICULT**  
    *Decision:* Retain for future training, particularly to help the network differentiate uniform wet sheen from localized leak flows.

---

## 2. Training Feasibility Decisions

| Image Ref | Issue Description | Classification | Training Action |
| :--- | :--- | :--- | :--- |
| `water_leakage_014.jpg` (GT area) | Thin spécular leakage stream | **DIFFICULT** | Keep in training data; teaches model to recognize thin runoff. |
| `water_leakage_014.jpg` (FP area) | foliage shadows on cement | **AMBIGUOUS** | Supplement with shadow negatives to suppress. |
| `water_leakage_046.jpg` (FP area) | Glare sheen on wet asphalt | **DIFFICULT** | Inject as hard-negative background examples. |

---

## 3. Recommended Actions
1.  **Exclude Unusable:** Remove low-resolution, blurry, or non-grievance wet images from annotations.
2.  **Add Wet Pavement negatives:** Provide 15+ negative images of fully wet blacktop under clear sun (high reflection) to distinguish actual runoff paths from ambient wet pavement.
3.  **Correct Pothole overlap:** Distinguish pothole cavities containing water (Pothole class) from flowing leaks on smooth street lines (Water Leakage class).
