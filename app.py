import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="DocuReady", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
        /* Off-white background */
        .stApp {
            background-color: #f8f9fa;
        }

        /* Centered header with logo */
        .header-container {
            display: flex;
            align-items: center;
            padding: 10px 20px;
        }
        .header-logo {
            width: 120px;
            margin-right: 15px;
        }
        .header-title {
            font-size: 28px;
            font-weight: bold;
            color: #222;
        }

        /* Card style */
        .card {
            background-color: #fff;
            border-radius: 10px;
            padding: 20px;
            margin: 15px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            transition: transform 0.2s ease-in-out;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        }
        .card-title {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 5px;
        }
        .card-subtitle {
            font-size: 14px;
            color: #555;
            margin-bottom: 10px;
        }
        .card-price {
            font-size: 16px;
            font-weight: bold;
            color: #28a745;
            margin-bottom: 10px;
        }
        .add-btn {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 6px;
            background-color: #28a745;
            color: white;
            font-weight: 500;
            text-decoration: none;
        }
        .add-btn:hover {
            background-color: #218838;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
col1, col2 = st.columns([1,6])
with col1:
    st.image("assets/logo.png", width=100)
with col2:
    st.markdown("<div class='header-title'>DocuReady</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------- CARD DATA ----------
services = [
    {"title": "Contract Review", "subtitle": "Fast AI-powered insights", "price": "₹999"},
    {"title": "Document Drafting", "subtitle": "Custom templates in minutes", "price": "₹1499"},
    {"title": "Compliance Check", "subtitle": "Stay legally safe", "price": "₹1299"},
    {"title": "Legal Summaries", "subtitle": "Concise & clear reports", "price": "₹799"},
    {"title": "Business Docs", "subtitle": "MOUs, NDAs, Agreements", "price": "₹1599"},
    {"title": "24/7 Support", "subtitle": "WhatsApp, Call & Email help", "price": "Free"}
]

# ---------- RENDER CARDS ----------
cols = st.columns(3)

for i, service in enumerate(services):
    with cols[i % 3]:
        st.markdown(f"""
            <div class='card'>
                <div class='card-title'>{service['title']}</div>
                <div class='card-subtitle'>{service['subtitle']}</div>
                <div class='card-price'>{service['price']}</div>
                <a href='#' class='add-btn'>Select</a>
            </div>
        """, unsafe_allow_html=True)
