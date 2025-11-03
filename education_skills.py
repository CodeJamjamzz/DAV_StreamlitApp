import streamlit as st

# --- EDUCATION SECTION ---
st.header("🎓 Education")
st.write("- **Elementary to Senior High School:** De La Salle Andres Soriano Memorial College")
st.write("- **Tertiary:** Bachelor of Science in Computer Science – Cebu Institute of Technology - University")
st.write("- **Expected Graduation:** 2027")

st.divider()

# --- SKILLS SECTION ---
st.header("🧠 Tech Stack (Languages and Tools)")

# Better layout with full visibility
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🗣️ Languages")
    st.write("""
    - Python  
    - C  
    - C++  
    - Java  
    - JavaScript  
    - TypeScript  
    - Kotlin
    """)

with col2:
    st.subheader("⚙️ Frameworks & Libraries")
    st.write("""
    - Django  
    - Spring Boot  
    - React  
    - TensorFlow  
    - FastAPI  
    - LangChain  
    - Scikit-Learn
    """)

with col3:
    st.subheader("🧩 Tools & Design")
    st.write("""
    - Git / GitHub  
    - Docker / Docker Desktop  
    - Figma  
    - Canva  
    - Adobe Lightroom  
    - VS Code  
    - PyCharm  
    - Postman
    """)

st.divider()

# --- PROJECTS / EXPERIENCE ---
st.header("🚀 Projects & Experience")
st.write("""
Here are some of the things I’ve worked on:
- 🧠 **AI & Machine Learning:** Built models using Scikit-Learn and TensorFlow for academic projects.  
- 🌐 **Full-Stack Development:** Created and deployed complete web and mobile applications using React, Django, and Spring Boot.  
- 🔄 **Automation & APIs:** Integrated automated workflows, API services, and used LangChain for LLM-driven solutions.  
- 🎨 **Creative Design:** Used Figma and Canva for UI/UX prototypes and visual storytelling.
""")

st.divider()

# --- CERTIFICATIONS SECTION ---
st.header("📄 Certifications & Completed Courses")
st.write("Here are my certifications and completed courses. Click any link below to view them on Google Drive:")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📘 Associate AI Engineer for Developers")
    st.caption("Issued by Datacamp | Completed: 2024")
    st.markdown("[🔗 View Certificate](https://drive.google.com/file/d/1BZWf96Gy0Z0MviWxAnf1_ZlUzOgYqfFm/view?usp=sharing)", unsafe_allow_html=True)

    st.subheader("📘 Java OOP (PUP Manila)")
    st.caption("Issued by Polytechnic University of the Philippines | Completed: 2024")
    st.markdown("[🔗 View Certificate](https://drive.google.com/file/d/1I1b6p-4uxSS8KCzJ14_WR1M3OvzYiJmg/view?usp=sharing)", unsafe_allow_html=True)

    st.subheader("📘 Java Codechum")
    st.caption("Issued by CodeChum | Completed: 2024")
    st.markdown("[🔗 View Certificate](https://drive.google.com/file/d/1WXysbRRlI31tbsEcitk9rtUicJuHZ8uV/view?usp=sharing)", unsafe_allow_html=True)

with col2:
    st.subheader("📗 JavaScript Essentials")
    st.caption("Issued by Sololearn | Completed: 2024")
    st.markdown("[🔗 View Certificate](https://drive.google.com/file/d/1fjs_-Wvw4b1pRSvnFCTNllhLRbAUbkUG/view?usp=sharing)", unsafe_allow_html=True)

    st.subheader("📗 C Codechum")
    st.caption("Issued by CodeChum | Completed: 2024")
    st.markdown("[🔗 View Certificate](https://drive.google.com/file/d/1YF-6fbQcllMo960n6rXA3uaFSO4aMrlW/view?usp=sharing)", unsafe_allow_html=True)

    st.subheader("📗 Python Essentials")
    st.caption("Issued by Sololearn | Completed: 2024")
    st.markdown("[🔗 View Certificate](https://drive.google.com/file/d/1fK2dXUD8Xe58As6MeF-lAm-44THWdFPT/view?usp=sharing)", unsafe_allow_html=True)

with col3:
    st.subheader("📙 Graphic Design Essentials")
    st.caption("Issued by Canva | Completed: 2023")
    st.markdown("[🔗 View Certificate](https://drive.google.com/file/d/1qIsy5Z8EosUn-bWMYOxJCT7xW7FS76aR/view?usp=sharing)", unsafe_allow_html=True)

    st.subheader("📙 Intermediate Git")
    st.caption("Issued by Datacamp | Completed: 2023")
    st.markdown("[🔗 View Certificate](https://drive.google.com/file/d/1Rq6XhMKP0VtjNCTNL4H6WNFeGuJdj3UN/view?usp=sharing)", unsafe_allow_html=True)

    st.subheader("📙 Intermediate GitHub Concepts")
    st.caption("Issued by Datacamp | Completed: 2023")
    st.markdown("[🔗 View Certificate](https://drive.google.com/file/d/1bCkapVMoFfNmmwzWz-BLY6y-wyCrAh8j/view?usp=sharing)", unsafe_allow_html=True)

st.divider()

