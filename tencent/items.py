# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):

    positionName = scrapy.Field()
    positionType = scrapy.Field()
    peropleNumber = scrapy.Field()
    positionLocation = scrapy.Field()
    publishTime = scrapy.Field()


