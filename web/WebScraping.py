import requests
import bs4

author_set = set()
quotes_list = []

base_url = "https://quotes.toscrape.com/page/{}/"

def get_quotes_and_author_list():
    page_number = 1;
    
    while page_number != -1:
        page_url = base_url.format(page_number)
        
        res = requests.get(page_url)
        soup = bs4.BeautifulSoup(res.text, "lxml")
        
        quotes = soup.select(".quote")
        
        for quote in quotes:
            print(quote.select(".text"))
            print(quote.select(".author"))
            quotes_list.append(quote.select(".text").text)
            author_set.add(quote.select(".author").text)
        
        page_number = page_number+1 if len(soup.select(".pager").select(".next")) != 0 else -1

def get_tag_items(page_url):
    tag_item_list = []
    
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    
    for item in soup.select(".tag-item"):
        tag_item_list.append(item.text)
    
    return tag_item_list

get_tag_items(base_url.format(1))
get_quotes_and_author_list()
