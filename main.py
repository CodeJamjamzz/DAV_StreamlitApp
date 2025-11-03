import streamlit as st

st.set_page_config(page_title="Jamiel Kyne Pinca | Portfolio", page_icon="✨", layout="wide", initial_sidebar_state="expanded")
pages = {
    "Personal Details": [
        st.Page("about_me.py", title="About Me", icon="👤"),
        st.Page("education_skills.py", title="Education & Skills", icon="🎓"),
    ],
    "Portfolio": [
        st.Page("projects.py", title="Projects", icon="💻"),
        st.Page("contact.py", title="Contact", icon="📬"),
    ],
}

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()


