import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

# Sample regions and genders
regions = ['Central', 'Eastern', 'Northern', 'Western', 'Kampala']
genders = ['Male', 'Female']

# Number of voters
num_voters = 1000

# Generate data
data = {
    'Voter_ID': [f'V{1000+i}' for i in range(num_voters)],
    'Region': [choice(regions) for _ in range(num_voters)],
    'Age': [randint(18, 65) for _ in range(num_voters)],
    'Gender': [choice(genders) for _ in range(num_voters)],
    'Registration_Date': [
        (datetime(2023,1,1) + timedelta(days=randint(0, 364))).strftime('%Y-%m-%d') 
        for _ in range(num_voters)
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("mock_voter_data.csv", index=False)

# Show first 10 rows
# print(df.head(10))

print(df.info())
print(df.describe())
print(df['Region'].value_counts())
print(df['Gender'].value_counts())

# --- Step 3: Data Cleaning ---

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# Check for duplicates
print("Duplicate rows:", df.duplicated().sum())

# Remove duplicates (if any)
df = df.drop_duplicates()

# Convert Registration_Date to datetime format
df['Registration_Date'] = pd.to_datetime(df['Registration_Date'])

# Confirm changes
print(df.dtypes)

# --- Step 4: Feature Engineering ---

# 1. Extract Registration Month
df['Registration_Month'] = df['Registration_Date'].dt.month

# Optional: Convert month number to month name
df['Registration_Month_Name'] = df['Registration_Date'].dt.month_name()


# 2. Create Age Groups
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


# Preview new columns
print(df[['Age', 'Age_Group', 'Registration_Month_Name']].head(10))

# --- Step 5: Data Analysis ---

# 1. Voters per Region
voters_per_region = df['Region'].value_counts()
print("\nVoters per Region:\n", voters_per_region)

# 2. Gender Distribution
gender_distribution = df['Gender'].value_counts()
print("\nGender Distribution:\n", gender_distribution)

# 3. Age Group Distribution
age_group_distribution = df['Age_Group'].value_counts()
print("\nAge Group Distribution:\n", age_group_distribution)

# 4. Monthly Registration Trends
monthly_trend = df['Registration_Month_Name'].value_counts().sort_index()
print("\nMonthly Registration:\n", monthly_trend)

import matplotlib.pyplot as plt

# --- Step 6: Visualization ---

# 1. Bar Chart: Region Distribution
plt.figure()
voters_per_region.plot(kind='bar')
plt.title("Voters per Region")
plt.xlabel("Region")
plt.ylabel("Number of Voters")
plt.xticks(rotation=45)
plt.show()


# 2. Pie Chart: Age Groups
plt.figure()
age_group_distribution.plot(kind='pie', autopct='%1.1f%%')
plt.title("Age Group Distribution")
plt.ylabel("")
plt.show()


# 3. Line Graph: Monthly Registration Trends
plt.figure()
monthly_trend.plot(kind='line', marker='o')
plt.title("Monthly Voter Registration Trend")
plt.xlabel("Month")
plt.ylabel("Number of Registrations")
plt.xticks(rotation=45)
plt.show()
