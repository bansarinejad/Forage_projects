import pandas as pd
import re

# Load the scraped data
df = pd.read_csv("BA_reviews.csv")

# Define a function to remove the unwanted strings
def remove_prefix(text):
    return re.sub(r'^(✅ Trip Verified \|)|^(Not Verified \|)', '', text).strip()

# Apply the function to the 'reviews' column
df['reviews'] = df['reviews'].apply(remove_prefix)

# Remove leading and trailing whitespaces
df['reviews'] = df['reviews'].str.strip()

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values - removing any rows where the review is missing
df = df.dropna(subset=['reviews'])

# Removing unnecessary characters (e.g., newlines)
df['reviews'] = df['reviews'].str.replace('\n', ' ').str.strip()

# Save the cleaned DataFrame to a new CSV file
df.to_csv("BA_reviews_cleaned.csv", index=False)
