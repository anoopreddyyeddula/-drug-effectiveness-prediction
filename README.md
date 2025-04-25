---
title: Drug Effectiveness Prediction System
emoji: 💊
colorFrom: pink
colorTo: purple
sdk: gradio
sdk_version: 5.27.0
app_file: app.py
pinned: false
---

# Drug Effectiveness Prediction System 🚀

This project predicts how effective a drug will be for a specific medical condition using machine learning.

## How It Works
- Input the **Drug Name** and **Medical Condition**.
- The system predicts the likely **Effectiveness**: `Effective`, `Neutral`, or `Not Effective`.

## Technologies Used
- Random Forest Classifier
- TF-IDF Text Vectorization
- Gradio for User Interface
- Deployed on Hugging Face Spaces

## How to Run
If you want to run locally:
```bash
pip install -r requirements.txt
python app.py
```

Otherwise, it runs automatically on Hugging Face Spaces! 🚀

## Example
| Drug Name  | Condition           | Predicted Effectiveness |
|------------|---------------------|--------------------------|
| Mirtazapine | Depression          | Effective |
| Bactrim     | Urinary Tract Infection | Effective |

---

Made with ❤️ by Anoop Reddy