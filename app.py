import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("mock_voter_data.csv")

# Create Age_Group column
def age_group(age):
    if age < 25:
        return '18-24'
    elif age < 35:
        return '25-34'
    elif age < 45:
        return '35-44'
    elif age < 55:
        return '45-54'
    else:
        return '55+'

df['Age_Group'] = df['Age'].apply(age_group)

st.title("Voter Registration Dashboard")

# Region Chart
st.subheader("Voters per Region")
region_counts = df['Region'].value_counts()
st.bar_chart(region_counts)

# Age Group Chart
st.subheader("Age Group Distribution")
age_counts = df['Age_Group'].value_counts()
st.write(age_counts)

# Monthly Trend
st.subheader("Monthly Registration Trends")
df['Registration_Date'] = pd.to_datetime(df['Registration_Date'])
df['Month'] = df['Registration_Date'].dt.month_name()
monthly = df['Month'].value_counts().sort_index()
st.line_chart(monthly)

