# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import pymongo


class NovelItem(scrapy.Item):
    collection = 'Novel'
    BookName = scrapy.Field()  #书名
    BookTitle = scrapy.Field() #卷名
    BookChaptersUrl = scrapy.Field()
    BookBrief = scrapy.Field()


class ChapterItem(scrapy.Item):
    collection = 'Chapter'

    ChpaterTitle = scrapy.Field()  # 标题
    ChpaterUrl = scrapy.Field() #url
    ChpaterContent = scrapy.Field() #正文
