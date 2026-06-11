import streamlit as st
from google import genai
import time
import os

# Set up the Gemini client
client = genai.Client()

# Set page config
st.set_page_config(page_title="ChokePoint | Hardware Diagnostic", page_icon="⚙️", layout="wide")

# --- NOTHING TECH AESTHETIC CSS INJECTION ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Major+Mono+Display&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cutive+Mono&display=swap');
    
    html, body, [class*="css"] {
        background-color: #000000 !important;
        color: #ffffff !important;
        font-family: 'Cutive+Mono', monospace !important;
        font-size: 18px !important;
        line-height: 1.5;
    }
    
    h1 {
        font-family: 'Major Mono Display', monospace !important;
        font-size: 80px !important;
        color: #ffffff !important;
        text-align: center;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-top: 50px;
        margin-bottom: 10px !important;
    }

    h3 {
        font-family: 'Cutive+Mono', monospace !important;
        color: #ffffff !important;
        text-align: center;
        font-size: 26px !important;
        margin-bottom: 60px !important;
        font-weight: normal;
    }

    h4 {
        font-family: 'Major Mono Display', monospace !important;
        color: #777777 !important;
        font-size: 22px !important;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 40px !important;
        margin-bottom: 20px !important;
        text-align: left;
    }

    /* Standard text inputs */
    .stTextInput>div>div>input {
        background-color: #000000 !important;
        border: 1px solid #777777 !important;
        color: #ffffff !important;
        border-radius: 0px !important;
        padding: 15px !important;
        font-size: 18px !important;
        transition: border-color 0.2s ease;
    }

    /* Select box adjustment to prevent text clipping */
    .stSelectbox>div>div>div {
        background-color: #000000 !important;
        border: 1px solid #777777 !important;
        color: #ffffff !important;
        border-radius: 0px !important;
        padding: 6px 15px !important; /* Reduced vertical padding */
        font-size: 18px !important;
        min-height: 56px !important; /* Ensures plenty of room for text */
        display: flex !important;
        align-items: center !important;
        transition: border-color 0.2s ease;
    }

    .stTextInput>div>div>input:focus, .stSelectbox>div>div>div:focus {
        border-color: #ffffff !important;
        box-shadow: none !important;
    }

    .stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-family: 'Major Mono Display', monospace !important;
        font-size: 28px !important;
        padding: 15px 40px !important;
        border-radius: 0px !important;
        border: 1px solid #ffffff !important;
        width: 100%;
        margin-top: 50px;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    .stProgress > div > div > div > div {
        background-color: #ffffff !important;
        border-radius: 0px !important;
        height: 8px;
    }

    .ai-output-section {
        background-color: #111111;
        border: 1px solid #777777;
        padding: 25px;
        margin-bottom: 30px;
    }

    .ai-output-section h3 {
        font-family: 'Major Mono Display', monospace !important;
        color: #ff4b4b !important;
        font-size: 28px !important;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 15px;
        text-align: left;
    }

    .ai-output-section p {
        color: #ffffff;
        font-size: 18px;
        line-height: 1.6;
    }
    
    .fact-box {
        background-color: #111111;
        border: 2px solid #ff4b4b;
        padding: 20px;
        margin-top: 30px;
        color: #ffffff;
        font-size: 22px;
        text-align: center;
        border-radius: 0px;
    }

    .horizontal-line {
        border-bottom: 1px solid #777777;
        margin: 50px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>CHOKEPOINT</h1>", unsafe_allow_html=True)
st.markdown("<h3>>>> BRUTAL HARDWARE BOTTLENECK DIAGNOSTIC <<<</h3>", unsafe_allow_html=True)
st.markdown("<div class='horizontal-line'></div>", unsafe_allow_html=True)

# MODULAR GRID LAYOUT
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h4>>>> SYSTEM SPECIFICATIONS <<<</h4>", unsafe_allow_html=True)
    cpu = st.text_input("CPU / central processing unit", placeholder="e.g., Ryzen 7 5700X")
    gpu = st.text_input("GPU / graphics processing unit", placeholder="e.g., RTX 3070 Ti")

with col2:
    st.markdown("<h4>>>> OPERATIONAL USE CASE <<<</h4>", unsafe_allow_html=True)
    ram = st.selectbox("MEMORY / sys_mem (GB)", ["4", "8", "16", "32", "64", "128"])
    storage = st.text_input("STORAGE / non-volatile_sys_drive", placeholder="e.g., 2TB NVMe SSD")

with col3:
    st.markdown("<h4>>>> ACQUISITION PARAMETERS <<<</h4>", unsafe_allow_html=True)
    workload = st.selectbox("OPERATIONAL_USE_CASE / mission_type", [
        "3D Rendering & Animation", 
        "Video Editing", 
        "Software Development",
        "AAA Gaming"
    ])
    price = st.text_input("COINS EXPENDED / current_acquisition_cost", placeholder="e.g., $1800 or ₹1,40,000")

st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("RUN DIAGNOSTIC PROTOCOL"):
    if cpu and gpu and storage and price:
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.markdown("<h3>>>> INITIATING DIAGNOSTIC... <<<</h3>", unsafe_allow_html=True)
        time.sleep(0.3)
        progress_bar.progress(25)
        
        status_text.markdown("<h3>>>> ISOLATING PERFORMANCE BOTTLENECKS... <<<</h3>", unsafe_allow_html=True)
        time.sleep(0.3)
        progress_bar.progress(50)
        
        status_text.markdown("<h3>>>> CALCULATING FINANCIAL EFFICIENCY... <<<</h3>", unsafe_allow_html=True)
        time.sleep(0.3)
        progress_bar.progress(80)
        
        status_text.markdown("<h3>>>> COMPILING INSULTS... <<<</h3>", unsafe_allow_html=True)
        time.sleep(0.3)
        progress_bar.progress(100)

        prompt = f"""
        You are a cold, calculated, authoritarian system diagnostic AI analyzing PC specifications.
        Specs: CPU: {cpu}, GPU: {gpu}, RAM: {ram}GB, Storage: {storage}. 
        Operational Use Case (Workload): {workload}. Listed Price: {price}.
        
        Evaluate the system balance and price-to-performance ratio. 
        Output four distinct, short sections in Markdown, framing your response as precise technical analysis. Do NOT use emojis.
        
        ### PERFORMANCE DIAGNOSTIC (SYSTEM EVALUATION)
        If the build is unbalanced or the hardware is weak for the workload: Point out the central limitation with icy, authoritarian sarcasm (Roast them).
        If the build is well-balanced, powerful, and highly appropriate for the workload: Issue a cold, calculated compliment acknowledging their technical competence. State that the system parameters are "ACCEPTABLE."
        
        ### REQUIRED OPTIMIZATION (THE FIX)
        If a bottleneck exists: The primary prioritized component upgrade required.
        If the build is already perfect: State "NO ALTERATIONS REQUIRED. SYSTEM OPTIMIZED."
        
        ### FINANCIAL AUDIT (VALUE CHECK)
        Brutal verdict on whether their listed price of {price} is a financial scam, an average market rate, or a highly efficient acquisition.
        
        ### FAIR ACQUISITION VALUE (RECOMMENDATION)
        Provide a realistic, fair market price range (matching the currency system they typed in: {price}) that they SHOULD ideally be paying for these exact components in today's market.
        """
        
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            
            status_text.empty()
            progress_bar.empty()
            st.success(">>> SYSTEM CHECK COMPLETE. <<<") 
            
            diagnostic_output = response.text
            sections = diagnostic_output.split('###')
            
            for section in sections[1:]:
                if section.strip():
                    heading, text = section.strip().split('\n', 1)
                    if "FAIR ACQUISITION VALUE" in heading:
                        st.markdown(f"<div class='fact-box'><h3>>>> {heading.strip()} <<<</h3><p>{text.strip()}</p></div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div class='ai-output-section'><h3>>>> {heading.strip()} <<<</h3><p>{text.strip()}</p></div>", unsafe_allow_html=True)
                        
        except Exception as e:
            st.error(f"SYSTEM FAILURE. Details: {e}")
    else:
        st.error(">>> ERROR: INCOMPLETE LOADOUT. EQUIP ALL ITEMS PROTOCOL FAILED. <<<")