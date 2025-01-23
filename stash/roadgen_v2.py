import streamlit as st
import boto3
import json

# Initialize Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")

def generate_roadmap(skills, goal):
    """Generate a career roadmap using AWS Bedrock."""
    prompt = f"""
    The user has the following skills: {skills if skills else 'N/A'}.
    Their career goal is: {goal if goal else 'N/A'}.
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

    try:
        response = bedrock.invoke_model(
            body=body,
            modelId="us.meta.llama3-3-70b-instruct-v1:0",
            accept="application/json",
            contentType="application/json"
        )
        response_body = json.loads(response.get("body").read())
        return response_body.get('generation', 'No roadmap generated.')
    except Exception as e:
        return f"Error generating roadmap: {str(e)}"

def show_roadmap_generator():
    """Display the roadmap generator interface."""
    st.markdown("""
        <style>
        .main-container {
            max-width: 800px;
            margin: auto;
        }
        .divider {
            border-top: 2px solid #ddd;
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: green; text-align: center;'>Career Roadmap Generator</h1>", unsafe_allow_html=True)
    # st.write("Input your skills and career goal to generate a personalized roadmap.")
    st.markdown("<h3 style='color: white; text-align: center;'>Input your skills and career goal to generate a personalized roadmap.</h1>", unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("Your Input")
        skills = st.text_area(
            "Skills",
            placeholder="e.g., Python, Docker, Linux, AWS",
            height=150
        )
        goal = st.text_input(
            "Career Goal",
            placeholder="e.g., DevOps Engineer"
        )

        if st.button("Generate Roadmap"):
            if skills and goal:
                st.session_state.roadmap = generate_roadmap(skills, goal)
                st.success("Roadmap generated successfully!")
            else:
                st.error("Please provide both skills and career goal.")

    with col2:
        st.subheader("Generated Roadmap")
        if "roadmap" in st.session_state:
            st.write(st.session_state.roadmap)
        else:
            st.info("Your roadmap will appear here once generated.")



show_roadmap_generator()
