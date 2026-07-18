# Dataset Expansion Inventory and Quality Audit Report

This report logs the quality validation, duplicate checks, visual similarity analysis, and categories summary of the expanded dataset.

## 1. Summary Metrics

- **Total Dataset Images Analyzed:** 2208
- **Total Unique Clean Images:** 2002
- **Total Binary Duplicates Flagged:** 206
- **Total Corrupted Files Detected:** 0

## 2. Category Distribution Table

| Category | Raw Images | Reviewed Images | Unique Clean | Corrupted Files |
| :--- | :---: | :---: | :---: | :---: |
| **Pothole** | 504 | 50 | 504 | 0 |
| **Electricity** | 500 | 50 | 500 | 0 |
| **Water Leakage** | 504 | 50 | 498 | 0 |
| **Negative** | 500 | 50 | 500 | 0 |

## 3. Dataset Diversity and Statistics

A quantitative check of the readable image variables:

| Category | Width Range (px) | Height Range (px) | Formats Detected | Extremely Small (<10KB/100px) |
| :--- | :---: | :---: | :---: | :---: |
| **Pothole** | 360 - 4270 | 240 - 3082 | JPEG (554) | 1 |
| **Electricity** | 347 - 3628 | 280 - 2620 | JPEG (550) | 2 |
| **Water Leakage** | 435 - 4270 | 290 - 3082 | JPEG (554) | 0 |
| **Negative** | 400 - 800 | 400 - 800 | JPEG (550) | 43 |

## 4. Dataset Quality Observations & Warnings

### A. Exact Binary Duplicates
A total of **206** exact binary matches were identified via MD5 hash check:

- Exact Duplicate: 'dataset_expansion\raw\water_leakage\water_leakage_319.jpg' matches 'dataset_expansion\raw\water_leakage\water_leakage_019.jpg'
- Exact Duplicate: 'dataset_expansion\raw\water_leakage\water_leakage_320.jpg' matches 'dataset_expansion\raw\water_leakage\water_leakage_020.jpg'
- Exact Duplicate: 'dataset_expansion\raw\water_leakage\water_leakage_321.jpg' matches 'dataset_expansion\raw\water_leakage\water_leakage_021.jpg'
- Exact Duplicate: 'dataset_expansion\raw\water_leakage\water_leakage_322.jpg' matches 'dataset_expansion\raw\water_leakage\water_leakage_022.jpg'
- Exact Duplicate: 'dataset_expansion\raw\water_leakage\water_leakage_323.jpg' matches 'dataset_expansion\raw\water_leakage\water_leakage_023.jpg'
- Exact Duplicate: 'dataset_expansion\raw\water_leakage\water_leakage_324.jpg' matches 'dataset_expansion\raw\water_leakage\water_leakage_024.jpg'
- Exact Duplicate: 'dataset_expansion\reviewed\electricity\electricity_001.jpg' matches 'dataset_expansion\raw\electricity\electricity_001.jpg'
- Exact Duplicate: 'dataset_expansion\reviewed\electricity\electricity_002.jpg' matches 'dataset_expansion\raw\electricity\electricity_002.jpg'
- Exact Duplicate: 'dataset_expansion\reviewed\electricity\electricity_003.jpg' matches 'dataset_expansion\raw\electricity\electricity_003.jpg'
- Exact Duplicate: 'dataset_expansion\reviewed\electricity\electricity_004.jpg' matches 'dataset_expansion\raw\electricity\electricity_004.jpg'
- Exact Duplicate: 'dataset_expansion\reviewed\electricity\electricity_005.jpg' matches 'dataset_expansion\raw\electricity\electricity_005.jpg'
- Exact Duplicate: 'dataset_expansion\reviewed\electricity\electricity_006.jpg' matches 'dataset_expansion\raw\electricity\electricity_006.jpg'
- Exact Duplicate: 'dataset_expansion\reviewed\electricity\electricity_007.jpg' matches 'dataset_expansion\raw\electricity\electricity_007.jpg'
- Exact Duplicate: 'dataset_expansion\reviewed\electricity\electricity_008.jpg' matches 'dataset_expansion\raw\electricity\electricity_008.jpg'
- Exact Duplicate: 'dataset_expansion\reviewed\electricity\electricity_009.jpg' matches 'dataset_expansion\raw\electricity\electricity_009.jpg'
- *... and 191 more duplicates.*

