# FaceLikeness AI 🚀
**An AI-powered face verification tool optimized for human perception, featuring a 2-stage filtering and scoring system.**

## 🌟 Overview
**FaceLikeness AI** is a specialized tool designed to evaluate and grade the quality of AI-generated images (such as LoRA) based on how humans perceive facial similarity. 

By combining 5 top-tier models (The "Divine 5") available in DeepFace, this tool goes beyond simple data matching. It focuses on "structural fidelity" and "emotional likeness" to provide a score that truly resonates with human intuition.

## 🧠 Core Logic: The 2-Stage Algorithm
This tool uses a unique dual-layered approach to separate "imposters" from "perfection."

### Step 1: The Gatekeepers (Strict Filtering)
- **Models**: `Facenet512`, `SFace`
- **Role**: These models act as strict filters to eliminate fatal structural differences and unnatural AI artifacts.
- **Rule**: **AND Condition**. If either model identifies the subject as a "different person," the image is immediately rejected.

### Step 2: Similarity Scoring (Perceptual Evaluation)
- **Models**: `ArcFace`, `Facenet`, `VGG-Face`
- **Role**: These models evaluate the nuances and "vibe" that humans typically notice.
- **Scaling**: We use a custom non-linear calculation where the AI threshold is mapped to **60%**. This ensures that "passing" images start from a score that feels intuitive to humans.

## 🛠 Key Features
- **Multi-Target Ensemble**: Supports multiple reference images (e.g., `target1.jpg`, `target2.png`) to capture a multi-angle understanding of the subject and minimize bias.
- **Auto-Sorting & Renaming**: Automatically moves files into "Verified" (本人) and "Rejected" (別人) folders, prefixing files with their similarity scores for easy sorting.
- **Detailed Analytics**: Generates a comprehensive summary table showing Distance, Threshold, and Similarity for every model used.

## 🚀 Quick Start
1. Download the script to your local machine.
2. Place it in the folder containing the images you want to analyze.
3. Rename your reference image(s) to `target.jpg` (or `target1`, `target2`, etc.).
4. Run the script. The tool will automatically create output directories and start the sorting process.

---
## Credits
- **Planning & Configuration**: fpt-labs
- **Coding & Implementation**: Assisted by Gemini (Google Large Language Model)

*This project is a collaboration between human insight and artificial intelligence.*
