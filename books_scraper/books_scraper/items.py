# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Books(scrapy.Item):
    # define the fields for your item here like:
    book_cover = scrapy.Field()
    ratings=scrapy.Field()
    book_name=scrapy.Field()
    price=scrapy.Field()
    stock_availability=scrapy.Field()
