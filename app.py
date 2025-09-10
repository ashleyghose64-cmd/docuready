import streamlit as st
import pandas as pd
import urllib.parse

# --- Company Info ---
st.title("DocuReady Services")
st.write("**DocuReady** offers professional solutions for your business needs, including graphic design, bookkeeping, tax services, content marketing, web development, and more.")

# --- Sample Services List ---
services = [
    {"Name": "Graphic Design", "Price": 5000, "Description": "Professional graphics and branding."},
    {"Name": "Bookkeeping", "Price": 3000, "Description": "Accurate accounting for small businesses."},
    {"Name": "Small Business Tax", "Price": 4000, "Description": "Tax filing and consultation services."},
    {"Name": "Content Marketing", "Price": 3500, "Description": "Boost your brand with targeted content."},
    {"Name": "Logo Design", "Price": 2000, "Description": "Unique and memorable logos."},
    {"Name": "Web Design", "Price": 8000, "Description": "Elegant websites for your business."},
    {"Name": "Resume Writing", "Price": 1500, "Description": "Professional resumes to land your dream job."},
]

# --- Convert to DataFrame ---
df = pd.DataFrame(services)

# --- Sorting Option ---
sort_option = st.selectbox("Sort by:", ["Name", "Price"])
df = df.sort_values(by=sort_option)

# --- Display Services ---
for index, row in df.iterrows():
    st.subheader(f"{row['Name']} - ₹{row['Price']}")
    st.write(row['Description'])
    
    # WhatsApp link with pre-filled message
    message = f"Hello! I would like to avail the service: {row['Name']} from DocuReady."
    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"https://wa.me/919004804043?text={encoded_message}"
    
    st.markdown(f"[Contact via WhatsApp]({whatsapp_url})", unsafe_allow_html=True)

