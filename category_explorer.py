import requests # Used for obtaining the HTML.
from bs4 import BeautifulSoup # Used for parsing the HTML we've obtained.
import csv # Enable writing the data we've obtained into a file.
import re

url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
url2 = "https://books.toscrape.com/catalogue/category/books/classics_6/index.html"

# Extraction Stage 
def list_of_books(page_to_parse):
    '''
    Function used to extract one specific web page. Takes in a URL, and uses Beautiful Soup to extract
    the list of books.
    '''
    page = requests.get(page_to_parse)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    page_info = []
    # product_page_url
    list_of_books = soup.find_all("a")
    no = 0
    for each in list_of_books:
        no += 1
        print(str(no) + " ------")
        print(each.get('href'))
        print(each.attrs)
        if(each.has_attr("title")):
            page_info.append(each.get('href'))
    print("....")
    return page_info

def list_of_books_in_page(page_to_extract):
    '''
    Function used to extract one specific web page. Takes in a URL, and uses Beautiful Soup to extract
    the list of books.
    page_to_extract: intakes the current page that is a soup object and extracts the list of books from the page
    '''
    page_info = []
    list_of_books = page_to_extract.find_all("a")
    no = 0
    for each in list_of_books:
        no += 1
        print(str(no) + " ------")
        print(each.get('href'))
        print(each.attrs)
        if(each.has_attr("title")):
            page_info.append(each.get('href'))
    return page_info

def check_next_page(page_to_parse):
    '''
    Function to check if there's another page or not.
    '''
    page = requests.get(page_to_parse)
    soup = BeautifulSoup(page.content, 'html.parser')
    next_page = []
    no = 0
    list_of_books = soup.find_all("a")
    for each in list_of_books:
        no += 1
        if (re.search(re.compile('page-'), each.get('href'))):
            return True
    return False

print(check_next_page(url))
print(check_next_page(url2))