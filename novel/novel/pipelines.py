# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class NovelPipeline(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        cname = settings['MONGODB_DOCNAME']

        client = pymongo.MongoClient(host=host,port=port)
        self.tdb = client[dbname]
        self.post = self.tdb[cname]


    def process_item(self, item, spider):
        if spider.name == 'NovelSPider':
            bookinfo = dict(item)
            self.tdb[item.collection].insert(bookinfo)
            # self.post.insert(bookinfo)
        if spider.name == 'chapter':
            chapterinfo = dict(item)
            self.tdb[item.collection].insert(chapterinfo)
        return item

