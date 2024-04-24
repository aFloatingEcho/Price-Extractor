import requests # Used for obtaining the HTML.
from bs4 import BeautifulSoup # Used for parsing the HTML we've obtained.
import csv # Enable writing the data we've obtained into a file.
import re #Enable the usage of regular expressions

url = "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
file_path = 'output.csv'
url2 = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"

website_to_scrape = "https://books.toscrape.com/"

# Extraction of Page Info 
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

def convert_to_csv(page_extraction, path, input):
    '''
    page_extraction: should be a list of tuples that is extracted from each webpage
    path: location of where the csv is saved
    '''
    columns = []
    output = []
    # parse each of the files into the columns and the output for each part, this only handles for one part
    for each in page_extraction:
        columns.append(each[0])
        output.append(each[1])
    output_wrapped = []
    output_wrapped.append(output)
    header = False
    with (open(path, 'a')) as csvfile:
        csvwriter = csv.writer(csvfile)
        if(input == 0):
            csvwriter.writerow(columns)
        csvwriter.writerows(output_wrapped)

def single_page_extract(page_extraction):
    '''
    Extracts the information from one page into a column.
    '''
    output = []
    for each in page_extraction:
        output.append(each[1])
    return output

# Extract List of Books 
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

def convert_urls_to_seek(url):
    modified_url = []
    for each in url:
        modified_url.append(each.replace("../../../", "https://books.toscrape.com/catalogue/"))
    return modified_url

def category_extraction(url):
    raw_list = list_of_books(url)
    urls_to_seek = convert_urls_to_seek(raw_list)
    no = 0
    for each in urls_to_seek:
        print(each)
        page_info = book_page_extractor(each)
        convert_to_csv(page_info, file_path, no)
        no += 1
    return urls_to_seek

def list_of_categories(page_to_parse):
    '''
    Function used to obtain the list of categories off of books.toscrape.com and prep the system to scrape
    each of the given categories.
    It returns an array of categories to search.
    '''
    main_page_get = requests.get(page_to_parse)
    main_page = BeautifulSoup(main_page_get.content, 'html.parser')
    list_of_ul = main_page.find_all("ul", class_="nav")
    list_of_categories = list_of_ul[0].find_all("li")
    print(list_of_categories)
    no = 0
    page_info = []
    # We skip over the first one because it's unusual.
    for each in list_of_categories[1:]:
        print(str(no) + " ...")
        # print(repr(each.text))
        # print("--")
        # print(each.contents[1].attrs)
        # How we figured it out: we used a for loop to inspect each of the objects within each itself,
        # turns out that's an object that somehow manages to do itself.
        link = each.contents[1]['href']
        text = (each.text).replace("\n\n                            \n                                ","")
        text = text.replace("\n                            \n                        \n","")
        print(link)
        print(repr(text))
        page_info.append([link, text])
        no += 1
    return page_info

print(category_extraction(url2))