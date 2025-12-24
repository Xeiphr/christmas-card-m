import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

# --- CONFIGURATION & ASSETS ---
st.set_page_config(page_title="Holiday Greetings", page_icon="🎄", layout="centered")

# 1. THE "LOTTIE" LOADER
# Lottie files are lightweight, high-quality animations. 
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load assets (free animations from LottieFiles)
lottie_santa = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_tijmpky4.json")
lottie_gift = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_p5tali1o.json")

# 2. CUSTOM CSS INJECTION
# This hides the standard Streamlit menu and sets a festive background.
st.markdown("""
    <style>
        /* Change background color to a deep festive red or snowy white */
        .stApp {
            background-color: #D32F2F; 
        }
        /* Style the main title */
        h1 {
            color: #FFFFFF;
            font-family: 'Helvetica', sans-serif;
            text-align: center;
            text-shadow: 2px 2px 4px #000000;
        }
        /* Style standard text */
        p {
            color: #FFEBEE;
            font-size: 1.2rem;
            text-align: center;
        }
        /* Custom button styling */
        .stButton>button {
            color: #D32F2F;
            background-color: white;
            border-radius: 20px;
            height: 3em;
            width: 100%;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- APP LOGIC ---

# 3. URL PERSONALIZATION
# Allow the URL to determine the name (e.g. app.py?name=Grandma)
# If no name is in the link, default to "Friend"
query_params = st.query_params
name = query_params.get("name", "Friend")

# 4. SESSION STATE (The "Unwrapping" Logic)
# We use session_state to remember if the gift has been opened
if 'gift_opened' not in st.session_state:
    st.session_state.gift_opened = False

def open_gift():
    st.session_state.gift_opened = True

# --- THE LAYOUT ---

# Header
st.title(f"❄️ Happy Holidays, Mam! ❄️")

# We use columns to center content perfectly
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if not st.session_state.gift_opened:
        # STATE 1: THE CLOSED GIFT
        st.markdown("### I have a surprise for you...")
        st_lottie(lottie_gift, height=200, key="gift")
        
        # The button triggers the state change
        st.button("🎁 TAP TO UNWRAP 🎁", on_click=open_gift)
        
    else:
        # STATE 2: THE REVEAL
        # Trigger effects immediately
        st.snow()
        
        st.markdown("### ✨ Wishing you a magical 2026! ✨")
        st_lottie(lottie_santa, height=300, key="santa")
        
        st.markdown("""
        > "May your code compile on the first try, 
        > and your coffee always be hot."
        """)
        
        if st.button("Close Gift 🔄"):
            st.session_state.gift_opened = False
            st.rerun()

# Footer
st.markdown("---")
st.markdown(f"Made with ❤️ and Python for {name}")