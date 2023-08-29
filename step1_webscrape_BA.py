# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL for British Airways reviews and the number of pages and reviews per page to scrape
base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 10
page_size = 100

# Create an empty list to store the reviews
reviews = []

# Loop through each page to scrape reviews
for i in range(1, pages + 1):
    # Inform the user about the progress of the scraping
    print(f"Scraping page {i}")

    # Create a URL for the current page, sorting reviews by post date in descending order
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    # Send a request to the constructed URL and get the HTML content
    response = requests.get(url)

    # Parse the received HTML content using BeautifulSoup
    content = response.content
    parsed_content = BeautifulSoup(content, 'html.parser')

    # Loop through each review block and extract the text content, then add it to the reviews list
    for para in parsed_content.find_all("div", {"class": "text_content"}):
        reviews.append(para.get_text())

    # Print the current count of collected reviews
    print(f"   ---> {len(reviews)} total reviews")

# Convert the list of reviews into a DataFrame for easier manipulation
df = pd.DataFrame()
df["reviews"] = reviews
# Display the first few rows of the DataFrame
df.head()

# Save the DataFrame to a CSV file for future reference
df.to_csv("BA_reviews.csv")
