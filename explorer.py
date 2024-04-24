import requests # Used for obtaining the HTML.
from bs4 import BeautifulSoup # Used for parsing the HTML we've obtained.
import csv # Enable writing the data we've obtained into a file.
import re
import os
import string

url = "https://books.toscrape.com/catalogue/alice-in-wonderland-alices-adventures-in-wonderland-1_5/index.html"
url2 = "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"

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
    available = (list_of_t[5].contents[3].get_text())
    print(available)
    print(re.findall('\d+',available)[0])
    # universal_ product_code (upc)
    list_of_p = soup.find_all("p")
    print("".join(list_of_p[3].contents))
    # book_title
    # price_including_tax
    # price_excluding_tax
    # quantity_available
    # product_description
    # category
    # review_rating
    # image_url
    return page_info

def book_page_extractor2(page_to_parse):
    '''
    Function used to extract one specific web page. Takes in a URL, and uses Beautiful Soup to extract
    each part of the book webpage.
    '''
    page = requests.get(page_to_parse)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    page_info = [] # A list of tuples used to store information
    # product_page_url
    category = soup.find_all("li")
    print(soup.find_all("li")[2].get_text())
    print(soup.find_all("li")[3].get_text())
    no = 0
    for each in category:
        no += 1
        print(str(no) + " ------")
        print(each.contents)
    print("....")
    # universal_ product_code (upc)
    list_of_p = soup.find_all("p")
    print("".join(list_of_p[3].contents))
    # book_title
    # price_including_tax
    # price_excluding_tax
    # quantity_available
    # product_description
    # category
    # review_rating
    # image_url
    return page_info

def book_page_extractor3(page_to_parse):
    '''
    Function used to extract one specific web page. Takes in a URL, and uses Beautiful Soup to extract
    each part of the book webpage.
    '''
    page = requests.get(page_to_parse)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    page_info = [] # A list of tuples used to store information
    # product_page_url
    ranking = soup.find_all("p",class_="star-rating")
    print((ranking[0].attrs)['class'][1])
    no = 0
    for each in ranking:
        no += 1
        print(str(no) + " ------")
        print(each.attrs)
    print("....")
    # universal_ product_code (upc)
    list_of_p = soup.find_all("star-rating")
    # book_title
    # price_including_tax
    # price_excluding_tax
    # quantity_available
    # product_description
    # category
    # review_rating
    # image_url
    return page_info

def book_page_extractor4(page_to_parse):
    '''
    Function used to extract one specific web page. Takes in a URL, and uses Beautiful Soup to extract
    each part of the book webpage.
    '''
    page = requests.get(page_to_parse)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    page_info = [] # A list of tuples used to store information
    # product_page_url
    image_seek = soup.find_all("img")
    print(soup.find_all("img")[0].attrs['src'])
    no = 0
    for each in image_seek:
        no += 1
        print(str(no) + " ------")
        print(each.attrs)
        print(each.attrs['src'].replace("../../", "https://books.toscrape.com/"))
        try:
            r = requests.get(each.attrs['src'].replace("../../", "https://books.toscrape.com/")).content
            name = each.attrs['alt']
            safety = name.translate(str.maketrans("","", string.punctuation)) + ".jpg" # This line is meant to delete all invalid characters out of a filename.
            print(safety)
            with open(safety, 'wb') as handler:
                handler.write(r)  
        except:
            print("Fail!")
    # universal_ product_code (upc)
    list_of_p = soup.find_all("star-rating")
    # book_title
    # price_including_tax
    # price_excluding_tax
    # quantity_available
    # product_description
    # category
    # review_rating
    # image_url
    return page_info


book_page_extractor(url)