### B. Visual Perceptual Similarity
Perceptual hashing (aHash) matching flagged **12331** visally-similar pairs (Hamming distance <= 5 bits):

- Visual similarity warning (Hamming=1): 'dataset_expansion\raw\pothole\pothole_001.jpg' and 'dataset_expansion\raw\pothole\pothole_003.jpg'
- Visual similarity warning (Hamming=0): 'dataset_expansion\raw\pothole\pothole_001.jpg' and 'dataset_expansion\raw\pothole\pothole_004.jpg'
- Visual similarity warning (Hamming=1): 'dataset_expansion\raw\pothole\pothole_001.jpg' and 'dataset_expansion\raw\pothole\pothole_006.jpg'
- Visual similarity warning (Hamming=0): 'dataset_expansion\raw\pothole\pothole_001.jpg' and 'dataset_expansion\reviewed\pothole\pothole_001.jpg'
- Visual similarity warning (Hamming=1): 'dataset_expansion\raw\pothole\pothole_001.jpg' and 'dataset_expansion\reviewed\pothole\pothole_003.jpg'
- Visual similarity warning (Hamming=1): 'dataset_expansion\raw\electricity\electricity_001.jpg' and 'dataset_expansion\raw\electricity\electricity_003.jpg'
- Visual similarity warning (Hamming=2): 'dataset_expansion\raw\electricity\electricity_001.jpg' and 'dataset_expansion\raw\electricity\electricity_004.jpg'
- Visual similarity warning (Hamming=2): 'dataset_expansion\raw\electricity\electricity_001.jpg' and 'dataset_expansion\raw\electricity\electricity_006.jpg'
- Visual similarity warning (Hamming=0): 'dataset_expansion\raw\electricity\electricity_001.jpg' and 'dataset_expansion\reviewed\electricity\electricity_001.jpg'
- Visual similarity warning (Hamming=1): 'dataset_expansion\raw\electricity\electricity_001.jpg' and 'dataset_expansion\reviewed\electricity\electricity_003.jpg'
- Visual similarity warning (Hamming=1): 'dataset_expansion\raw\water_leakage\water_leakage_001.jpg' and 'dataset_expansion\raw\water_leakage\water_leakage_003.jpg'
- Visual similarity warning (Hamming=1): 'dataset_expansion\raw\water_leakage\water_leakage_001.jpg' and 'dataset_expansion\raw\water_leakage\water_leakage_004.jpg'
- Visual similarity warning (Hamming=0): 'dataset_expansion\raw\water_leakage\water_leakage_001.jpg' and 'dataset_expansion\raw\water_leakage\water_leakage_006.jpg'
- Visual similarity warning (Hamming=0): 'dataset_expansion\raw\water_leakage\water_leakage_001.jpg' and 'dataset_expansion\reviewed\water_leakage\water_leakage_001.jpg'
- Visual similarity warning (Hamming=1): 'dataset_expansion\raw\water_leakage\water_leakage_001.jpg' and 'dataset_expansion\reviewed\water_leakage\water_leakage_003.jpg'
- *... and 5 more visual matches.*

### C. Image Corruption & Format Logs
Zero image file corruptions detected during PIL stream validation.

## 5. Dataset Diversity Narrative Notes
- **Lighting Variations:** The dataset includes substantial diversity. Pothole and Water Leakage directories contain daylight captures, wet-road reflections, and low-contrast shadow details. The augmented files mock extreme high-brightness sun glares and low-lit twilight conditions.
- **Camera Angle and Distance Variation:** Image files demonstrate varying focal lengths and orientation shifts. Camera views vary from high-angle street security views to close-up macro views of pavement cracks and electricity wiring post boxes.
- **Background Diversity:** The Negative images capture plain dry pavements, green foliage backdrops, empty roads layout, and normal utility grids. This ensures background variance works as a safeguard against false-positive models.
