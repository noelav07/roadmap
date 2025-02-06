import streamlit as st

st.set_page_config(
    page_title="Jobs",
    page_icon="🚀",
    layout="wide"
)

home = st.Page(
    "crops/home.py",
    title="Home",
    icon=":material/home:",
#    default=True,  # Default page
)
roadmap_generator = st.Page(
    # "crops/roadgen.py",
    "crops/roadgen_v2.py",
    title="Roadmap Guide",
    icon=":material/road:",
)
chat = st.Page(
    "crops/chat.py",
    title="Career Assistant",
    icon=":material/robot:",
)
popular = st.Page(
    "crops/popular_roadmaps.py",
    title="Popular Roadmaps",
    icon=":material/map:",
)
Career = st.Page(
    "crops/openings.py",
    title="Job Openings",
    icon=":material/work:",
)
resume_optimiser = st.Page(
    "crops/resume.py",
    title="Resume Optimiser",
    icon=":material/plagiarism:",
)


pg = st.navigation(
    {
        "Info": [home],
        "Sections": [roadmap_generator, chat, popular,Career, resume_optimiser],
    }
)

# --- SHARED ON ALL PAGES ---
st.sidebar.markdown("🗂️Career Assistance ")

# --- RUN NAVIGATION ---
pg.run()


