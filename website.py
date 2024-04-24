import requests # Used for obtaining the HTML.
from bs4 import BeautifulSoup # Used for parsing the HTML we've obtained.
import csv # Enable writing the data we've obtained into a file.
import re

url = "https://books.toscrape.com/"

# Extraction Stage 
def list_of_categories(page_to_parse):
    '''
    Function used to extract the list of books in a single category, makes use of list_of_books_in_page()
    as well as check_next_page() to check if the next page exists.
    '''
    main_page_get = requests.get(page_to_parse)
    main_page = BeautifulSoup(main_page_get.content, 'html.parser')
    list_of_ul = main_page.find_all("ul", class_="nav")
    list_of_categories = list_of_ul[0].find_all("li")
    print(list_of_categories)
    no = 0
    for each in list_of_categories:
        print(str(no) + " ...")
        # print(repr(each.text))
        print("--")
        print(each)
        no += 1
    page_info = []
    return page_info

def list_of_categories2(page_to_parse):
    '''
    Function used to extract the list of books in a single category, makes use of list_of_books_in_page()
    as well as check_next_page() to check if the next page exists.
    '''
    main_page_get = requests.get(page_to_parse)
    main_page = BeautifulSoup(main_page_get.content, 'html.parser')
    list_of_ul = main_page.find_all("ul", class_="nav")
    list_of_categories = list_of_ul[0].find_all("li")
    print(list_of_categories)
    no = 0
    for each in list_of_categories:
        print(str(no) + " ...")
        # print(repr(each.text))
        print("--")
        print(each)
        no += 1
    page_info = []
    return page_info

print(list_of_categories(url))

