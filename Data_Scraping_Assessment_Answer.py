# Module 11 - Data Scraping with Python
# Assessment Solution

# Import required libraries
import requests
from bs4 import BeautifulSoup

# URL of the website
url = "http://quotes.toscrape.com"

# Send HTTP request to fetch webpage content
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse the webpage using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quote containers
    quotes = soup.find_all("div", class_="quote")

    # Extract and print data
    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

        print("Quote:", text)
        print("Author:", author)
        print("Tags:", tags)
        print("-" * 50)
else:
    print("Failed to retrieve webpage. Status code:", response.status_code)
