import streamlit as st

def show_roadmap_generator():
    st.title("Roadmap Generator")
    skills = st.text_area("🛠️ Your Skills", placeholder="e.g., Python, Docker, Linux, AWS")
    goal = st.text_input("🎯 Your Career Goal", placeholder="e.g., DevOps Engineer")
    if st.button("Generate Roadmap"):
        if skills and goal:
            st.success("Your roadmap will appear below:")
            st.write("**Skills Provided:**", skills)
            st.write("**Career Goal:**", goal)
            st.info("Roadmap generation is currently a placeholder.")
        else:
            st.error("Please provide both your skills and career goal to proceed.")

show_roadmap_generator()
