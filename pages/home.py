import streamlit as st

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
        <div class="landing-subtitle">Ask questions, generate personalized roadmaps, and explore popular IT career paths</div>

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

show_home()
