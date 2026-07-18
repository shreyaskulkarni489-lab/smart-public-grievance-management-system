# Production Ready YOLOv8 Civic Dataset

This directory contains the final production expanded dataset for the Smart Public Grievance Management System.

## Class Mapping
*   `0`: Pothole
*   `1`: Electricity
*   `2`: Water Leakage

## Stratified Split Distribution
*   **Train Set (70%):** 105 images (35 pothole, 35 electricity, 35 water_leakage)
*   **Val Set (20%):** 30 images (10 pothole, 10 electricity, 10 water_leakage)
*   **Test Set (10%):** 15 images (5 pothole, 5 electricity, 5 water_leakage)
*   **Random Seed:** 42

## Format
Every coordinate is normalized between 0-1 following the standard format:
`[class_id] [x_center] [y_center] [width] [height]`

## Validation Results
*   Missing labels: 0
*   Data Leakage overlap: 0
*   Target Status: **READY FOR TRAINING**

## YOLOv8 Training Command
To train YOLOv8 on this dataset using CPU:
```bash
yolo task=detect mode=train model=yolov8n.pt data=dataset_v2/data.yaml epochs=100 imgsz=640 batch=8 device=cpu
```
