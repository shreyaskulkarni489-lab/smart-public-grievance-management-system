# Dataset Improvement Plan (V3)

This plan outlines data collection parameters and specific example profiles required to construct the improved `dataset_v3` for the Smart Public Grievance Management System.

---

## 1. Pothole

To address the high rate of missed potholes (recall of 55.56% on test split), the training dataset must be supplemented with these visual varieties:

*   **Small Potholes:** 20+ images of small road holes (diameter < 15cm) to train the model on early-stage road pavement failures.
*   **Dark/Shadowed Potholes:** 20+ images of potholes covered by foliage shadow structures or dark wet cavities on dark asphalt surfaces.
*   **Partially Visible Potholes:** 15+ images of potholes located at the edges of the camera view, capturing border truncations.
*   **Varying Pavements:** 15+ images of potholes on unpaved dirt roads, yellow lines, cobbles, and brick-layered pavements.
*   **Varying Camera Distances:** Add images captured from moving vehicles (long-distance forward views) mimicking standard dashcam telemetry.

---

## 2. Water Leakage

To decrease false-alarm checks (F1 = 76.92% on test split), collect files matching:

*   **Subtle & Small Patches:** 25+ images of minor fluid leakage paths (thin streams vs wide pools) representing fresh Pipe breaks.
*   **Low-Light & specularity:** Images captured under cloud cover and dusk highlighting reflections on water surfaces versus dry surfaces.
*   **Leakage near Potholes:** 15+ images of pooled water inside pothole cavities to help the network differentiate pothole structures from flat leaking flows.
*   **Distinct pavement textures:** Leakage on concrete sidewalk stones, brick lanes, and highly porous asphalt.

---

## 3. Hard-Negative Background Images

Hard-negatives are crucial to suppress false alarms in real-world deployments. Add 40+ negative background images containing:

*   **Normal Road Cracks:** Sealed asphalt lines and joints (confused with potholes).
*   **Dark Asphalt Patches:** Re-paved blacktop circles and squares (confused with potholes).
*   **Wet Roads without Leakage:** Image of streets after rain showing uniform wetness/sheen (confused with water leakage).
*   **Ambient Shadows:** Tree leaf shadows, building overhangs, and vehicle shadows on dry grey roads (confused with potholes and leakage).
*   **Unrelated overhead cables:** Standard phone cords, tree branches, or clean laundry lines (confused with electricity-related hazards).
*   **Poles without damage:** Clean, normal street lights, tree trunks, and signs.
