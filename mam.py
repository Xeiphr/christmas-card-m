import streamlit as st
import time

st.set_page_config(page_title="Merry Christmas!", page_icon="🎄")

st.markdown("""
    <style>
    /* 1. The Festive Background */
    .stApp {
        background-color: #a30000;
        background-image: url("https://images.vexels.com/media/users/3/104576/raw/601231f7a7c64db42b5355996d46e049-beautiful-christmas-background.png");
        background-size: auto;
    }
    
    /* 2. Fix the top header strip to match */
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0); /* Make it transparent */
    }
    
    /* 4. Text Styling */
    h1 {
        color: white !important;
        font-family: 'Georgia', serif;
        text-shadow: 2px 2px 4px #000000;
    }
    h2, p {
        color: white !important;
        text-shadow: 1px 1px 2px #000000;
        text-align: center;
    }

    /* 5. Button Styling */
    .stButton>button {
        color: #a30000;
        background-color: red;
        border-radius: 20px;
        font-weight: bold;
        border: 2px solid gold; /* A little gold border for luxury */
        height: 3em;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

#snow falling
st.snow()

col_a, col_b, col_c = st.columns([1,1,1])
#with col_b:
    #st.image("https://cdn-icons-png.flaticon.com/512/3798/3798197.png", width=150)

#container for card
st.markdown('<div class="festive-card">', unsafe_allow_html=True)

st.title("To Mam ❤️")
st.header("Merry Christmas!")
st.write("""
Thank you for all that you do for us, we never say it enough but we are truly grateful. We couldn't ask for a better mam. We love you more than words can describe 
and hope you have an amazing Christmas filled with joy and relaxation.
""")
st.write("Speaking of relaxation...")

st.markdown('</div>', unsafe_allow_html=True)

st.write("") # Spacing

col1, col2, col3 = st.columns([0.5, 2, 0.5])

#gift reveal
with col2:
    if st.button("🎁 Click to open your gift 🎁"):
        
        st.balloons()
        
        #voucher pop up
        st.markdown("""
            <div style="background-color: #black; color: #a30000; padding: 30px; border-radius: 15px; border: 4px dashed #a30000; text-align: center; box-shadow: 0px 0px 20px gold;">
                <h2 style="color: #a30000 !important; margin: 0; text-shadow: none;">SPA VOUCHER!!!</h2>
                <h1 style="color: #d4af37 !important; margin: 10px 0; font-size: 50px; text-shadow: 1px 1px 1px #000;">205€</h1>
                <p style="color: black !important; font-size: 18px; text-shadow: none;">
                <b>For the Unique Day Spa</b><br>
                We know you've been wanting to try that Japanese Head Massage!!<br>
                <br>
                <i>Love Daniel, Sophie and Dad</i>
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        #st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmc1dnh1NHUwaTBkaTVyZG4zZmtnMGYxZm4zYnlpd3Q5cnBxdWlnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fZlP5WCnQXo2s/giphy.gif")
        st.markdown("""
            <div style="display: flex; justify-content: center;">
                <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmc1dnh1NHUwaTBkaTVyZG4zZmtnMGYxZm4zYnlpd3Q5cnBxdWlnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fZlP5WCnQXo2s/giphy.gif" width="300" style="border-radius: 15px; box-shadow: 0px 0px 15px white;">
            </div>
        """, unsafe_allow_html=True)
