import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="About Me | Jamiel Kyne R. Pinca", page_icon="👋", layout="wide")

# --- HEADER ---
st.title("👋 About Me")
st.caption("Welcome to my personal Streamlit portfolio — an overview of who I am, what I do, and what drives me.")
st.divider()

# --- MAIN SECTION ---
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    st.image("Pfp.jpg", width=420)
with col2:
    st.header("Jamiel Kyne R. Pinca")
    st.write("🎓 Computer Science Student | 💡 Tech Enthusiast | 🌏 Cebu, Philippines")
    st.markdown("""
    A Computer Science student at Cebu Institute of Technology - University. Beyond my academic
    pursuits, I enjoy exploring new technologies and collaborating on innovative projects—especially those that
    make a positive impact on the community. 

    I am driven by creativity and problem-solving, continuously striving
    to enhance my skills in programming and design while contributing to meaningful and socially beneficial
    initiatives.
    """)
    st.markdown("> *'Code with purpose, build with passion.'*")

st.divider()

# --- QUICK STATS ---
st.subheader("📊 Highlights")
col3, col4, col5 = st.columns(3)
col3.metric("💻 Projects", "15+", "Active")
col4.metric("📚 Certifications / Online Course ", "13", "Completed")
col5.metric("🌐 Collaborations", "5+", "Team Projects")

st.divider()

# --- SKILLS & TRAITS ---
st.subheader("⚡ Personal Traits & Focus Areas")

col6, col7 = st.columns(2)

with col6:
    st.write("**Technical Strengths**")
    st.progress(0.9, text="Problem Solving & Algorithms")
    st.progress(0.85, text="Full-Stack Development")
    st.progress(0.8, text="AI / Machine Learning")
    st.progress(0.75, text="Data Visualization & Analytics")

with col7:
    st.write("**Core Traits**")
    st.progress(0.95, text="Creativity & Innovation")
    st.progress(0.9, text="Collaboration & Communication")
    st.progress(0.85, text="Leadership & Initiative")
    st.progress(0.8, text="Adaptability & Lifelong Learning")

st.divider()

# --- INTERACTIVE DATA SECTION ---
st.subheader("📈 My Learning Journey")
data = {
    "Year": ["2022", "2023", "2024", "2025"],
    "Projects Completed": [3, 6, 10, 15],
    "Skills Mastered": [4, 7, 10, 13]
}
df = pd.DataFrame(data)
chart = px.line(df, x="Year", y=["Projects Completed", "Skills Mastered"],
                title="Progress Over the Years", markers=True)
st.plotly_chart(chart, use_container_width=True)

st.divider()

# --- EXPANDERS ---
st.subheader("🎯 Beyond Code")

with st.expander("🧠 What drives me"):
    st.write("""
    I believe technology should **empower people**. My mission is to create solutions that make learning, 
    sustainability, and innovation accessible to everyone.
    """)

with st.expander("🎨 My creative side"):
    st.write("""
    I design UI/UX prototypes and digital art using **Figma**, **Canva**, and **Adobe Lightroom**. 
    Creativity allows me to bridge functionality with aesthetics.
    """)

with st.expander("🤝 Teamwork & Leadership"):
    st.write("""
    I enjoy working with teams that value **collaboration, curiosity, and shared growth**. 
    Great ideas come from people who build together.
    """)

st.divider()

# --- CHAT SECTION ---
st.subheader("💬 Let's Chat!")
chat_tab1, chat_tab2 = st.tabs(["Ask Me Anything", "Quick Feedback"])

with chat_tab1:
    user_input = st.text_input("Got a question or something to say?")
    if user_input:
        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write(f"Thanks for sharing! I love that you mentioned: **{user_input}** 😊")

with chat_tab2:
    feedback = st.radio("How do you find my portfolio?", ["Awesome!", "Cool but can improve", "Needs more features"])
    if st.button("Submit Feedback"):
        st.success("✅ Thanks for your feedback!")

st.divider()

# --- FUN FACTS / TIMELINE ---
st.subheader("🕒 My Timeline")
timeline = pd.DataFrame({
    "Year": ["2023", "2024", "2025"],
    "Milestone": [
        "Started my Computer Science journey 🎓",
        "Became part of collaborative projects 🤝",
        "Developed my personal Streamlit portfolio 🚀"
    ]
})
st.table(timeline)

# --- FOOTER ---
st.divider()

