# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class DoubanPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient(host=settings['MONGODB_HOST'],port=settings['MONGPDB_PORT'])
        self.tdb = client[settings["MONGODB_DNAME"]]

    def process_item(self, item, spider):
        book = dict(item)

        self.tdb[item.collection].insert(book)
        return item
