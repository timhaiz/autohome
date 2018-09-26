# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AhItem(scrapy.Item):
    chexin = scrapy.Field()
    pingfen = scrapy.Field()
    renshu = scrapy.Field()
    link = scrapy.Field()
