# Duplicate Resolution Report

This report outlines the resolutions applied to duplicate and near-duplicate candidates during structural merge.

## 1. Exact Binary SHA-256 Duplicates
*   **Exact duplicates found:** 24
*   **Exact duplicates removed:** 12

### Resolution details:
*   `electricity_022.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\train\electricity_022.jpg`
    *   `dataset_improvement\source\corrections\electricity_022.jpg`
*   `electricity_023.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\train\electricity_023.jpg`
    *   `dataset_improvement\source\corrections\electricity_023.jpg`
*   `pothole_024.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\train\pothole_024.jpg`
    *   `dataset_improvement\source\corrections\pothole_024.jpg`
*   `water_leakage_006.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\train\water_leakage_006.jpg`
    *   `dataset_improvement\source\corrections\water_leakage_006.jpg`
*   `water_leakage_038.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\train\water_leakage_038.jpg`
    *   `dataset_improvement\source\corrections\water_leakage_038.jpg`
*   `electricity_035.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\test\electricity_035.jpg`
    *   `dataset_improvement\source\corrections\electricity_035.jpg`
*   `pothole_008.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\test\pothole_008.jpg`
    *   `dataset_improvement\source\corrections\pothole_008.jpg`
*   `pothole_016.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\test\pothole_016.jpg`
    *   `dataset_improvement\source\corrections\pothole_016.jpg`
*   `pothole_018.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\test\pothole_018.jpg`
    *   `dataset_improvement\source\corrections\pothole_018.jpg`
*   `pothole_041.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\test\pothole_041.jpg`
    *   `dataset_improvement\source\corrections\pothole_041.jpg`
*   `water_leakage_014.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\test\water_leakage_014.jpg`
    *   `dataset_improvement\source\corrections\water_leakage_014.jpg`
*   `water_leakage_046.jpg`: Kept correction version of the file, removed other copies from:
    *   `dataset_v2\images\test\water_leakage_046.jpg`
    *   `dataset_improvement\source\corrections\water_leakage_046.jpg`


## 2. Perceptual Similarity Near-Duplicates (Hamming dHash <= 2)
*   **Near-duplicates removed:** 68 (Hamming Distance <= 1, representing redundant frame iterations)
*   **Near-duplicates retained:** 37 (Hamming Distance == 2, representing genuinely unique perspective offsets)

