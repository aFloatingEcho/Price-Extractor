import requests # Used for obtaining the HTML.
from bs4 import BeautifulSoup # Used for parsing the HTML we've obtained.
import csv # Enable writing the data we've obtained into a file.
import re

url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"

# Extraction Stage 
def book_page_extractor(page_to_parse):
    '''
    Function used to extract one specific web page. Takes in a URL, and uses Beautiful Soup to extract
    each part of the book webpage.
    '''
    page = requests.get(page_to_parse)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    page_info = [] # A list of tuples used to store information
    # product_page_url
    list_of_t = soup.find_all("tr")
    no = 0
    for each in list_of_t:
        no += 1
        print(str(no) + " ------")
        print(each.contents)
    print("....")
    return page_info

book_page_extractor(url)