# Dataset Expansion YOLOv8 Annotation Guidelines

This document outlines standard visual labeling procedures for custom categories within the Smart Public Grievance Management System.

---

## 1. Class Categorization & Numeric Mappings
Official class mappings:
*   `0` = Pothole
*   `1` = Electricity
*   `2` = Water Leakage

---

## 2. Bounding Box Rules per Category

### A. Pothole (Class 0)
*   **Rule:** Draw a tight, rectangular bounding box bounding the perimeter of the potholes, pavement depressions, or visual structural breaks on asphalt.
*   **Bounds:** Box only the damaged pavement coordinates. Stop boxing normal flat pavements. Look for cracks and loose gravel surrounding the central circle.

### B. Electricity (Class 1)
*   **Rule:** Draw bounding boxes around damaged, dangerous, or exposed utility infrastructure.
*   **Examples:** Damaged electrical poles, exposed wires, broken generator doors, or hanging transformers.
*   **Restriction:** **Do NOT box normal utility wires or normal poles.** Only annotate files that clearly represent light or electrical grievances.

### C. Water Leakage (Class 2)
*   **Rule:** Box the exact water puddle boundaries, leaking pipeline cracks, or structural spray points on dry pavements.
*   **Restriction:** Do not box natural river water, reflections, or wet areas due to standard rain weather. Only select leaks.

---

## 3. Label File Formats
Save label boundaries as a matching name `.txt` file alongside coordinates normalized between `0` and `1`:
`[class_id] [x_center] [y_center] [width] [height]`

*Example:*
`0 0.5200 0.4800 0.3000 0.2500`
