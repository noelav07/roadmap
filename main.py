import streamlit as st

home = st.Page(
    "crops/home.py",
    title="About Me",
    icon=":material/account_circle:",
#    default=True,  # Default page
)
roadmap_generator = st.Page(
    # "crops/roadgen.py",
    "crops/roadgen.py",
    title="Roadmap Generator",
    icon=":material/bar_chart:",
)
chat = st.Page(
    "crops/chat.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
popular = st.Page(
    "crops/popular_roadmaps.py",
    title="Popular",
    icon=":material/smart_toy:",
)

pg = st.navigation(
    {
        "Info": [home],
        "Projects": [roadmap_generator, chat, popular],
    }
)

# --- SHARED ON ALL PAGES ---
st.sidebar.markdown("Noel")

# --- RUN NAVIGATION ---
pg.run()
