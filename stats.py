import streamlit as st
import pandas as pd  # pip install pandas

YEAR = 2023
SKILL_CATEGORIES = ["Cloud Computing", "Cybersecurity", "AI", "Software Development"]  # Example skill categories
DATA_URL = "careers_global.csv"  

st.title(f"IT Job Openings Dashboard", anchor=False)

@st.cache_data
def get_and_prepare_data(data):
    df = pd.read_csv(data)
    
    df['date_of_posting'] = pd.to_datetime(df['date'], errors='coerce')
    
    df = df.dropna(subset=['date_of_posting', 'skill_category', 'job_openings'])
    
    # Add year and month columns
    df['month'] = df['date_of_posting'].dt.month
    df['year'] = df['date_of_posting'].dt.year
    
    return df

df = get_and_prepare_data(data=DATA_URL)

# Check available skill categories in the dataset
available_skill_categories = df['skill_category'].unique()

# Calculate total job openings for each skill category for the selected year
skill_category_job_openings = (
    df.query("year == @YEAR")
    .groupby("skill_category")["job_openings"]
    .sum()
    .reset_index()
)

# Display the total job openings for each skill category
columns = st.columns(len(SKILL_CATEGORIES))
for i, skill_category in enumerate(SKILL_CATEGORIES):
    if skill_category in available_skill_categories:  # Check if the skill category exists in the dataset
        with columns[i]:
            total_openings = skill_category_job_openings.loc[
                skill_category_job_openings['skill_category'] == skill_category, 
                'job_openings'
            ].values[0]
            st.metric(
                label=skill_category,
                value=f"{total_openings:,} job openings",
            )
    else:
        st.write(f"Skill category '{skill_category}' not found in the dataset.")

# Selection field for skill category
selected_skill_category = st.selectbox("Select a skill category:", available_skill_categories)

# Filter data based on selected skill category
filtered_data = (
    df.query("skill_category == @selected_skill_category & year == @YEAR")
    .groupby("month", dropna=False)["job_openings"]
    .sum()
    .reset_index()
)

# Ensure month column is formatted as two digits for consistency
filtered_data["month"] = filtered_data["month"].apply(lambda x: f"{x:02d}")

# Display the data
st.write(f"**Job Openings for {selected_skill_category} in {YEAR}**")
st.bar_chart(filtered_data.set_index("month")["job_openings"])
