from price_reader import scrape_category_info
# url of the book being extracted
url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
# filepath of the save location of extracted category (DO NOT CHANGE)
path = "extracted"

scrape_category_info(url, path)