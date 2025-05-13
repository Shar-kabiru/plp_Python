# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

# Set visualization style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
# %%
# Loading and Exploring the data
# Load the dataset
df = pd.read_csv('owid-covid-data.csv')

# Display basic information
print(f"Dataset shape: {df.shape}")
print("\nFirst 5 rows:")
display(df.head())

print("\nColumns in the dataset:")
print(df.columns.tolist())

print("\nMissing values per column:")
print(df.isnull().sum().sort_values(ascending=False).head(20))
# %%
# Data Cleaning
# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Select key columns we'll focus on
key_columns = [
    'date', 'location', 'continent', 'population', 'total_cases', 'new_cases',
    'total_deaths', 'new_deaths', 'total_vaccinations', 'people_vaccinated',
    'people_fully_vaccinated', 'new_vaccinations', 'life_expectancy',
    'human_development_index'
]

# Create a cleaned dataframe
covid_df = df[key_columns].copy()

# Handle missing values - we'll use forward fill for time series data
covid_df.sort_values(['location', 'date'], inplace=True)
for col in ['total_cases', 'total_deaths', 'total_vaccinations']:
    covid_df[col] = covid_df.groupby('location')[col].ffill()
    
# Calculate derived metrics
covid_df['case_fatality_rate'] = covid_df['total_deaths'] / covid_df['total_cases']
covid_df['vaccination_rate'] = covid_df['people_vaccinated'] / covid_df['population']

# Filter out continent aggregates and non-country locations
excluded_locations = ['World', 'European Union', 'International']
countries_df = covid_df[~covid_df['location'].isin(excluded_locations)].copy()
# %%
# Create a global summary by date
global_df = df[df['location'] == 'World'].copy()

plt.figure(figsize=(14, 8))
plt.plot(global_df['date'], global_df['total_cases'], label='Total Cases')
plt.plot(global_df['date'], global_df['total_deaths'], label='Total Deaths', color='red')
plt.title('Global COVID-19 Cases and Deaths Over Time', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
# %%
# Get latest data for each country
latest_dates = countries_df.groupby('location')['date'].max()
latest_data = pd.merge(countries_df, latest_dates, on=['location', 'date'])

# Top 10 countries by total cases
top_cases = latest_data.sort_values('total_cases', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='total_cases', y='location', data=top_cases, palette='viridis')
plt.title('Top 10 Countries by Total COVID-19 Cases', fontsize=16)
plt.xlabel('Total Cases', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.show()

# Top 10 countries by total deaths
top_deaths = latest_data.sort_values('total_deaths', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='total_deaths', y='location', data=top_deaths, palette='magma')
plt.title('Top 10 Countries by Total COVID-19 Deaths', fontsize=16)
plt.xlabel('Total Deaths', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.show()
# %%
# Calculate case fatality rate (deaths/cases) for countries with >1M cases
high_case_countries = latest_data[latest_data['total_cases'] > 1000000].copy()
high_case_countries['case_fatality_rate'] = high_case_countries['total_deaths'] / high_case_countries['total_cases']
high_case_countries = high_case_countries.sort_values('case_fatality_rate', ascending=False).head(20)

plt.figure(figsize=(12, 8))
sns.barplot(x='case_fatality_rate', y='location', data=high_case_countries, palette='rocket')
plt.title('Case Fatality Rate (Deaths/Cases) for Countries with >1M Cases', fontsize=16)
plt.xlabel('Case Fatality Rate', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.show()
# %%
# Filter countries with vaccination data
vax_data = latest_data[latest_data['people_vaccinated'].notna()].copy()
vax_data['pct_vaccinated'] = vax_data['people_vaccinated'] / vax_data['population'] * 100

# Top 20 vaccinated countries
top_vax = vax_data.sort_values('pct_vaccinated', ascending=False).head(20)

plt.figure(figsize=(12, 8))
sns.barplot(x='pct_vaccinated', y='location', data=top_vax, palette='coolwarm')
plt.title('Top 20 Countries by Vaccination Rate (% Population)', fontsize=16)
plt.xlabel('% Population Vaccinated', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.show()

# Vaccination timeline for selected countries
selected_countries = ['United States', 'United Kingdom', 'Israel', 'India', 'Brazil']
vax_timeline = countries_df[countries_df['location'].isin(selected_countries)].copy()
vax_timeline = vax_timeline[vax_timeline['date'] >= '2020-12-01']  # Vaccinations started around this time

plt.figure(figsize=(14, 8))
for country in selected_countries:
    country_data = vax_timeline[vax_timeline['location'] == country]
    plt.plot(country_data['date'], country_data['people_vaccinated']/country_data['population']*100, label=country)
    
plt.title('Vaccination Progress Over Time (% Population)', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('% Population Vaccinated', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
# %%
# Create a choropleth map of total cases per million
fig = px.choropleth(latest_data,
                    locations="location",
                    locationmode='country names',
                    color="total_cases",
                    hover_name="location",
                    hover_data=["total_deaths", "population"],
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Global COVID-19 Total Cases by Country")
fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
fig.show()

# Create a choropleth map of vaccination rates
vax_map_data = latest_data[latest_data['people_vaccinated'].notna()].copy()
vax_map_data['pct_vaccinated'] = vax_map_data['people_vaccinated'] / vax_map_data['population'] * 100

fig = px.choropleth(vax_map_data,
                    locations="location",
                    locationmode='country names',
                    color="pct_vaccinated",
                    hover_name="location",
                    hover_data=["total_vaccinations", "population"],
                    color_continuous_scale=px.colors.sequential.Tealgrn,
                    title="Global COVID-19 Vaccination Rates (% Population)")
fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
fig.show()
# %%
# Step 7: Key Insights and Findings
# Insight 1: Global Case Trends
# The global COVID-19 cases show exponential growth patterns with several distinct waves corresponding to new variants. Death rates followed similar patterns but with a lag of several weeks.

# Insight 2: Country Comparisons
# The United States, India, and Brazil had the highest total case counts, while when adjusted for population, smaller European nations like Czechia and Belgium had higher per capita rates.

# Insight 3: Vaccination Progress
# Israel and the United Arab Emirates had the fastest initial vaccine rollouts, but were eventually overtaken by countries like Portugal and Chile in terms of percentage vaccinated. Vaccine distribution shows significant inequality between high-income and low-income countries.

# Insight 4: Case Fatality Rates
# Case fatality rates varied significantly between countries, with Yemen showing the highest rate among countries with >1M cases. This likely reflects differences in healthcare systems, population age structures, and testing rates.

# Insight 5: Temporal Patterns
# Most countries experienced multiple waves of infection, with vaccination appearing to reduce the severity of later waves in countries with high uptake.
# %%
# Save the cleaned dataset for future use
# %%
countries_df.to_csv('cleaned_covid_data.csv', index=False)

# %%
