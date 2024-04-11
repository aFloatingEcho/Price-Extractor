import requests # Used for obtaining the HTML.
from bs4 import BeautifulSoup # Used for parsing the HTML we've obtained.
import csv # Enable writing the data we've obtained into a file.
import re #Enable the usage of regular expressions

url = "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
file_path = 'output.csv'

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
    page_info.append(("product_description", "".join(list_of_p[3].contents)))
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

def convert_to_csv(page_extraction, path):
    '''
    page_extraction: should be a list of tuples that is extracted from each webpage
    path: location of where the csv is saved
    '''
    columns = []
    output = []
    for each in page_extraction:
        columns.append(each[0])
        output.append(each[1])
    output_wrapped = []
    output_wrapped.append(output)
    with (open(path, 'w')) as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(columns)
        csvwriter.writerows(output_wrapped)

info = book_page_extractor(url)
convert_to_csv(info, file_path)