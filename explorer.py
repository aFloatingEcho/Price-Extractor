import requests # Used for obtaining the HTML.
from bs4 import BeautifulSoup # Used for parsing the HTML we've obtained.
import csv # Enable writing the data we've obtained into a file.
import re
import os
import string

url = "https://books.toscrape.com/catalogue/alice-in-wonderland-alices-adventures-in-wonderland-1_5/index.html"
url2 = "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
url3 = "https://books.toscrape.com/catalogue/worlds-elsewhere-journeys-around-shakespeares-globe_972/index.html"

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
    list_of_p = soup.find_all("p")
    page_info = [] # A list of tuples used to store information
    # product_page_url
    page_info.append(("product_page_url", url))
    # universal_ product_code (upc)
    page_info.append(("universal_product_code", list_of_t[0].contents[2].get_text()))
    # book_title
    page_info.append(("book_title", soup.find_all("li")[3].get_text()))
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
    print("----")
    this = soup.find_all("meta")
    no = 0
    for each in this:
        print(no)
        print(each.attrs)
        no += 1
    print(this[2].attrs['content'])
    page_info.append(("product_description", this[2].attrs['content']))
    # category
    # .strip to remove the newline
    page_info.append(("category", (soup.find_all("li")[2].get_text()).strip()))
    # review_rating
    # Have to do some odd magic to get the rankings of each of the items.
    ranking = soup.find_all("p",class_="star-rating")
    page_info.append(("review_rating", (ranking[0].attrs)['class'][1]))
    # image_url
    page_info.append(("image_url", "".join(soup.find_all("img")[0].attrs['src'])))
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


book_page_extractor(url2)
book_page_extractor(url3)