### Removed Redundancy Nodes:
*   Removed duplicate pair elements: `dataset_v2\images\train\electricity_004.jpg` similar to `dataset_v2\images\train\electricity_001.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_v2\images\val\electricity_003.jpg` similar to `dataset_v2\images\train\electricity_004.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\electricity_010.jpg` similar to `dataset_v2\images\train\electricity_007.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\electricity_012.jpg` similar to `dataset_v2\images\train\electricity_010.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_v2\images\train\electricity_018.jpg` similar to `dataset_v2\images\train\electricity_016.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\electricity_030.jpg` similar to `dataset_v2\images\train\electricity_028.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_v2\images\train\electricity_046.jpg` similar to `dataset_v2\images\train\electricity_043.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\val\pothole_006.jpg` similar to `dataset_v2\images\train\pothole_001.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\corrections\pothole_016.jpg` similar to `dataset_v2\images\train\pothole_013.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_v2\images\train\pothole_021.jpg` similar to `dataset_v2\images\train\pothole_019.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_v2\images\train\pothole_022.jpg` similar to `dataset_v2\images\train\pothole_021.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\corrections\pothole_024.jpg` similar to `dataset_v2\images\train\pothole_022.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_v2\images\train\pothole_030.jpg` similar to `dataset_v2\images\train\pothole_025.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\val\pothole_028.jpg` similar to `dataset_v2\images\train\pothole_030.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\pothole_034.jpg` similar to `dataset_v2\images\train\pothole_031.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\pothole_040.jpg` similar to `dataset_v2\images\train\pothole_037.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_v2\images\train\pothole_042.jpg` similar to `dataset_v2\images\train\pothole_040.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_v2\images\train\pothole_045.jpg` similar to `dataset_v2\images\train\pothole_043.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_051.jpg` similar to `dataset_v2\images\train\pothole_049.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\water_leakage_003.jpg` similar to `dataset_v2\images\train\water_leakage_001.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\water_leakage_004.jpg` similar to `dataset_v2\images\train\water_leakage_003.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\corrections\water_leakage_006.jpg` similar to `dataset_v2\images\train\water_leakage_004.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\water_leakage_018.jpg` similar to `dataset_v2\images\train\water_leakage_013.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\water_leakage_024.jpg` similar to `dataset_v2\images\train\water_leakage_019.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\test\water_leakage_021.jpg` similar to `dataset_v2\images\train\water_leakage_024.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\water_leakage_027.jpg` similar to `dataset_v2\images\train\water_leakage_025.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\water_leakage_028.jpg` similar to `dataset_v2\images\train\water_leakage_027.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\val\water_leakage_030.jpg` similar to `dataset_v2\images\train\water_leakage_028.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\test\water_leakage_037.jpg` similar to `dataset_v2\images\train\water_leakage_039.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\train\water_leakage_048.jpg` similar to `dataset_v2\images\train\water_leakage_043.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_v2\images\val\water_leakage_045.jpg` similar to `dataset_v2\images\train\water_leakage_048.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\water_leakage\water_leakage_051.jpg` similar to `dataset_v2\images\train\water_leakage_049.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_v2\images\test\water_leakage_037.jpg` similar to `dataset_v2\images\val\water_leakage_042.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\corrections\water_leakage_046.jpg` similar to `dataset_v2\images\val\water_leakage_045.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\hard_negatives\pothole\negative_009.jpg` similar to `dataset_improvement\source\hard_negatives\pothole\negative_005.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\hard_negatives\water_leakage\negative_013.jpg` similar to `dataset_improvement\source\hard_negatives\pothole\negative_009.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\hard_negatives\water_leakage\negative_017.jpg` similar to `dataset_improvement\source\hard_negatives\water_leakage\negative_013.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_057.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_055.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_058.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_057.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_066.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_061.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_066.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_063.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_072.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_067.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_081.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_079.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_084.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_081.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_084.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_082.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_087.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_085.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_088.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_087.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_090.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_088.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_093.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_091.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_096.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_093.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_096.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_094.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_099.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_097.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_100.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_099.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\pothole\pothole_102.jpg` similar to `dataset_improvement\source\additional_positives\pothole\pothole_100.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\water_leakage\water_leakage_054.jpg` similar to `dataset_improvement\source\additional_positives\water_leakage\water_leakage_051.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\water_leakage\water_leakage_058.jpg` similar to `dataset_improvement\source\additional_positives\water_leakage\water_leakage_055.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\water_leakage\water_leakage_060.jpg` similar to `dataset_improvement\source\additional_positives\water_leakage\water_leakage_057.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\water_leakage\water_leakage_060.jpg` similar to `dataset_improvement\source\additional_positives\water_leakage\water_leakage_058.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\water_leakage\water_leakage_066.jpg` similar to `dataset_improvement\source\additional_positives\water_leakage\water_leakage_063.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\water_leakage\water_leakage_069.jpg` similar to `dataset_improvement\source\additional_positives\water_leakage\water_leakage_067.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\water_leakage\water_leakage_070.jpg` similar to `dataset_improvement\source\additional_positives\water_leakage\water_leakage_069.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\electricity\electricity_052.jpg` similar to `dataset_improvement\source\additional_positives\electricity\electricity_051.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\electricity\electricity_054.jpg` similar to `dataset_improvement\source\additional_positives\electricity\electricity_052.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\electricity\electricity_060.jpg` similar to `dataset_improvement\source\additional_positives\electricity\electricity_055.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\electricity\electricity_063.jpg` similar to `dataset_improvement\source\additional_positives\electricity\electricity_061.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\electricity\electricity_064.jpg` similar to `dataset_improvement\source\additional_positives\electricity\electricity_063.jpg` (Hamming Distance: 0)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\electricity\electricity_066.jpg` similar to `dataset_improvement\source\additional_positives\electricity\electricity_064.jpg` (Hamming Distance: 1)
*   Removed duplicate pair elements: `dataset_improvement\source\additional_positives\electricity\electricity_069.jpg` similar to `dataset_improvement\source\additional_positives\electricity\electricity_067.jpg` (Hamming Distance: 1)

### Retained Visual Variants:
*   Retained variant: `dataset_v2\images\train\electricity_018.jpg` and `dataset_v2\images\val\electricity_013.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\electricity_021.jpg` and `dataset_v2\images\val\electricity_019.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\corrections\electricity_022.jpg` and `dataset_v2\images\val\electricity_019.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\electricity_027.jpg` and `dataset_v2\images\train\electricity_028.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\electricity_027.jpg` and `dataset_v2\images\train\electricity_030.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\electricity_030.jpg` and `dataset_v2\images\test\electricity_025.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\electricity_042.jpg` and `dataset_v2\images\val\electricity_037.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\electricity_042.jpg` and `dataset_v2\images\val\electricity_040.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\electricity_049.jpg` and `dataset_improvement\source\additional_positives\electricity\electricity_051.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\electricity_049.jpg` and `dataset_improvement\source\additional_positives\electricity\electricity_052.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\pothole_012.jpg` and `dataset_v2\images\val\pothole_007.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\pothole_027.jpg` and `dataset_v2\images\train\pothole_030.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\pothole_045.jpg` and `dataset_v2\images\train\pothole_046.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\pothole_046.jpg` and `dataset_v2\images\val\pothole_048.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\water_leakage_012.jpg` and `dataset_v2\images\val\water_leakage_009.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\water_leakage_018.jpg` and `dataset_v2\images\val\water_leakage_016.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\water_leakage_019.jpg` and `dataset_v2\images\train\water_leakage_022.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\water_leakage_031.jpg` and `dataset_v2\images\train\water_leakage_034.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\water_leakage_031.jpg` and `dataset_v2\images\val\water_leakage_036.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\water_leakage_034.jpg` and `dataset_v2\images\val\water_leakage_036.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\water_leakage_039.jpg` and `dataset_v2\images\val\water_leakage_042.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\train\water_leakage_040.jpg` and `dataset_v2\images\test\water_leakage_037.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_v2\images\val\electricity_037.jpg` and `dataset_v2\images\val\electricity_040.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\corrections\pothole_016.jpg` and `dataset_improvement\source\corrections\pothole_018.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\pothole\pothole_051.jpg` and `dataset_improvement\source\additional_positives\pothole\pothole_052.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\pothole\pothole_051.jpg` and `dataset_improvement\source\additional_positives\pothole\pothole_054.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\pothole\pothole_052.jpg` and `dataset_improvement\source\additional_positives\pothole\pothole_054.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\pothole\pothole_061.jpg` and `dataset_improvement\source\additional_positives\pothole\pothole_063.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\pothole\pothole_063.jpg` and `dataset_improvement\source\additional_positives\pothole\pothole_064.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\pothole\pothole_067.jpg` and `dataset_improvement\source\additional_positives\pothole\pothole_070.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\pothole\pothole_069.jpg` and `dataset_improvement\source\additional_positives\pothole\pothole_070.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\pothole\pothole_081.jpg` and `dataset_improvement\source\additional_positives\pothole\pothole_082.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\pothole\pothole_093.jpg` and `dataset_improvement\source\additional_positives\pothole\pothole_094.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\water_leakage\water_leakage_051.jpg` and `dataset_improvement\source\additional_positives\water_leakage\water_leakage_052.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\water_leakage\water_leakage_055.jpg` and `dataset_improvement\source\additional_positives\water_leakage\water_leakage_057.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\water_leakage\water_leakage_057.jpg` and `dataset_improvement\source\additional_positives\water_leakage\water_leakage_058.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
*   Retained variant: `dataset_improvement\source\additional_positives\electricity\electricity_055.jpg` and `dataset_improvement\source\additional_positives\electricity\electricity_058.jpg` (Hamming Distance: 2) -- clustered in same split to prevent leakage.
