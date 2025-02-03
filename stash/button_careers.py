import streamlit as st

# Sample job data
jobs = [
    {"position": "Cloud Engineer", "company": "AWS", "location": "Remote", "career_url": "https://aws.amazon.com/careers/"},
    {"position": "DevOps Engineer", "company": "Google", "location": "USA", "career_url": "https://careers.google.com/"},
    {"position": "Software Engineer", "company": "Microsoft", "location": "India", "career_url": "https://careers.microsoft.com/"},
    {"position": "Network Engineer", "company": "Cisco", "location": "UK", "career_url": "https://www.cisco.com/c/en/us/about/careers.html"},
    {"position": "Cybersecurity Analyst", "company": "IBM", "location": "Canada", "career_url": "https://www.ibm.com/employment/"},
    {"position": "Data Scientist", "company": "Meta", "location": "Germany", "career_url": "https://www.metacareers.com/"},
    {"position": "AI Engineer", "company": "OpenAI", "location": "USA", "career_url": "https://openai.com/careers"},
    {"position": "SRE", "company": "Netflix", "location": "Remote", "career_url": "https://jobs.netflix.com/"},
    {"position": "Security Engineer", "company": "Palo Alto", "location": "Netherlands", "career_url": "https://www.paloaltonetworks.com/company/careers"},
    {"position": "Frontend Developer", "company": "Spotify", "location": "Sweden", "career_url": "https://www.spotifyjobs.com/"},
    {"position": "Backend Engineer", "company": "Apple", "location": "Singapore", "career_url": "https://www.apple.com/careers/"},
    {"position": "Full Stack Developer", "company": "Amazon", "location": "Remote", "career_url": "https://www.amazon.jobs/"},
    {"position": "Product Manager", "company": "Tesla", "location": "USA", "career_url": "https://www.tesla.com/careers"},
    {"position": "Business Analyst", "company": "Adobe", "location": "India", "career_url": "https://www.adobe.com/careers.html"},
    {"position": "Data Engineer", "company": "Facebook", "location": "Canada", "career_url": "https://www.facebook.com/careers"},
    {"position": "ML Engineer", "company": "DeepMind", "location": "UK", "career_url": "https://deepmind.com/careers"},
    {"position": "Cloud Architect", "company": "IBM", "location": "Germany", "career_url": "https://www.ibm.com/employment/"},
    {"position": "Tech Lead", "company": "Oracle", "location": "Remote", "career_url": "https://www.oracle.com/corporate/careers/"},
    {"position": "System Administrator", "company": "Dell", "location": "Australia", "career_url": "https://jobs.dell.com/"},
    {"position": "Penetration Tester", "company": "CyberArk", "location": "India", "career_url": "https://www.cyberark.com/careers/"},
    {"position": "IoT Engineer", "company": "Intel", "location": "USA", "career_url": "https://www.intel.com/content/www/us/en/jobs/locations.html"},
    {"position": "Kubernetes Engineer", "company": "Red Hat", "location": "Remote", "career_url": "https://www.redhat.com/en/jobs"},
    {"position": "DevSecOps Engineer", "company": "GitHub", "location": "Switzerland", "career_url": "https://github.com/about/careers"},
    {"position": "Embedded Systems Engineer", "company": "Nvidia", "location": "Canada", "career_url": "https://www.nvidia.com/en-us/about-nvidia/careers/"}
]

st.title("📌 Job Openings")

# Define number of columns
num_columns = 3
rows = [jobs[i : i + num_columns] for i in range(0, len(jobs), num_columns)]

# Apply CSS for uniform spacing (including row gaps) and hover effect
st.markdown(
    """
    <style>
        .job-card {
            border: 1px solid #ddd; 
            padding: 15px; 
            border-radius: 10px; 
            background-color: #ffffff; 
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            height: 160px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin-bottom: 15px;  /* Adds space between rows */
            transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for hover effect */
        }
        .job-card:hover {
            transform: translateY(-10px); /* Lifts the card when hovered */
            box-shadow: 4px 4px 15px rgba(0,0,0,0.2); /* Stronger shadow on hover */
        }
        .apply-btn {
            margin-top: 10px;
            padding: 8px 16px;
            background-color: #1a73e8;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
        }
        .apply-btn:hover {
            background-color: #1558b0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Generate Grid
for row in rows:
    cols = st.columns(num_columns)  # Create 3 columns for each row
    for i, job in enumerate(row):

        with cols[i]:
            st.markdown(
                f"""
                <div class="job-card">
                    <h4 style="margin: 0px 0; font-size: 16px; color: #000000;">{job["position"]}</h4>
                    <p style="margin: 0px 0; color: #555;"><strong>{job["company"]}</strong></p>
                    <p style="margin: 0px 0; color: #888;">📍 {job["location"]}</p>
                    <a href="{job['career_url']}" target="_blank" class="apply-btn">Apply Now</a>
                </div>
                """,
                unsafe_allow_html=True,
            )





