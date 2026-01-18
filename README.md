# FaceLikeness AI 🚀
**A heuristic AI tool for analyzing and organizing facial similarity, optimized for human visual perception.**

## ⚠️ IMPORTANT NOTICE (Disclaimer)
This project is intended strictly for **Personal Organization, Research, and Educational purposes.**
- ❌ **NOT** for Surveillance or Law Enforcement.
- ❌ **NOT** for Security-critical Authentication.
- ❌ **NOT** a definitive legal or medical identification tool.
- ❌ **NOT** to be used for identifying, classifying, or tracking real individuals without their explicit consent.
- ❌ **NOT** a "Face Recognition" or "Personal Identification System."

The "Similarity Score" provided by this tool is a heuristic visualization based on specific AI models and is **NOT** a statistical probability or a legal confidence level.

## 🌟 Overview
**FaceLikeness AI** is a specialized tool designed to evaluate and grade the visual quality of AI-generated images (e.g., LoRA outputs) based on how humans perceive facial likeness.

By combining an Ensemble of 5 Models, this tool goes beyond simple data matching, quantifying skeletal fidelity and emotional nuances to provide scores that resonate with human intuition.

## 🧠 Core Logic: 2-Stage Analysis

### Stage 1: Structural Filtering (Primary Check)
- **Models**: `Facenet512`, `SFace`
- **Role**: Identifies significant skeletal or structural deviations.
- **Rule**: **AND Condition**. If both models do not meet the criteria, the image is categorized as "Low Similarity."

### Stage 2: Similarity Scoring (Perceptual Evaluation)
- **Models**: `ArcFace`, `Facenet`, `VGG-Face`
- **Role**: Quantifies fine features and "vibes" that humans typically notice.
- **Scaling**: Uses a custom non-linear calculation where the AI threshold is mapped to **60%**. This ensures that images humans feel are a "pass" start from an intuitive score of 60+.

## 🛠 Directory Structure & Usage
The tool automatically creates the following folders in the same directory:

1. **1_Reference_Images**: Place your target/base image here (e.g., `target.jpg`).
2. **2_Input_Images**: Place the batch of images you want to analyze here.
3. **3_Result_Low_Similarity**: Images that do not meet the criteria are copied here.
4. **4_Result_High_Similarity**: Images that meet the criteria are copied here, prefixed with their score.

## 🚀 Quick Start
1. Place the script (or .exe) in your desired folder.
2. Put reference images in `1_Reference_Images` and targets in `2_Input_Images`.
3. Run the tool. The sorting process will begin automatically.

## 📜 Credits & Licenses
- **Planning & Configuration**: [fpt-labs](https://github.com/fpt-labs)
- **Coding & Implementation**: Assisted by Gemini (Google Large Language Model)
- **Dependencies**: This project relies on [DeepFace](https://github.com/serengil/deepface).

---
*This project is a collaboration between human insight and artificial intelligence.*
