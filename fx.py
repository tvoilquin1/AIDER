import streamlit as st
import pandas as pd

# Read the Excel file
df = pd.read_excel(r'C:\Users\tvoil\OneDrive\Desktop\Aider\FX Model.xlsx', sheet_name='FX Rate Forecasts')

# Function to filter data
def filter_data(df, region, currency, strategy):
    if region:
        df = df[df['Region'].str.lower().isin([r.lower() for r in region])]
    if currency:
        df = df[df['Currency'].str.lower().isin([c.lower() for c in currency])]
    if strategy:
        df = df[df['FY24 Strategy'].str.lower().isin([s.lower() for s in strategy])]
    return df

# Streamlit web app
st.title('FX Rate Forecasts')

# User input for search functionality
region = st.multiselect('Search by Region', options=list(df['Region'].unique()))
currency = st.multiselect('Search by Currency', options=list(df['Currency'].unique()))
strategy = st.multiselect('Search by Strategy', options=list(df['FY24 Strategy'].unique()))

# Filter data based on user input
filtered_data = filter_data(df, region, currency, strategy)

# Display data
st.dataframe(filtered_data[['Region', 'Currency', 'FY24 Strategy', 'FY24 Forecast', 'FY24 Target', 'Spot', 'Forwards']])
