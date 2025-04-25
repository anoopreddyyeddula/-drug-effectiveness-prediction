
import gradio as gr
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Prediction function
def predict_effectiveness(drug_name, condition):
    input_text = drug_name + " " + condition
    prediction = model.predict([input_text])[0]
    return f"Predicted Effectiveness: {prediction}"

# Gradio Interface
iface = gr.Interface(
    fn=predict_effectiveness,
    inputs=[
        gr.Textbox(label="Drug Name"),
        gr.Textbox(label="Condition")
    ],
    outputs="text",
    title="Drug Effectiveness Prediction System",
    description="Enter the drug name and the medical condition to predict how effective the drug might be.",
    allow_flagging="never"
)

# Launch the app
if __name__ == "__main__":
    iface.launch()
