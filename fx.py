import streamlit as st
import pandas as pd

# Read the Excel file
df = pd.read_excel('c:\\users\\tvoil\\Dowloads\\FX Model.xlsx', sheet_name='FX Rate Forecasts')

# Function to filter data
def filter_data(df, region, currency, strategy):
    if region:
        df = df[df['Region'] == region]
    if currency:
        df = df[df['Currency'] == currency]
    if strategy:
        df = df[df['FY24 strategy'] == strategy]
    return df

# Streamlit web app
st.title('FX Rate Forecasts')

# User input for search functionality
region = st.text_input('Search by Region')
currency = st.text_input('Search by Currency')
strategy = st.text_input('Search by Strategy')

# Filter data based on user input
filtered_data = filter_data(df, region, currency, strategy)

# Display data
st.dataframe(filtered_data[['Region', 'Currency', 'FY24 strategy', 'FY24 Forecast', 'FY24 Target', 'Spot', 'Forwards']])
