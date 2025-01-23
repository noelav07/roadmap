import streamlit as st

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

pg = st.navigation(
    {
        "Info": [home],
        "Sections": [roadmap_generator, chat, popular],
    }
)

# --- SHARED ON ALL PAGES ---
st.sidebar.markdown("🗂️Career Assistance ")

# --- RUN NAVIGATION ---
pg.run()
