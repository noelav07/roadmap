import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Roadmap Generator", layout="wide")

def show_home():
    st.markdown(
        """
        <style>
        .landing-title {
            font-size: 3em;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-top: 20px;
        }
        .landing-subtitle {
            font-size: 1.5em;
            color: #555;
            text-align: center;
            margin-top: 10px;
        }
        .features {
            display: flex;
            justify-content: center;
            margin-top: 30px;
        }
        .feature-box {
            width: 250px;
            padding: 20px;
            margin: 10px;
            border: 1px solid #ddd;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .feature-box h3 {
            font-size: 1.2em;
            color: #333;
        }
        .feature-box p {
            font-size: 0.9em;
            color: #666;
        }
        </style>

        <div class="landing-title">Personalized Roadmap Generator</div>
        <div class="landing-subtitle">"Ask questions, generate personalized roadmaps, and explore popular IT career paths</div>

        <div class="features">
            <div class="feature-box">
                <h3>Generate Roadmaps</h3>
                <p>Create customized learning paths based on your skills and goals.</p>
            </div>
            <div class="feature-box">
                <h3>Interactive Chat</h3>
                <p>Get guidance and answers to your career-related queries.</p>
            </div>
            <div class="feature-box">
                <h3>Popular Roadmaps</h3>
                <p>Explore and download ready-made roadmaps for top IT roles.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

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

def show_chat():
    st.title("Chat")
    st.write("This is where you can interact for guidance and queries.")
    st.text_area("Type your question here:", placeholder="e.g., What certifications should I pursue for DevOps?")
    if st.button("Send"):
        st.info("Chat functionality is a placeholder.")

def show_popular_roadmaps():
    st.title("Popular Roadmaps")
    st.write("Explore some of the most popular roadmaps.")
    
    # Embed the images directly and set the width to a smaller size (e.g., 100px for icon size)
    backend_img = "./map_img/backend.jpg"
    devops_img = "./map_img/devops.jpg"
    aws_img = "./map_img/aws.jpg"

    # Create columns for the row layout
    cols = st.columns(3)

    # Backend Developer Roadmap
    with cols[0]:
        st.image(backend_img, caption="Backend Developer Roadmap", use_container_width=False, width=100)
        with open("backend.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download Backend Roadmap PDF", data=PDFbyte, file_name="backend_roadmap.pdf", mime="application/pdf")

    # DevOps Engineer Roadmap
    with cols[1]:
        st.image(devops_img, caption="DevOps Engineer Roadmap", use_container_width=False, width=100)
        with open("devops.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download DevOps Roadmap PDF", data=PDFbyte, file_name="devops_roadmap.pdf", mime="application/pdf")

    # AWS Cloud Architect Roadmap
    with cols[2]:
        st.image(aws_img, caption="AWS Cloud Architect Roadmap", use_container_width=False, width=100)
        with open("aws.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download AWS Cloud Architect Roadmap PDF", data=PDFbyte, file_name="aws.pdf", mime="application/pdf")

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f0f5;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .sidebar .sidebar-header {
        text-align: center;
        font-size: 1.5em;
        color: #333;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sidebar .sidebar-radio label {
        font-size: 1.2em;
        color: #333;
    }
    .sidebar .sidebar-radio input[type="radio"] {
        margin-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

page = st.sidebar.radio("Select a page:", ["Home", "Roadmap Generator", "Chat", "Popular Roadmaps"], index=0)

# Page routing
if page == "Home":
    show_home()
elif page == "Roadmap Generator":
    show_roadmap_generator()
elif page == "Chat":
    show_chat()
elif page == "Popular Roadmaps":
    show_popular_roadmaps()
