import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# App title
st.title('COVID-19 Global Data Tracker')

# Load data with caching
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_covid_data.csv')
    df['date'] = pd.to_datetime(df['date'])  # Ensure date is datetime type
    return df

df = load_data()

# Sidebar for user inputs
with st.sidebar:
    st.header("Filter Options")
    
    # Country selection (multiple countries possible)
    available_countries = sorted(df['location'].unique())
    selected_countries = st.multiselect(
        'Select Countries',
        options=available_countries,
        default=['United States', 'China', 'Kenya']
    )
    
    # Date range selection
    min_date = df['date'].min().to_pydatetime()
    max_date = df['date'].max().to_pydatetime()
    start_date, end_date = st.slider(
        "Select Date Range",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date),
        format="YYYY-MM-DD"
    )

# Filter data based on user selections
filtered_data = df[
    (df['location'].isin(selected_countries)) & 
    (df['date'] >= start_date) & 
    (df['date'] <= end_date)
]

# Main dashboard
if not selected_countries:
    st.warning("Please select at least one country")
else:
    # Metrics row
    st.subheader("Key Metrics")
    cols = st.columns(len(selected_countries))
    
    for idx, country in enumerate(selected_countries):
        country_data = filtered_data[filtered_data['location'] == country]
        latest_data = country_data.iloc[-1] if not country_data.empty else None
        
        with cols[idx]:
            st.metric(
                label=country,
                value=f"{latest_data['total_cases']:,.0f}" if latest_data is not None else "N/A",
                delta=f"{latest_data['new_cases']:,.0f} new" if latest_data is not None else None
            )

    # Cases Over Time plot
    st.subheader('Cases Over Time')
    if not filtered_data.empty:
        fig = px.line(
            filtered_data,
            x='date',
            y='total_cases',
            color='location',
            labels={'total_cases': 'Total Cases', 'date': 'Date'},
            title='COVID-19 Cases Over Time'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for the selected filters")

    # Vaccinations Over Time plot
    if 'people_vaccinated' in filtered_data.columns:
        st.subheader('Vaccinations Over Time')
        fig = px.line(
            filtered_data,
            x='date',
            y='people_vaccinated',
            color='location',
            labels={'people_vaccinated': 'People Vaccinated', 'date': 'Date'},
            title='Vaccination Progress Over Time'
        )
        st.plotly_chart(fig, use_container_width=True)

    # Daily New Cases plot
    st.subheader('Daily New Cases')
    if not filtered_data.empty:
        fig = px.bar(
            filtered_data,
            x='date',
            y='new_cases',
            color='location',
            labels={'new_cases': 'New Cases', 'date': 'Date'},
            title='Daily New COVID-19 Cases',
            barmode='group'
        )
        st.plotly_chart(fig, use_container_width=True)

    # Data table
    st.subheader('Raw Data')
    st.dataframe(filtered_data.sort_values(['location', 'date']), use_container_width=True)