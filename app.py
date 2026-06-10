import streamlit as st
from google import genai
import time

client = genai.Client()

st.set_page_config(page_title="ChokePoint | Hardware Roaster", page_icon="🕹️", layout="centered")

# --- ARCADE CSS INJECTION ---
st.markdown("""
<style>
    /* Import retro arcade font from Google */
    @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
    
    /* Apply font to everything */
    html, body, [class*="css"] {
        font-family: 'VT323', monospace !important;
        font-size: 22px !important;
    }
    
    /* Glowing Arcade Title */
    h1 {
        font-size: 70px !important;
        text-shadow: 4px 4px 0px #880000, 0px 0px 20px #ff0000;
        color: #ff4b4b !important;
        text-align: center;
        letter-spacing: 4px;
        margin-bottom: 0px !important;
    }

    h3 {
        color: #ff9999 !important;
        text-align: center;
        font-size: 28px !important;
    }

    /* Chunky Arcade Inputs */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #1a0000 !important;
        border: 2px solid #ff4b4b !important;
        color: #ffffff !important;
        border-radius: 0px !important;
        padding: 10px !important;
        box-shadow: 3px 3px 0px #ff4b4b;
        font-size: 20px !important;
    }

    /* The "Insert Coin" Button */
    .stButton > button {
        background-color: #000000 !important;
        border: 4px solid #ff4b4b !important;
        color: #ff4b4b !important;
        font-family: 'VT323', monospace !important;
        font-size: 32px !important;
        padding: 15px 30px !important;
        border-radius: 0px !important;
        box-shadow: 6px 6px 0px #880000;
        transition: all 0.1s ease-in-out;
        width: 100%;
        margin-top: 20px;
    }
    
    /* Button click physical pressing effect */
    .stButton > button:active {
        transform: translate(6px, 6px);
        box-shadow: 0px 0px 0px #880000;
    }

    .stButton > button:hover {
        background-color: #ff4b4b !important;
        color: #000 !important;
        text-shadow: none !important;
    }
    
    /* Subtle CRT Scanlines */
    .block-container {
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%);
        background-size: 100% 4px;
    }
</style>
""", unsafe_allow_html=True)
# ----------------------------

st.markdown("<h1>CHOKEPOINT</h1>", unsafe_allow_html=True)
st.markdown("<h3>>>> SYSTEM LOADOUT SELECTOR <<<</h3>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# UI Inputs themed like a game loadout
col1, col2 = st.columns(2)

with col1:
    cpu = st.text_input("PLAYER CPU", placeholder="e.g., Ryzen 5 5600X")
    gpu = st.text_input("PLAYER GPU", placeholder="e.g., RTX 4060")
    ram = st.selectbox("SYSTEM MEMORY", ["4GB", "8GB", "16GB", "32GB", "64GB", "128GB"])

with col2:
    storage = st.text_input("STORAGE DRIVE", placeholder="e.g., 1TB NVMe SSD")
    workload = st.selectbox("MISSION TYPE (WORKLOAD)", [
        "3D Rendering & Animation", 
        "Video Editing", 
        "Software Development",
        "AAA Gaming"
    ])
    price = st.text_input("COINS EXPENDED (PRICE)", placeholder="e.g., $1200 or ₹90,000")

# The Big Arcade Button
if st.button("INSERT COIN TO ANALYZE"):
    if cpu and gpu and storage and price:
        
        # --- THE GAMIFIED LOADING ANIMATION ---
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.markdown("<h3>[SCANNING CPU ARCHITECTURE...]</h3>", unsafe_allow_html=True)
        time.sleep(0.6)
        progress_bar.progress(25)
        
        status_text.markdown("<h3>[STRESS TESTING GPU VRAM...]</h3>", unsafe_allow_html=True)
        time.sleep(0.6)
        progress_bar.progress(50)
        
        status_text.markdown("<h3>[MOCKING THERMAL PERFORMANCE...]</h3>", unsafe_allow_html=True)
        time.sleep(0.6)
        progress_bar.progress(80)
        
        status_text.markdown("<h3>[CALCULATING FINANCIAL RUIN...]</h3>", unsafe_allow_html=True)
        time.sleep(0.6)
        progress_bar.progress(100)
        # --------------------------------------

        prompt = f"""
        You are an aggressive, arcade-style AI boss. Analyze these specs for the chosen mission.
        Specs: CPU: {cpu}, GPU: {gpu}, RAM: {ram}, Storage: {storage}. 
        Mission (Workload): {workload}. Price: {price}.
        
        Output in exactly three short sections using Markdown headings:
        ###  THE ROAST
        Point out the exact bottleneck mercilessly like a video game villain.
        
        ###  UPGRADE TREE
        The most practical component upgrade path to defeat the bottleneck.
        
        ###  MERCHANT APPRAISAL
        Brutally honest verdict on whether they got scammed by the merchant or found a rare loot drop for {price}.
        """
        
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            # Clear the loading animations
            status_text.empty()
            progress_bar.empty()
            
            st.success(">>> GAME OVER. READ AND WEEP. <<<") 
            st.write(response.text)
        except Exception as e:
            st.error(f"SYSTEM FAILURE. Details: {e}")
    else:
        st.error(">>> ERROR: INCOMPLETE LOADOUT. EQUIP ALL ITEMS FIRST. <<<")