import streamlit as st
import os

# Define the mapping of pages to file paths
pages = {
    "🏠 Home": "crops/home.py",
    "🛣️ Roadmap Generator": "crops/roadgen.py",
    "🤖 Assistant": "crops/chat.py",
    "👩‍💻 Popular Roadmaps": "crops/popular_roadmaps.py"
}

# Sidebar for navigation with radio buttons
page_selection = st.sidebar.radio(
    "Navigate to:",  # Label for the radio button group
    list(pages.keys()),
    label_visibility="collapsed"  # Ensure the label is collapsed
)

# Load and execute the selected page
selected_page = pages[page_selection]

if os.path.exists(selected_page):
    with open(selected_page, "r") as file:
        code = file.read()
        exec(code, globals())
else:
    st.error(f"Page not found: {selected_page}")


