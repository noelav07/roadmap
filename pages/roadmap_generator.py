import streamlit as st
import boto3
import json

# Initialize Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")

def generate_roadmap(skills, goal):
    # Prepare the payload for the Bedrock model
    prompt = f"""
    [INST]
    The user has the following skills: {skills}.
    Their career goal is: {goal}.
    Generate a detailed, concise, and actionable career roadmap including:
    1. Key career paths based on their skills and goal.
    2. Essential skills or tools they should learn next.
    3. Steps to improve and advance in their career.
    Keep the output clear, crisp, and straight to the point.
    """
    payload = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }
    body = json.dumps(payload)

    # Call the Bedrock model
    try:
        response = bedrock.invoke_model(
            body=body,
            modelId="us.meta.llama3-3-70b-instruct-v1:0",
            accept="application/json",
            contentType="application/json"
        )
        # Parse the response
        response_body = json.loads(response.get("body").read())
        return response_body.get('generation', 'No roadmap generated.')
    except Exception as e:
        return f"Error generating roadmap: {str(e)}"

def show_roadmap_generator():
    # Title with styling for a professional look
    st.markdown("<h1 style='color: green; text-align: center;'>Roadmap Generator</h1>", unsafe_allow_html=True)
    st.write("Create a personalized career roadmap by providing your skills and career goal. Let's get started!")

    # Add spacing for better visual separation
    st.markdown("<hr>", unsafe_allow_html=True)

    # Create a container with larger space between input and output sections
    with st.container():
        # Create three columns with a larger space between input and output sections
        col1, col2, col3 = st.columns([30, 0.5, 30])  # Adjust column widths as needed

        with col1:
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
                    roadmap = generate_roadmap(skills, goal)
                    st.session_state.roadmap = roadmap  # Store the roadmap in session state
                else:
                    st.error("Please fill in both your skills and career goal to proceed.")

        with col2:
            # Vertical divider with custom styling
            st.html(
                '''
                    <div class="divider-vertical-line"></div>
                    <style>
                        .divider-vertical-line {
                            border-left: 2px solid rgba(49, 51, 63, 0.2);
                            height: 350px;  /* Adjust the height as needed */
                            margin: auto;
                        }
                    </style>
                '''
            )

        with col3:
            # Display the generated roadmap
            if 'roadmap' in st.session_state:
                st.markdown("### **Generated Career Roadmap:**")
                st.write(st.session_state.roadmap)
            else:
                st.write("Your roadmap will appear here once it's generated.")

# Call the function to display the roadmap generator page
if __name__ == "__main__":
    show_roadmap_generator()
