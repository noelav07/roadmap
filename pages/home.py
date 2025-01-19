import streamlit as st
import plotly.express as px
import pandas as pd

# Data for IT jobs (You can replace this with real data or API responses)
job_titles = ['Software Engineer', 'DevOps Engineer', 'Data Scientist', 'Cybersecurity Analyst', 'Cloud Architect']
average_salaries = [120000, 115000, 130000, 110000, 140000]
job_demand = [85, 90, 92, 80, 95]  # Hypothetical job demand percentage

# Create a DataFrame
data = {'Job Title': job_titles, 'Average Salary (USD)': average_salaries, 'Job Demand (%)': job_demand}
df = pd.DataFrame(data)

# Set the page configuration (only once, at the top)
st.set_page_config(page_title="IT Jobs Salary and Demand Comparison", layout="wide")

# Function to show the home page with charts
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
            justify-content: space-between;
            flex-wrap: wrap;
            margin-top: 40px;
        }
        .feature-box {
            width: 30%;
            padding: 20px;
            margin: 15px;
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
            margin-bottom: 20px;
        }
        .chart-container {
            margin-top: 20px;
        }
        </style>

        <div class="landing-title">Personalized Roadmap Generator</div>
        <div class="landing-subtitle">Ask questions, generate personalized roadmaps, and explore popular IT career paths</div>
        """, unsafe_allow_html=True)

    # Feature boxes with descriptions
    st.markdown("""
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
    """, unsafe_allow_html=True)

    # Chart for IT Jobs Salary and Demand Comparison
    st.markdown("<h4 style='color: #4CAF50;'>IT Jobs Salary and Demand Comparison</h4>", unsafe_allow_html=True)

    # Create an interactive bar chart with Plotly
    fig_bar = px.bar(df, 
                     x='Job Title', 
                     y='Average Salary (USD)', 
                     color='Job Demand (%)', 
                     title='IT Jobs Comparison: Salaries and Demand',
                     labels={'Average Salary (USD)': 'Salary (USD)', 'Job Demand (%)': 'Job Demand (%)'},
                     color_continuous_scale='Viridis',  # A color scale to indicate job demand
                     text='Job Demand (%)',  # Show job demand percentage on top of the bars
                     template='plotly_dark')  # A dark theme for the chart

    # Customize the layout for the bar chart
    fig_bar.update_layout(
        xaxis_title='Job Title',
        yaxis_title='Average Salary (USD)',
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        showlegend=False,  # Hide the legend
        font=dict(family='Arial, sans-serif', size=14, color='white'),  # Font styling
    )

    # Display the bar chart in Streamlit
    st.plotly_chart(fig_bar)

    # Pie chart for Job Demand Distribution
    st.markdown("<h4 style='color: #4CAF50;'>Job Demand Distribution</h4>", unsafe_allow_html=True)

    # Create a pie chart for job demand distribution
    fig_pie = px.pie(df, 
                     names='Job Title', 
                     values='Job Demand (%)', 
                     title='Job Demand Distribution by Role',
                     color='Job Title', 
                     color_discrete_sequence=px.colors.qualitative.Set2)  # A color palette for the pie chart

    # Customize the layout for the pie chart with larger size
    fig_pie.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        font=dict(family='Arial, sans-serif', size=14, color='white'),  # Font styling
        height=600,  # Increase the height of the pie chart
        width=800   # Increase the width of the pie chart
    )

    # Display the pie chart in Streamlit
    st.plotly_chart(fig_pie)

# Call the show_home function to render the page
show_home()
