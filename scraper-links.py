import scrapy

class Rspider(scrapy.Spider):
    name = 'rspider'

    #sortBy codes (2 = Newest first, 3 = low to high, 4 = high to low, )
    #URL FOR SOLD BOOKS
    #start_urls = ["https://www.mercari.com/search/?categoryIds=1487&facets=2&itemStatuses=2&length=999999&sortBy=3"]

    #URL FOR FOR SALE BOOKS
    start_urls = ["https://www.mercari.com/search/?categoryIds=1487&facets=2&itemStatuses=1&length=999999&sortBy=3"]
    base_url = 'https://mercari.com'
    allowed_domains = ['mercari.org']
    def parse(self, response):
        for link in response.css('a.Link__StyledPlainLink-dkjuk2-2.hykQP.Link__StyledAnchor-dkjuk2-0'):
            print(link.attrib['href'])

LOG_STDOUT = True
LOG_FILE = 'scraper-links-output.txt'
