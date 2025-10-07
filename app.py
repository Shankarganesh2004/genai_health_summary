import streamlit as st
from utils.ocr import extract_from_image
from utils.interpret import interpret_values
from utils.genai import generate_summary
import pandas as pd

st.set_page_config(page_title="GenAI Blood Report Assistant", layout="wide")
st.title("🧠 GenAI Blood Report Assistant")
st.markdown("Upload your blood report or enter values manually to get a preliminary interpretation.")

# Sidebar for input mode
mode = st.sidebar.radio("Choose Input Mode", ["📤 Upload Image", "✍️ Manual Entry"])

if mode == "📤 Upload Image":
    uploaded_file = st.file_uploader("Upload Blood Report Image", type=["jpg", "png", "jpeg", "pdf"])
    if uploaded_file:
        with st.spinner("🔍 Extracting data..."):
            extracted_data = extract_from_image(uploaded_file)
        st.success("✅ Data extracted")
        st.dataframe(extracted_data)

elif mode == "✍️ Manual Entry":
    st.subheader("Enter Blood Test Values")
    fields = ["Hemoglobin (g/dL)", "Glucose (mg/dL)", "HbA1c (%)", "ALT (U/L)", "Platelets (10^3/μL)"]
    user_input = {}
    for field in fields:
        user_input[field] = st.number_input(field, min_value=0.0, step=0.1)
    extracted_data = pd.DataFrame([user_input])

# Interpretation and GenAI Output
if st.button("🧠 Analyze Report"):
    with st.spinner("🔬 Interpreting values..."):
        interpretation = interpret_values(extracted_data)
    with st.spinner("💬 Generating summary..."):
        summary = generate_summary(interpretation)
    st.subheader("🩺 Interpretation")
    st.json(interpretation)
    st.subheader("🧠 GenAI Summary")
    st.markdown(summary)
    st.markdown("⚠️ *This is not medical advice. Please consult a physician for diagnosis.*")