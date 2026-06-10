import streamlit as st
from google import genai
import os

# Set up the Gemini client
client = genai.Client()

st.title("ChokePoint")
st.subheader("The brutal hardware bottleneck analyzer.")

# UI Inputs
cpu = st.text_input("CPU", placeholder="e.g., Core i5-11400H")
gpu = st.text_input("GPU", placeholder="e.g., GTX 1650")
ram = st.selectbox("RAM", ["4GB", "8GB", "16GB", "32GB", "64GB"])
storage = st.text_input("Storage", placeholder="e.g., 512GB NVMe SSD")
workload = st.selectbox("Primary Use Case", [
    "3D Rendering & Animation", 
    "Video Editing", 
    "Software Development",
    "AAA Gaming"
])

if st.button("Analyze My Build"):
    if cpu and gpu and storage:
        prompt = f"""
        You are a sarcastic hardware engineer. Analyze these specs for the chosen workload.
        Specs: CPU: {cpu}, GPU: {gpu}, RAM: {ram}, Storage: {storage}. Workload: {workload}.
        
        Output in two short sections:
        1. THE ROAST: Point out the exact bottleneck mercilessly.
        2. THE FIX: The most practical component upgrade path.
        """
        
        with st.spinner("Evaluating your silicon..."):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                st.write(response.text)
            except Exception as e:
                st.error(f"API Error. Did you set your API key? Details: {e}")
    else:
        st.warning("Fill out all fields first!")