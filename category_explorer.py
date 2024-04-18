import requests # Used for obtaining the HTML.
from bs4 import BeautifulSoup # Used for parsing the HTML we've obtained.
import csv # Enable writing the data we've obtained into a file.
import re

url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
url2 = "https://books.toscrape.com/catalogue/category/books/classics_6/index.html"
url3 = "https://books.toscrape.com/catalogue/category/books/fiction_10/page-4.html"

# Extraction Stage 
def list_of_books(page_to_parse):
    '''
    Function used to extract the list of books in a single category, makes use of list_of_books_in_page()
    as well as check_next_page() to check if the next page exists.
    '''
    main_page_get = requests.get(page_to_parse)
    main_page = BeautifulSoup(main_page_get.content, 'html.parser')
    # print(soup.prettify())
    page_info = []
    page_info = page_info + list_of_books_in_page(main_page)
    currentPage = 1
    checkPage = check_next_page(main_page, currentPage)
    modified_url = page_to_parse.replace("index.html", "page-1.html")
    print("Page 1 Completed, Current Book Total: " + str(page_info.__len__()))
    while(checkPage):
        print("Doing Page " + str(currentPage))
        modified_url = modified_url.replace(str(currentPage - 1) + ".html", str(currentPage) + ".html")
        print(modified_url)
        modified_page_get = requests.get(modified_url)
        modified_page = BeautifulSoup(modified_page_get.content, 'html.parser')
        page_info = page_info + list_of_books_in_page(modified_page)
        checkPage = check_next_page(modified_page, currentPage)
        print("Page " + str(currentPage) + " Completed, Current Book Total: " + str(page_info.__len__()))
        currentPage += 1
    print(page_info.__len__())
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
        # print(str(no) + " ------")
        # print(each.get('href'))
        # print(each.attrs)
        if(each.has_attr("title")):
            page_info.append(each.get('href'))
    return page_info

def check_next_page(page_to_parse, currentPage):
    '''
    Function to check if there's another page or not.
    Intakes a soup object to check.
    '''
    no = 0
    next_page = currentPage + 1
    print(next_page)
    list_of_books = page_to_parse.find_all("a")
    for each in list_of_books:
        no += 1
        if (re.search(re.compile('page-' + str(next_page)), each.get('href'))):
            return True
    return False

def next_page_url(url):
    modified_url = url.replace("index.html", "page-2.html")
    return modified_url

print(list_of_books(url))