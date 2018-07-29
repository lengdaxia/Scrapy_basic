# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    collection = 'TOP_250_BOOKS'

    bookName = scrapy.Field()
    bookPostUrl = scrapy.Field()
    bookPostPath = scrapy.Field()
    bookRate = scrapy.Field()
    bookInfo = scrapy.Field()
    bookCommentNum = scrapy.Field()
    bookQuote = scrapy.Field()

    isRead = scrapy.Field()