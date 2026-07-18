# Visual Annotation Tool Setup

Use a visual labeling tool to annotate the positive images located in `dataset_expansion/annotation_workspace/`.

## Recommended Client Tool: CVAT or LabelImg / Labelme

### Step-by-Step workflow with LabelImg:
1.  **Install locally:**
    `pip install labelImg`
2.  **Start application:**
    `labelImg`
3.  **Choose directories inside the program:**
    *   Click **Open Dir** and select `dataset_expansion/annotation_workspace/pothole/` (or `electricity/`, `water_leakage/`).
    *   Click **Change Save Dir** and choose the same workspace folder so images and labels save together.
4.  **Format setup:**
    *   Change format label to **YOLO** format (under the Save option).
5.  **Classes configuration:**
    Ensure classes match exactly:
    *   0: Pothole
    *   1: Electricity
    *   2: Water Leakage
6.  **Create box labels:**
    *   Press `W` to draw a box, select class name, and press `Ctrl+S` to save.
