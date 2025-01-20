import streamlit as st

def show_roadmap_generator():
    # Title with styling for a professional look
    st.markdown("<h1 style='color: green; text-align: center;'>Roadmap Generator</h1>", unsafe_allow_html=True)
    st.write("Create a personalized career roadmap by providing your skills and career goal. Let's get started!")

    # Add spacing for better visual separation
    st.markdown("<hr>", unsafe_allow_html=True)
    # Input fields for skills and career goal
    st.subheader("Step 1: Enter Your Skills 🛠️")
    skills = st.text_area(
        "Skills (e.g., Python, Docker, Linux, AWS)",
        placeholder="e.g., Python, Docker, Linux, AWS",
        height=150,
        label_visibility="collapsed"
    )
    
    st.subheader("Step 2: Define Your Career Goal 🎯")
    goal = st.text_input(
        "Career Goal (e.g., DevOps Engineer)",
        placeholder="e.g., DevOps Engineer",
        label_visibility="collapsed"
    )

    # Add some spacing before the button
    st.markdown("<br>", unsafe_allow_html=True)

    # Button to generate the roadmap
    if st.button("Generate Roadmap"):
        if skills and goal:
            st.success("Your roadmap is being generated!")
            st.write("### **Skills Provided:**")
            st.write(f"- {skills}")
            st.write("### **Career Goal:**")
            st.write(f"- {goal}")
            st.info("Roadmap generation is a placeholder for now. Stay tuned!")
        else:
            st.error("Please fill in both your skills and career goal to proceed.")

# Call the function to display the roadmap generator page
show_roadmap_generator()
