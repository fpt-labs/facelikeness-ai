# FaceLikeness AI 🚀
**A heuristic tool for facial similarity analysis and photo organization, optimized for human perception.**

## ⚠️ IMPORTANT NOTICE (Disclaimer)
This project is strictly for **Personal Organization, Research, and Educational purposes.**
- ❌ **NOT** for Surveillance or Law Enforcement.
- ❌ **NOT** for Security-critical Authentication.
- ❌ **NOT** a definitive legal identification tool.

The "Similarity Score" is a heuristic visualization based on specific AI models and is **NOT** a statistical probability or a confidence level.

## 🌟 Overview
**FaceLikeness AI** is a specialized tool designed to evaluate and grade the visual similarity of images (such as AI-generated LoRA outputs) based on how humans perceive facial likeness.

By combining 5 professional models available in DeepFace, this tool focuses on "structural fidelity" and "perceptual resemblance" to provide a score that aligns with human intuition.

## 🧠 Core Logic: 2-Stage Analysis

### Stage 1: Structural Filtering (Primary Check)
- **Models**: `Facenet512`, `SFace`
- **Role**: These models act as filters to identify significant structural deviations.
- **Rule**: **AND Condition**. If the similarity in these models is below the threshold, the image is categorized as "Low Similarity."

### Stage 2: Similarity Scoring (Perceptual Evaluation)
- **Models**: `ArcFace`, `Facenet`, `VGG-Face`
- **Role**: These models evaluate nuances and features that humans typically notice.
- **Scaling**: Uses a custom non-linear calculation where the AI distance threshold is mapped to **60%**. This ensures "High Similarity" images start from a score that feels intuitive to users.

## 🛠 Key Features
- **Multi-Target Ensemble**: Supports multiple reference images (e.g., `target1.jpg`, `target2.png`) to capture a multi-angle understanding of the subject.
- **Auto-Sorting**: Automatically copies files into `4_Result_High_Similarity` and `3_Result_Low_Similarity` folders based on the 2-stage analysis.
- **Renaming**: Prefixes files with their calculated scores (e.g., `85_image.png`) for easy sorting.

## 🚀 Quick Start
1. Download the script.
2. Place it in the folder containing the images you want to analyze.
3. Place your reference image(s) in the `1_Reference_Images` folder as `target.jpg` (or `target1`, `target2`, etc.).
4. Run the script. The tool will automatically create directories and start the process.

## 📜 Credits & Licenses
- **Planning & Configuration**: [fpt-labs](https://github.com/fpt-labs)
- **Coding & Implementation**: Assisted by Gemini (Google Large Language Model)
- **Dependencies**: This project relies on [DeepFace](https://github.com/serengil/deepface). Please refer to the original papers and licenses of each model (VGG-Face, Facenet, etc.) before any commercial use.

---
*This project is a collaboration between human insight and artificial intelligence.*
