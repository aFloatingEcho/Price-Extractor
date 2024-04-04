import requests # Used for obtaining the HTML.
from bs4 import BeautifulSoup # Used for parsing the HTML we've obtained.
import csv # Enable writing the data we've obtained into a file.
import re #Enable the usage of regular expressions

url = "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"

# Extraction Stage 
def book_page_extractor(url):
    '''
    Function used to extract one specific web page. Takes in a URL, and uses Beautiful Soup to extract
    each part of the book webpage.
    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # There's a table in the HTML that contains all the information that we need, so we'll be using that.
    # In more complicated webpages, we may need to make use of more compliated parsing mechanisms.
    list_of_t = soup.find_all("tr")
    page_info = [] # A list of tuples used to store information
    # product_page_url
    page_info.append(("product_page_url", url))
    # universal_ product_code (upc)
    page_info.append(("universal_product_code", list_of_t[0].contents[2].get_text()))
    # book_title
    # price_including_tax
    page_info.append(("product_description", list_of_t[2].contents[2].get_text()))
    # price_excluding_tax
    page_info.append(("product_description", list_of_t[3].contents[2].get_text()))
    # quantity_available
    # this particular piece of information is embedded in a string, so we have to extract the information from the string.
    # This requires regex due to the nature of the formatting
    available = (list_of_t[5].contents[3].get_text())
    number_available = re.findall('\d+',available)[0]
    page_info.append(("quantity_available", number_available))
    # product_description
    page_info.append(("product_description", list_of_t[6].contents[2].get_text()))
    # category
    # review_rating
    # image_url
    return page_info

print(book_page_extractor(url))