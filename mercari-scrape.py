# A HUGE THANK YOU TO RAYMOND!
# To run this code type the following the terminal:
# scrapy runspider mercari-scrape.py -o "<NAME_OF_FILE.csv"

import scrapy
import re

class MercariItem(scrapy.Item):
    condition = scrapy.Field()
    shipping = scrapy.Field()
    seller_name = scrapy.Field()
    description = scrapy.Field()
    sold = scrapy.Field()
    price = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    #THE THREE CLASSES BELOW COMMENTED OUT ARE THE PROBLEM!
    brand = scrapy.Field()
    category = scrapy.Field()
    posted = scrapy.Field()

class Rspider(scrapy.Spider):
    name = 'rspider'

    #can alter url status below using the following changes to the url:
    #CategoryIDs = 1487 is for children's Books
    #itemStatuses: 2 = sold, status 1 = for sale
    #sortBy: 1=Best Match, 2 = newest first, 3 = lowtohigh, 4 = hightolow, 5 = number of likes

    start_urls = ["https://www.mercari.com/search/?categoryIds=1487&facets=1&itemConditions=2&itemStatuses=1&length=30&maxPrice=699&minPrice=600&sortBy=2", "https://www.mercari.com/search/?categoryIds=1487&facets=1&itemConditions=2&itemStatuses=1&length=30&maxPrice=799&minPrice=700&sortBy=2"]
    base_url = 'https://mercari.com'
    allowed_domains = ['mercari.com']
    products = []

    #download_delay was a method I tried when trying to figure out why spider wasn't scraping all possible pages
    #download_delay = 2

    def parse(self, response):
        for link in response.css('a.Link__StyledPlainLink-dkjuk2-2.hykQP.Link__StyledAnchor-dkjuk2-0'):
            abslink = self.base_url + link.attrib['href']
            yield scrapy.Request(abslink, callback=self.second_parser, priority = 2, dont_filter = True) # priority = 2 and dont_filer = True were other methods I tried to figure out why spider wasn't scraping all possible pages. Not sure if it has any impact at all.

    def second_parser(self, response):
        item = MercariItem()
        try:
            item_desc = response.css('p.Text__ProductText-sc-40whai-0.fndAKa')
            item['condition'] = item_desc[0].css('::text').get()
            item['shipping'] = item_desc[1].css('::text').get()
            #Below is the problem. ~20-30% of pages don't specify a 'Brand' so it causes the spider to skip those pages.
            item['brand'] = item_desc[2].css('a::text').get()
            item['category'] = item_desc[3].css('a::text').getall()
            item['posted'] = item_desc[4].css('::text').get()

            seller_name = response.css('p.ProfileBar__Name-sc-2z5a96-0::text')
            item['seller_name'] = seller_name[0].get()

            description = response.css('p.ItemDescription__DescriptionText-sc-1w7qr5f-0.RRzr::text')
            item['description'] = description[0].getall()

            sold = response.css('p.Text4__Text4Bold-sc-13740j8-2.hYkkI::text')
            item['sold'] = sold[0].get()

            price = response.css('p.Text__Text7-sc-1lvlnjo-8.esBdtC.Text-sc-1lvlnjo-0.fiqSKf::text')
            item['price'] = price[0].get()

            title = response.css('p.Text1__Text1Normal-sc-1lii7za-0.ifKbkO.Text__Text1-sc-1lvlnjo-2.gdOGft.Text-sc-1lvlnjo-0.cMHTdX::text')
            item['title'] = title[0].get()

            id = response.css('script#__NEXT_DATA__::text')
            id_temp = id.extract_first().replace('"', '')
            id_temp_search = re.search(r'\d+', id_temp)
            item['id'] = id_temp_search

            print(item)
            yield(item)

        except:
            pass

        self.products.append(item)
