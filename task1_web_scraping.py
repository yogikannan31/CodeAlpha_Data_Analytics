import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

data = []

for quote, author in zip(quotes, authors):
    data.append({
        "Quote": quote.text,
        "Author": author.text
    })

df = pd.DataFrame(data)
df.to_csv("quotes_data.csv", index=False)

print("Web Scraping Completed Successfully")
