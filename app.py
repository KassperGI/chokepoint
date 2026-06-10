import streamlit as st
from google import genai
import os

client = genai.Client()

st.set_page_config(page_title="ChokePoint | Hardware Roaster", page_icon="💀", layout="centered")

st.title("💀 ChokePoint")
st.subheader("The brutal hardware bottleneck analyzer.")
st.markdown("---") # Adds a clean horizontal line

# UI Inputs
col1, col2 = st.columns(2)

with col1:
    cpu = st.text_input("CPU", placeholder="e.g., Core i5-11400H")
    gpu = st.text_input("GPU", placeholder="e.g., RTX 3060")
    ram = st.selectbox("RAM", ["4GB", "8GB", "16GB", "32GB", "64GB", "128GB"])

with col2:
    storage = st.text_input("Storage", placeholder="e.g., 512GB NVMe SSD")
    workload = st.selectbox("Primary Use Case", [
        "3D Rendering & Animation", 
        "Video Editing", 
        "Software Development",
        "AAA Gaming"
    ])
    price = st.text_input("Estimated Price/Budget", placeholder="e.g., $1000 or ₹80,000")

st.markdown("---")

if st.button("🔥 Analyze My Build"):
    if cpu and gpu and storage and price:
        prompt = f"""
        You are a sarcastic hardware engineer. Analyze these specs for the chosen workload.
        Specs: CPU: {cpu}, GPU: {gpu}, RAM: {ram}, Storage: {storage}. 
        Workload: {workload}. Estimated Price: {price}.
        
        Output in exactly three short sections:
        1. THE ROAST: Point out the exact bottleneck mercilessly.
        2. THE FIX: The most practical component upgrade path.
        3. THE VALUE CHECK: Brutally honest verdict on whether they are overpaying, getting scammed, or finding a rare good deal for {price}.
        """
        
        # Changed the spinner text to fit the personality
        with st.spinner("Compiling insults and evaluating your silicon..."):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                st.success("Analysis Complete.") # Adds a nice green checkmark box
                st.write(response.text)
            except Exception as e:
                st.error(f"API Error. Details: {e}")
    else:
        st.warning("Don't waste my time. Fill out all the fields first!")