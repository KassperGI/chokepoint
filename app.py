import streamlit as st
from google import genai
import os

# Set up the Gemini client
client = genai.Client()

# Set page config
st.set_page_config(page_title="ChokePoint | Hardware Roaster", page_icon="💀", layout="centered")

# --- CUSTOM CSS INJECTION ---
# This gives the app its aggressive neon personality
st.markdown("""
<style>
    /* Glowing Title */
    h1 {
        text-shadow: 0px 0px 20px #ff4b4b;
        color: #ff4b4b !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    /* Neon Hazardous Button */
    .stButton > button {
        border: 2px solid #ff4b4b !important;
        background-color: transparent !important;
        color: #ff4b4b !important;
        box-shadow: 0px 0px 10px #ff4b4b inset, 0px 0px 10px #ff4b4b;
        transition: all 0.3s ease;
        font-weight: bold;
        letter-spacing: 1px;
        width: 100%;
    }
    
    /* Button Hover Effect */
    .stButton > button:hover {
        background-color: #ff4b4b !important;
        color: #0e1117 !important;
        box-shadow: 0px 0px 25px #ff4b4b inset, 0px 0px 25px #ff4b4b;
        transform: scale(1.02);
    }
    
    /* Make input borders glow red when clicked */
    .stTextInput>div>div>input:focus, .stSelectbox>div>div>div:focus {
        border-color: #ff4b4b !important;
        box-shadow: 0 0 10px #ff4b4b !important;
    }
    
    /* Subheader styling */
    h3 {
        color: #a0a0a5 !important;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)
# ----------------------------

st.title("ChokePoint")
st.subheader("The brutal hardware bottleneck analyzer.")
st.markdown("---") 

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

# The button is now full-width and glowing red due to the CSS above
if st.button("INITIATE BRUTAL ANALYSIS"):
    if cpu and gpu and storage and price:
        prompt = f"""
        You are a sarcastic, slightly aggressive hardware engineer. Analyze these specs for the chosen workload.
        Specs: CPU: {cpu}, GPU: {gpu}, RAM: {ram}, Storage: {storage}. 
        Workload: {workload}. Estimated Price: {price}.
        
        Output in exactly three short sections using Markdown headings:
        ### THE ROAST
        Point out the exact bottleneck mercilessly. Be funny but technically accurate.
        
        ### THE FIX
        The most practical component upgrade path.
        
        ### THE VALUE CHECK
        Brutally honest verdict on whether they are overpaying, getting scammed, or finding a rare good deal for {price}.
        """
        
        with st.spinner("Compiling insults and evaluating your silicon..."):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                st.success("Target acquired. Commencing roast.") 
                st.write(response.text)
            except Exception as e:
                st.error(f"API Error. Details: {e}")
    else:
        st.error("ACCESS DENIED. Fill out all the hardware fields first!")