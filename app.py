import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(layout="wide")

# Load the pages navigation from the .toml file
nav = get_nav_from_toml(".streamlit/pages.toml")

# Display the navigation and page title
pg = st.navigation(nav)

add_page_title(pg)

# Run the selected page
pg.run()
