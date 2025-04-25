
# 💊 Drug Effectiveness Prediction System

This project predicts how effective a drug will be for a specific medical condition using machine learning.

---

## 🚀 How It Works
- Enter the **Drug Name** and **Medical Condition**.
- The system predicts the likely **Effectiveness**: `Effective`, `Neutral`, or `Not Effective`.

---

## 🛠️ Technologies Used
- Logistic Regression Classifier (Scikit-learn)
- TF-IDF Text Vectorization
- Gradio for User Interface
- joblib for Model Serialization
- Deployed using Hugging Face Spaces

---

## 📁 Project Structure

```
├── app.py                # Gradio Web App
├── model.pkl             # Saved Logistic Regression model with TF-IDF
├── requirements.txt      # Python dependencies
└── README.md             # Project Documentation
```

---

## 📦 Installation & Running Locally

1. Clone the repository:
```bash
git clone https://github.com/your-username/drug-effectiveness-prediction.git
cd drug-effectiveness-prediction
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

The app will launch on `localhost` and you can interact via a web browser.

---

## 📊 Example

| Drug Name   | Condition                  | Predicted Effectiveness |
|-------------|-----------------------------|--------------------------|
| Mirtazapine | Depression                  | Effective                |
| Bactrim     | Urinary Tract Infection     | Effective                |

---

## 🌟 Features
- Lightweight Machine Learning model
- Fast text-based predictions
- Easy-to-use Web Interface
- Free public deployment via Hugging Face Spaces

---

## 🔗 Deployment
- Live on [Hugging Face Spaces](https://huggingface.co/spaces/anoopreddyyeddula/Fitness-and-Nutrition-Coaching-Assistant) 🚀

---

## 👨‍💻 Author

Made by [Anoop Reddy](https://github.com/anoopreddyyeddula)

---
