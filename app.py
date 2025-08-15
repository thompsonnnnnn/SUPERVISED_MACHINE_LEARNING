import streamlit as st
import joblib
import json
from pathlib import Path
import pandas as pd

# --- Paths (safe regardless of where you run from) ---
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "artifacts" / "best_weather_model.pkl"
META_PATH = BASE_DIR / "artifacts" / "metadata.json"



# --- Load Model & Metadata ---
try:
    model = joblib.load(MODEL_PATH)
    with open(META_PATH, "r") as f:
        metadata = json.load(f)
except FileNotFoundError:
    st.error("Model or metadata not found. Please ensure training has been run and 'artifacts/' exists.")
    st.stop()

st.title("🏏 Proven Data Private Limited Sport Weather Prediction")

# --- User Inputs ---
st.subheader("Enter weather conditions:")

user_input = {}
for col, options in metadata.items():
    if all(o in ["True", "False", True, False] for o in options):
        # Boolean → Checkbox
        val = st.checkbox(col, value=False)
        user_input[col] = val
    elif all(isinstance(o, (int, float)) or str(o).isdigit() for o in options):
        # Numeric → Slider
        min_val = min([float(o) for o in options if o != ""])
        max_val = max([float(o) for o in options if o != ""])
        val = st.slider(col, min_val, max_val, min_val)
        user_input[col] = val
    else:
        # Categorical → Dropdown
        val = st.selectbox(col, options)
        user_input[col] = val

# --- Prediction ---
if st.button("Predict"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    # st.success(f"Prediction: {'✅ Yes, You can Play outside ' if prediction == 'yes' else '❌ No, Do not Play'}")
    # Display result
    if prediction.lower() == "yes":
        st.success("✅ Yes! The weather is good for outdoor sport.")
    else:
        st.error("❌ No! The weather is not suitable for outdoor sport.")

# Optional: About section
st.sidebar.header("About")
st.sidebar.info("This app predicts whether the weather is suitable for outdoor sports based on various weather conditions.")
st.markdown("---")
st.caption("Built with Streamlit • Model trained in scikit-learn")
