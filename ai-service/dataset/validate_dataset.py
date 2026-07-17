import os
import sys

# Configuration
DATASET_DIR = os.path.dirname(os.path.abspath(__file__))
YAML_PATH = os.path.join(DATASET_DIR, "data.yaml")

SUBSETS = ["train", "val"]
DIRS = {
    "train_images": os.path.join(DATASET_DIR, "images", "train"),
    "val_images": os.path.join(DATASET_DIR, "images", "val"),
    "train_labels": os.path.join(DATASET_DIR, "labels", "train"),
    "val_labels": os.path.join(DATASET_DIR, "labels", "val")
}

def parse_yaml_safely(path):
    """Parses data.yaml, verified against syntax errors."""
    if not os.path.exists(path):
        return None, "File does not exist."
    try:
        import yaml
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        return data, None
    except ImportError:
        # Fallback basic text parser just in case PyYAML is missing
        try:
            data = {}
            with open(path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    if ':' in line:
                        k, v = line.split(':', 1)
                        data[k.strip()] = v.strip()
            return data, "PyYAML not installed, basic fallback succeeded."
        except Exception as e:
            return None, f"Basic fallback loader failed: {e}"
    except Exception as e:
        return None, f"YAML syntax error: {e}"

def validate():
    print("==================================================")
    print("RUNNING REUSABLE YOLOv8 DATASET VALIDATOR")
    print("==================================================")
    
    errors = []
    warnings = []
    
    # Task 2: Validate Directory Structure and data.yaml
    print("\n[Step 1] Validating Directory Structure & data.yaml...")
    yaml_config, yaml_err = parse_yaml_safely(YAML_PATH)
    if yaml_config is None:
        errors.append(f"data.yaml validation error: {yaml_err}")
    else:
        print("[x] data.yaml exists and syntax is valid.")
        
        # Verify structure elements in data.yaml
        required_keys = ["train", "val", "nc", "names"]
        for k in required_keys:
            if k not in yaml_config:
                errors.append(f"data.yaml missing key: '{k}'")
                
        if "nc" in yaml_config:
            try:
                nc = int(yaml_config["nc"])
                if nc != 3:
                    errors.append(f"Invalid nc: expected 3 classes, found {nc}")
            except ValueError:
                errors.append("nc must be an integer.")
                
    for name, path in DIRS.items():
        if not os.path.exists(path) or not os.path.isdir(path):
            errors.append(f"Missing required directory: {path}")
        else:
            print(f"[x] Directory exists: {path}")
            
    if errors:
        print("\nCritical Errors encountered in structural scan. Exiting.")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
        
    # Task 3 & 4: Validate Image-Label Pairs & YOLO Annotations
    print("\n[Step 2] Validating Image-Label Pairs and Box Coordinates...")
    
    total_images = 0
    total_labels = 0
    missing_labels = 0
    orphan_labels = 0
    invalid_annotations = 0
    
    class_distribution = {
        "train": {0: 0, 1: 0, 2: 0},
        "val": {0: 0, 1: 0, 2: 0}
    }
    
    image_names = {"train": set(), "val": set()}
    label_names = {"train": set(), "val": set()}
    
    for sub in SUBSETS:
        sub_img_dir = DIRS[f"{sub}_images"]
        sub_lbl_dir = DIRS[f"{sub}_labels"]
        
        # Scan folders
        for f in os.listdir(sub_img_dir):
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_names[sub].add(os.path.splitext(f)[0])
                total_images += 1
                
        for f in os.listdir(sub_lbl_dir):
            if f.endswith('.txt'):
                label_names[sub].add(os.path.splitext(f)[0])
                total_labels += 1
                
        # Check duplicate mappings between train/val
        # Done at step level below
        
        # Check matching validation pairs
        for img in image_names[sub]:
            if img not in label_names[sub]:
                errors.append(f"[{sub}] Missing label for image: {img}")
                missing_labels += 1
                
        for lbl in label_names[sub]:
            if lbl not in image_names[sub]:
                errors.append(f"[{sub}] Orphan label (no matching image): {lbl}.txt")
                orphan_labels += 1
                
        # Parse validation formats
        for lbl in label_names[sub]:
            lbl_path = os.path.join(sub_lbl_dir, f"{lbl}.txt")
            if not os.path.exists(lbl_path):
                continue
                
            try:
                with open(lbl_path, 'r') as file:
                    lines = file.read().strip().split('\n')
            except Exception as e:
                errors.append(f"Unable to read label file {lbl}.txt: {e}")
                invalid_annotations += 1
                continue
                
            if not lines or (len(lines) == 1 and lines[0] == ''):
                errors.append(f"Empty label file: {lbl}.txt")
                invalid_annotations += 1
                continue
                
            for idx, line in enumerate(lines):
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) != 5:
                    errors.append(f"Malformed label in {lbl}.txt line {idx+1}: '{line}' (expected 5 items)")
                    invalid_annotations += 1
                    continue
                    
                try:
                    class_id = int(parts[0])
                    coords = [float(val) for val in parts[1:]]
                except ValueError:
                    errors.append(f"Non-numeric values in {lbl}.txt line {idx+1}: '{line}'")
                    invalid_annotations += 1
                    continue
                    
                # Class validation
                if class_id not in [0, 1, 2]:
                    errors.append(f"Invalid class ID {class_id} in {lbl}.txt line {idx+1} (only 0, 1, 2 allowed)")
                    invalid_annotations += 1
                else:
                    class_distribution[sub][class_id] += 1
                    
                # Bounding box boundaries validation
                x_center, y_center, width, height = coords
                if not (0.0 <= x_center <= 1.0):
                    errors.append(f"x_center out of bounds ({x_center}) in {lbl}.txt")
                    invalid_annotations += 1
                if not (0.0 <= y_center <= 1.0):
                    errors.append(f"y_center out of bounds ({y_center}) in {lbl}.txt")
                    invalid_annotations += 1
                if not (0.0 < width <= 1.0):
                    errors.append(f"width out of bounds ({width}) in {lbl}.txt")
                    invalid_annotations += 1
                if not (0.0 < height <= 1.0):
                    errors.append(f"height out of bounds ({height}) in {lbl}.txt")
                    invalid_annotations += 1
                    
    # Intersection check between splits
    train_val_img_leak = image_names["train"].intersection(image_names["val"])
    if train_val_img_leak:
        errors.append(f"Data Leakage: The following images exist in both train and validation: {train_val_img_leak}")
        
    train_val_lbl_leak = label_names["train"].intersection(label_names["val"])
    if train_val_lbl_leak:
        errors.append(f"Data Leakage: The following labels exist in both train and validation: {train_val_lbl_leak}")

    # Generate the validation report markdown
    report_path = os.path.join(DATASET_DIR, "DATASET_VALIDATION_REPORT.md")
    
    validation_status = "SUCCESS" if not errors else "FAILED"
    
    markdown_content = f"""# Dataset Validation Report - Smart Public Grievance Management System

This report presents a thorough, automated validation of the custom civic issues dataset and directory structures.

## Verification Status: **{validation_status}**

### Validation Metrics

| Metric | Result |
|--------|--------|
| Total Images | {total_images} |
| Training Images | {len(image_names["train"])} |
| Validation Images | {len(image_names["val"])} |
| Total Labels | {total_labels} |
| Missing Labels | {missing_labels} |
| Orphan Labels | {orphan_labels} |
| Invalid Annotations | {invalid_annotations} |

---

### Class Distribution Details

| Class | Train Annotations | Validation Annotations |
|-------|-------------------|------------------------|
| Pothole (Class 0) | {class_distribution["train"][0]} | {class_distribution["val"][0]} |
| Electricity (Class 1) | {class_distribution["train"][1]} | {class_distribution["val"][1]} |
| Water Leakage (Class 2) | {class_distribution["train"][2]} | {class_distribution["val"][2]} |
| **TOTAL** | **{sum(class_distribution["train"].values())}** | **{sum(class_distribution["val"].values())}** |

---

## Detailed Evaluation Log

"""
    if errors:
        markdown_content += "### Critical Errors Encountered\n"
        for err in errors:
            markdown_content += f"- [!] **ERROR:** {err}\n"
    else:
        markdown_content += "### Verification Details\n"
        markdown_content += "- [x] Directory structure matching YOLO requirements: **PASS**\n"
        markdown_content += "- [x] No data leakage detected between Train/Validation splits: **PASS**\n"
        markdown_content += "- [x] Coordinate values normalization validation: **PASS**\n"
        markdown_content += "- [x] Class ID consistency (all bounding boxes are strictly Pothole, Electricity, or Water Leakage): **PASS**\n"
        markdown_content += "\n**The dataset is completely healthy and prepared for customized custom YOLOv8 model training!**\n"

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
        
    print(f"\nWritten verification report to: {report_path}")
    
    # Step 3: Output CLI Summary
    print("\n==================================================")
    print("VALIDATION SUMMARY")
    print("==================================================")
    print(f"Total Images: {total_images}")
    print(f"Total Labels: {total_labels}")
    print(f"Missing Labels: {missing_labels}")
    print(f"Orphan Labels: {orphan_labels}")
    print(f"Invalid Annotations: {invalid_annotations}")
    
    print("\nClass distribution per split:")
    print(f"  Pothole: Train={class_distribution['train'][0]}, Val={class_distribution['val'][0]}")
    print(f"  Electricity: Train={class_distribution['train'][1]}, Val={class_distribution['val'][1]}")
    print(f"  Water Leakage: Train={class_distribution['train'][2]}, Val={class_distribution['val'][2]}")
    
    if errors:
        print("\n[CRITICAL ERROR] Dataset validation FAILED.")
        for err in errors[:10]:
            print(f" - {err}")
        if len(errors) > 10:
            print(f" - And {len(errors) - 10} more errors...")
        sys.exit(1)
    else:
        print("\n[SUCCESS] Dataset validation passed perfectly! Model training is ready.")
        sys.exit(0)

if __name__ == "__main__":
    validate()
