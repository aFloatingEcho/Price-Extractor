from price_reader import scrape_book_info

# url of the book being extracted
url = "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
# filepath of the save location of extracted book
path = "extracted/demo"

scrape_book_info(url, path)