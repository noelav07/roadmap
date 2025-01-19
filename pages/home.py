import streamlit as st
import pandas as pd
import plotly.express as px

# Data for IT jobs (You can replace this with real data or API responses)
job_titles = ['Software Engineer', 'DevOps Engineer', 'Data Scientist', 'Cybersecurity Analyst', 'Cloud Architect']
average_salaries = [120000, 115000, 130000, 110000, 140000]
job_demand = [85, 90, 92, 80, 95]  # Hypothetical job demand percentage

# Create a DataFrame
data = {'Job Title': job_titles, 'Average Salary (USD)': average_salaries, 'Job Demand (%)': job_demand}
df = pd.DataFrame(data)

# Set the page configuration
st.set_page_config(page_title="IT Jobs Salary and Demand Comparison", layout="wide")

# Landing Page
def show_landing_page():
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
        .chart-container {
            border: 2px solid #4CAF50;
            padding: 20px;
            border-radius: 10px;
            background-color: #1e1e1e;
            margin-top: 40px;
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

# IT Job Analysis Dashboard
def show_job_analysis():
    st.markdown("""
        <h1 style="text-align: center; color: #4CAF50;">IT Jobs Comparison: Salaries & Demand</h1>
        <p style="font-size: 18px; text-align: center; color: #555;">
            Explore the average salaries and job demand for some of the most popular IT roles in the industry.
        </p>
    """, unsafe_allow_html=True)

    # Create a custom container for the charts
    st.markdown("""
        <div class="chart-container">
        <h3 style="color: #4CAF50; text-align: center;">Salaries and Job Demand Analysis</h3>
    """, unsafe_allow_html=True)

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

    # Create a pie chart for job demand distribution
    fig_pie = px.pie(df, 
                     names='Job Title', 
                     values='Job Demand (%)', 
                     title='Job Demand Distribution by Role',
                     color='Job Title', 
                     color_discrete_sequence=px.colors.qualitative.Set2)  # A color palette for the pie chart

    # Customize the layout for the pie chart
    fig_pie.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        font=dict(family='Arial, sans-serif', size=14, color='white'),  # Font styling
    )

    # Display the pie chart in Streamlit
    st.plotly_chart(fig_pie)

    # Closing the custom container
    st.markdown("</div>", unsafe_allow_html=True)

    # Additional Information or Explanation
    st.markdown("""
        <h3 style="color: #4CAF50;">Key Insights</h3>
        <ul style="font-size: 16px; color: #333;">
            <li><strong>Software Engineers</strong> have a high demand with competitive salaries, making it one of the top IT roles.</li>
            <li><strong>Data Scientists</strong> are in high demand due to the increasing reliance on data-driven decision-making in various industries.</li>
            <li><strong>DevOps Engineers</strong> bridge the gap between development and operations, making them highly sought after in modern IT environments.</li>
            <li><strong>Cloud Architects</strong> are in demand as businesses migrate to the cloud, and the role offers the highest average salary.</li>
            <li><strong>Cybersecurity Analysts</strong> are essential for protecting organizations from cyber threats, with a steady demand for their skills.</li>
        </ul>
        """, unsafe_allow_html=True)

    # Closing Remarks
    st.markdown("""
        <p style="font-size: 18px; text-align: center; color: #555;">
            Understanding the demand and salary trends in the IT industry is crucial for making informed career decisions. 
            Keep an eye on these trends to stay ahead in your career path!
        </p>
        """, unsafe_allow_html=True)

# Main function to show either the landing page or the job analysis page
def main():
    show_landing_page()

    # Button to switch to the IT Job Analysis page
    if st.button("Explore IT Jobs Analysis"):
        show_job_analysis()

# Run the app
if __name__ == "__main__":
    main()
