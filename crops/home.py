import streamlit as st
import pandas as pd

# Data for IT jobs
job_titles = ['Software Engineer', 'DevOps Engineer', 'Data Scientist', 'Cybersecurity Analyst', 'Cloud Architect']
average_salaries = [120000, 115000, 130000, 110000, 140000]
job_demand = [85, 90, 92, 80, 95]

data = {'Job Title': job_titles, 'Average Salary (USD)': average_salaries, 'Job Demand (%)': job_demand}
df = pd.DataFrame(data)

# Define the home page layout
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
            color: #FFF;
            text-align: center;
            margin-top: 10px;
        }
        .features {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            margin-top: 40px;
        }
        .feature-box {
            width: 30%;
            padding: 10px;
            margin: 10px;
            border: 1px solid #ddd;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #f9f9f9;
            transition: transform 0.3s;
        }
        .feature-box:hover {
            transform: scale(1.05);
        }
        .feature-box h3 {
            font-size: 1.3em;
            color: #333;
            margin-bottom: 15px;
        }
        .feature-box p {
            font-size: 1em;
            color: #666;
            margin: 0;
            padding-top: 5px;
        }
        </style>

        <div class="landing-title">Personalized Roadmap Generator</div>
        <div class="landing-subtitle">Ask questions, generate personalized roadmaps, and explore popular IT career paths</div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="features">
            <div class="feature-box">
                <h3>Generate Roadmaps</h3>
                <p style= 'padding-top: 0px; margin: 0;'>Create customized learning paths based on your skills and goals.</p>
            </div>
            <div class="feature-box">
                <h3>Interactive Chat</h3>
                <p style= 'padding-top: 35px; margin: 0;' >Get guidance and answers to your career-related queries.</p>
            </div>
            <div class="feature-box">
                <h3>Popular Roadmaps</h3>
                <p style= 'padding-top: 0px; margin: 0;'>Explore and download ready-made roadmaps for top IT roles.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)  # Add a horizontal line
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>IT Jobs Salary and Demand Comparison</h2>", unsafe_allow_html=True)

    # Display IT Jobs Salary and Demand Comparison Table
    st.table(df)

# IT Job Openings Dashboard
def show_dashboard():
    YEAR = 2023
    SKILL_CATEGORIES = ["Cloud Computing", "Cybersecurity", "AI", "Software Development"]
    DATA_URL = "careers_global.csv"

    st.markdown("<hr>", unsafe_allow_html=True)  # Add a horizontal line
    # st.title("IT Job Openings Dashboard", anchor=False)
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>IT Job Openings Dashboard</h2>", unsafe_allow_html=True)

    @st.cache_data
    def get_and_prepare_data(data):
        df = pd.read_csv(data)
        df['date_of_posting'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date_of_posting', 'skill_category', 'job_openings'])
        df['month'] = df['date_of_posting'].dt.month
        df['year'] = df['date_of_posting'].dt.year
        return df

    df = get_and_prepare_data(data=DATA_URL)
    available_skill_categories = df['skill_category'].unique()

    skill_category_job_openings = (
        df.query("year == @YEAR")
        .groupby("skill_category")["job_openings"]
        .sum()
        .reset_index()
    )

    columns = st.columns(len(SKILL_CATEGORIES))
    for i, skill_category in enumerate(SKILL_CATEGORIES):
        if skill_category in available_skill_categories:
            with columns[i]:
                total_openings = skill_category_job_openings.loc[
                    skill_category_job_openings['skill_category'] == skill_category,
                    'job_openings'
                ].values[0]
                st.metric(
                    label=skill_category,
                    value=f"{total_openings:,} jobs ",
                )
        else:
            st.write(f"Skill category '{skill_category}' not found in the dataset.")

    selected_skill_category = st.selectbox("Select a skill category:", available_skill_categories)

    filtered_data = (
        df.query("skill_category == @selected_skill_category & year == @YEAR")
        .groupby("month", dropna=False)["job_openings"]
        .sum()
        .reset_index()
    )

    filtered_data["month"] = filtered_data["month"].apply(lambda x: f"{x:02d}")

    st.write(f"**Job Openings for {selected_skill_category} in 2023-2024**")
    st.bar_chart(filtered_data.set_index("month")["job_openings"])

# Display sections in the desired order
show_home()
show_dashboard()
