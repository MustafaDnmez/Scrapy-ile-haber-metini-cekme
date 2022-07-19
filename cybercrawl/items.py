# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CybercrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    url=scrapy.Field()
    tittle=scrapy.Field()
    tag_wrapper=scrapy.Field()
    Time=scrapy.Field()
    contect=scrapy.Field()
