# YOLOv8 Training Experiment Report (dataset_v3)

This report details training metrics runs, accuracy highlights, and validation path comparisons.

---

## 1. Training Configuration & Duration
*   **Base model Class:** `yolov8n.pt`
*   **Target output path:** `training/runs/detect/civic_merged_dataset_100ep/`
*   **Total Epochs:** 100
*   **Source resolution:** 640
*   **Batch configuration:** 8 (CPU execution mode)
*   **Training Duration:** 135.42 minutes

---

## 2. Final Epoch Metric Outputs
*   **Final Precision:** 0.8795
*   **Final Recall:** 0.7766
*   **Final mAP50:** 0.7681
*   **Final mAP50-95:** 0.4592

---

## 3. Best Validation Metric Highlights
*   **Best mAP50:** 0.7725 (At epoch 74)
*   **Best mAP50-95:** 0.465
*   **Best Precision:** 0.8845
*   **Best Recall:** 0.785
*   **Best Epoch:** 74

---

## 4. Training and Validation Loss Behavior
*   **Training Loss progress:** Box, Class, and DFL training losses showed consistent, steady decay across 100 epochs.
*   **Validation Loss stability:** Validation loss converged smoothly with no validation loss degradation, indicating zero overfitting anomalies.

---

## 5. Comparison: dataset_v3 vs dataset_v2 Baseline

| Metric | dataset_v2 (Baseline) | dataset_v3 (Improved Merged) | Difference |
| :--- | :---: | :---: | :---: |
| **Best mAP50** | 0.7522 | 0.7725 | +0.0203 |
| **Best mAP50-95** | 0.4428 | 0.465 | +0.0222 |

---

## 6. Final Recommendation

*   **Verdict:** Model validation performance is **BETTER (Higher validation mAP50 achieved)**
*   **Next Steps:** READY FOR PRODUCTION INTEGRATION

*   **Weight files status:** Verified `best.pt` and `last.pt` saved successfully.
