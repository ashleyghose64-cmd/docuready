import streamlit as st
import pandas as pd
import urllib.parse

# --- Page Config ---
st.set_page_config(page_title="DocuReady Services", layout="wide")

# --- Custom Styling ---
st.markdown(
    """
    <style>
    body {
        background-color: #fafafa;
    }
    /* Header Layout */
    .header-container {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .header-title {
        font-size: 32px;
        font-weight: bold;
        color: #2c3e50;
        margin: 0;
    }
    .header-subtitle {
        font-size: 16px;
        color: #555;
        margin: 0;
    }
    .service-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .service-card:hover {
        transform: scale(1.01);
        box-shadow: 0px 6px 16px rgba(0,0,0,0.12);
    }
    .whatsapp-btn {
        display: inline-block;
        padding: 8px 16px;
        background-color: #25D366;
        color: white !important;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        margin-right: 10px;
    }
    .whatsapp-btn:hover {
        background-color: #1ebe5c;
    }
    .call-btn {
        display: inline-block;
        padding: 8px 16px;
        background-color: #3498db;
        color: white !important;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
    }
    .call-btn:hover {
        background-color: #217dbb;
    }
    .footer {
        background-color: #f0f0f0;
        text-align: center;
        padding: 20px;
        margin-top: 40px;
        border-radius: 10px;
        font-size: 15px;
        color: #555;
    }
    .footer a {
        color: #2c3e50;
        text-decoration: none;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header with Logo & Title ---
col1, col2 = st.columns([1, 5])
with col1:
    st.image("BLACK LOGOp.png", width=140)  # logo top-left
with col2:
    st.markdown("<h1 class='header-title'>DocuReady Services</h1>", unsafe_allow_html=True)
    st.markdown("<p class='header-subtitle'>Professional solutions tailored for individuals & small businesses.</p>", unsafe_allow_html=True)

st.write("---")

# --- Company Summary ---
st.markdown(
    """
    <div style="font-size:18px; line-height:1.6; color:#333; margin-bottom:30px;">
    At <b>DocuReady</b>, we believe that professional services should be <b>simple, reliable, and affordable</b>.  
    Whether you’re a startup looking for creative branding, a small business in need of accurate bookkeeping, or 
    an individual preparing for the next step in your career — we’ve got you covered.  

    Our team combines expertise across <b>design, finance, marketing, and technology</b> to deliver services that help 
    you focus on what matters most: <b>growing your business and achieving your goals.</b>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Services List ---
services = [
    {"Name": "Graphic Design", "Price": 5000, "Description": "Eye-catching visuals, brochures, and branding that represent your business identity."},
    {"Name": "Bookkeeping", "Price": 3000, "Description": "Hassle-free management of your accounts with accuracy and transparency."},
    {"Name": "Small Business Tax", "Price": 4000, "Description": "Stress-free tax filing and expert consultation for small enterprises."},
    {"Name": "Content Marketing", "Price": 3500, "Description": "Engaging blogs, articles, and social media strategies to boost your online presence."},
    {"Name": "Logo Design", "Price": 2000, "Description": "Unique, memorable logos that build instant brand recognition."},
    {"Name": "Web Design", "Price": 8000, "Description": "Modern, responsive websites tailored to your brand and business needs."},
    {"Name": "Resume Writing", "Price": 1500, "Description": "Compelling resumes designed to showcase your strengths and land your dream job."},
]

df = pd.DataFrame(services)

# --- Filters ---
col1, col2 = st.columns([1, 2])
with col1:
    sort_option = st.selectbox("Sort by:", ["Name", "Price"])
with col2:
    search_query = st.text_input("Search service:", "")

df = df.sort_values(by=sort_option)
if search_query:
    df = df[df["Name"].str.contains(search_query, case=False, na=False)]

# --- Display Services ---
for _, row in df.iterrows():
    st.markdown(f"""
        <div class="service-card">
            <h3 style="color:#2c3e50;">{row['Name']} - ₹{row['Price']}</h3>
            <p style="color:#555; font-size:16px;">{row['Description']}</p>
            <a class="whatsapp-btn" href="https://wa.me/919004804043?text={urllib.parse.quote('Hello! I would like to avail the service: ' + row['Name'] + ' from DocuReady.')}" target="_blank">💬 WhatsApp</a>
            <a class="call-btn" href="tel:+919004804043">📞 Call Now</a>
        </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown(
    """
    <div class="footer">
        <p>📧 Contact us: <a href="mailto:info@docuready.shop">info@docuready.shop</a></p>
        <p>💬 WhatsApp: <a href="https://wa.me/919004804043" target="_blank">+91 90048 04043</a> | 📞 Call: <a href="tel:+919004804043">+91 90048 04043</a></p>
        <p>© 2025 DocuReady • All Rights Reserved</p>
    </div>
    """,
    unsafe_allow_html=True,
)
