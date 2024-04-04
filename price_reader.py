import requests # Used for obtaining the HTML.
from bs4 import BeautifulSoup # Used for parsing the HTML we've obtained.
import csv # Enable writing the data we've obtained into a file.

url = "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"

# Extraction Stage 
def book_page_extractor(url):
    '''
    Function used to extract one specific web page. Takes in a URL, and uses Beautiful Soup to extract
    each part of the book webpage.
    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    page_info = [] # A list of tuples used to store information
    # product_page_url
    page_info.append(("product_page_url", url))
    # universal_ product_code (upc)

    # book_title
    # price_including_tax
    # price_excluding_tax
    # quantity_available
    # product_description
    # category
    # review_rating
    # image_url
    return page_info