import streamlit as st
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Contact | Jamiel Kyne R. Pinca", page_icon="📬", layout="centered")

# --- HEADER ---
st.title("📬 Contact Me")
st.write("Let’s connect and collaborate on meaningful tech ideas 💡")
st.caption("Whether it’s for a project, opportunity, or just to say hi — I’d love to hear from you.")
st.divider()

# --- CONTACT INFO SECTION ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("📧 **Email**")
    st.write("[jamielpinca@example.com](mailto:jamielkynepinca@gmail.com)")
with col2:
    st.markdown("💼 **LinkedIn**")
    st.write("[linkedin.com/in/jamielpinca](https://www.linkedin.com/in/jamiel-kyne-r-pinca-92b045342/)")
with col3:
    st.markdown("🐙 **GitHub**")
    st.write("[github.com/jamielpinca](https://github.com/CodeJamjamzz?tab=overview&from=2025-10-01&to=2025-10-31)")

st.divider()

# --- CONTACT FORM ---
st.subheader("💌 Send me a message")

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message", placeholder="Write your message here...")
    submitted = st.form_submit_button("📨 Send Message")

    if submitted:
        if name and email and message:
            st.success(f"✅ Thanks {name}, your message has been sent successfully!")
            st.balloons()
        else:
            st.error("⚠️ Please fill out all fields before submitting.")

st.divider()

# --- OPTIONAL: ADD MAP OR AVAILABILITY ---
st.subheader("🌏 I'm Based In")
col_map, col_time = st.columns(2)

with col_map:
    st.map({"lat": [10.3157], "lon": [123.8854]})  # Cebu coordinates

with col_time:
    st.metric("⏰ Current Time", datetime.now().strftime("%I:%M %p"), "Cebu, Philippines")

st.divider()

# --- FOOTER ---