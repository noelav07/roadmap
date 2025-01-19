# import streamlit as st
# from st_pages import add_page_title, get_nav_from_toml

# st.set_page_config(layout="wide")

# # Load the pages navigation from the .toml file
# nav = get_nav_from_toml(".streamlit/pages.toml")

# # Display the navigation and page title
# pg = st.navigation(nav)

# add_page_title(pg)

# # Run the selected page
# pg.run()

import streamlit as st

# Define the pages and their respective paths
pages = [
    st.Page("pages/home.py", title="🏠 Home"),
    st.Page("pages/roadmap_generator.py", title="🛣️ Roadmap Generator"),
    st.Page("pages/chat.py", title="🤖 Assistant "),
    st.Page("pages/popular_roadmaps.py", title="👩‍💻 Popular Roadmaps")
]

# Set up navigation
pg = st.navigation(pages)

# Run the selected page
pg.run()
