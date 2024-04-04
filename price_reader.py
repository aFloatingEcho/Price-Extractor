import requests # Used for obtaining the HTML.
from bs4 import BeautifulSoup # Used for parsing the HTML we've obtained.

url = "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)