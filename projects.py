import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Projects | Jamiel Kyne R. Pinca", page_icon="💻", layout="wide")

# --- HEADER ---
st.title("💻 Projects & Case Studies")
st.subheader("Showcasing my development journey across various technologies")
st.caption("Here are the apps and systems I’ve built — ranging from Android apps to full-stack and AI projects.")
st.divider()

# --- PROJECT DATA ---
projects = [
    {
        "name": "Regit",
        "status": "✅ Done (2023)",
        "desc": "An event management app that helps organizations track attendees efficiently.",
        "tech": "Java, Android Studio",
        "progress": 1.0,
    },
    {
        "name": "Quetek",
        "status": "✅ Done (2024)",
        "desc": "A queue management app for optimizing customer service flow in organizations.",
        "tech": "Kotlin, Android Studio",
        "progress": 1.0,
    },
    {
        "name": "Structs & Algos",
        "status": "✅ Done (2024)",
        "desc": "A Snake & Ladders-inspired game integrating core data structure mechanics.",
        "tech": "Java, FXGL",
        "progress": 1.0,
    },
    {
        "name": "Flowyn",
        "status": "🔄 Pending (2025)",
        "desc": "A full-stack freelancing platform connecting developers and clients seamlessly.",
        "tech": "React, Express.js, Node.js",
        "progress": 0.7,
    },
    {
        "name": "RepoBased",
        "status": "🔄 Pending (2025)",
        "desc": "A smart chatbot assistant for your coding repositories and project management.",
        "tech": "React, Spring Boot",
        "progress": 0.6,
    },
    {
        "name": "Univerct",
        "status": "🔄 Pending (2025)",
        "desc": "A Python-based academic guide app helping students discover course insights and materials.",
        "tech": "Python, Django",
        "progress": 0.5,
    },
]

# --- PROJECT DISPLAY ---
for i in range(0, len(projects), 2):
    cols = st.columns(2)
    for col, project in zip(cols, projects[i:i + 2]):
        with col:
            st.markdown(f"### 🚀 {project['name']}")
            st.caption(project["status"])
            st.write(project["desc"])
            st.write(f"**Tech Stack:** {project['tech']}")
            st.progress(project["progress"])
            with st.expander("More details"):
                st.write(f"""
                **Project Overview:**  
                {project["desc"]}

                **Built With:** {project["tech"]}  
                **Status:** {project["status"]}
                """)
            st.divider()

# --- DATA VISUALIZATION ---
st.subheader("📊 Project Summary")

data = pd.DataFrame({
    "Status": ["Completed", "Pending"],
    "Count": [3, 3],
})

fig = px.pie(data, names="Status", values="Count",
             title="Completed vs Pending Projects",
             color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig, use_container_width=True)

# --- CTA ---
st.success("🚀 Excited to keep building — new projects are always in the works!")
st.caption("All projects are self-initiated, academic, or collaborative works aimed at learning and impact.")
