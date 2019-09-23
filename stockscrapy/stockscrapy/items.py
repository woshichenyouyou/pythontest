# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    stock_names = scrapy.Field()
    score_h = scrapy.Field()
    score_l = scrapy.Field()
    score_tech = scrapy.Field()
    score_money = scrapy.Field()
    score_news = scrapy.Field()
    score_industry = scrapy.Field()
    score_basic = scrapy.Field()
    pass
