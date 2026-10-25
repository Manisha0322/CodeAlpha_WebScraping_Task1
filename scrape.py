
import requests
from bs4 import BeautifulSoup
import csv

print("Scraping Started...")

url = "https://quotes.toscrape.com/"
response = requests.get(url, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

data = []

for block in soup.find_all("div", class_="quote"):
    quote = block.find("span", class_="text").get_text(strip=True)
    author = block.find("small", class_="author").get_text(strip=True)
    data.append([quote, author])

with open("my_custom_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(data)

print("SUCCESS! Dataset created!")
print("Total records:", len(data))
print("File saved as my_custom_dataset.csv")
