# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request

class DoubanPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient(host=settings['MONGODB_HOST'],port=settings['MONGPDB_PORT'])
        self.tdb = client[settings["MONGODB_DNAME"]]

    def process_item(self, item, spider):
        book = dict(item)
        self.tdb[item.collection].insert(book)
        return item


class DoubanPostImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        url = item['bookPostUrl']
        yield Request(url)


    def item_completed(self, results, item, info):
        # 判断是否下载成功
        # TODO 记得setting里面的 ROBOTSTXT_OBEY=False 来防止反爬虫技术
        image_paths = [x['path'] for ok,x in results if ok]
        if not image_paths:
            DropItem('item contains no images')
        item['bookPostPath'] = image_paths[0]
        return item