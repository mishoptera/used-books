# A HUGE THANK YOU TO RAYMOND
# To run this code type the following the terminal: scrapy runspider mercari-scrape.py -o "sold_data.csv"

import scrapy
import re


class MercariItem(scrapy.Item):
    condition = scrapy.Field()
    shipping = scrapy.Field()
    brand = scrapy.Field()
    category = scrapy.Field()
    posted = scrapy.Field()
    seller_name = scrapy.Field()
    description = scrapy.Field()
    sold = scrapy.Field()
    price = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()

class Rspider(scrapy.Spider):
    name = 'rspider'
    # can alter url status (status 2 = sold, status 1 = for sale) and sortby (2 = newest first, 3 = lowtohigh, 4 = hightolow)

    start_urls = ["https://www.mercari.com/search/?categoryIds=1487&facets=2&length=9999999&sortBy=5"]
    base_url = 'https://mercari.com'
    allowed_domains = ['mercari.com']
    products = []
    download_delay = 2

    def parse(self, response):
        for link in response.css('a.Link__StyledPlainLink-dkjuk2-2.hykQP.Link__StyledAnchor-dkjuk2-0'):
            abslink = self.base_url + link.attrib['href']
            yield scrapy.Request(abslink, callback=self.second_parser, dont_filter = True)

    def second_parser(self, response):
        item = MercariItem()
        try:
            item_desc = response.css('p.Text__ProductText-sc-40whai-0.fndAKa')
            item['condition'] = item_desc[0].css('::text').get()
            item['shipping'] = item_desc[1].css('::text').get()
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
            # RAYMOND SAYS THEN WE JUST REGEX THIS HA!
            id_temp = id.extract_first().replace('"', '')
            id_temp_search = re.search(r'\d+', id_temp)
            item['id'] = id_temp_search

            print(item)
            yield(item)

        except:
            pass

        self.products.append(item)
