from scrapy.spiders import Spider
from scrapy.selector import Selector
from novel.items import *
from scrapy.http import Request
import pymongo
from scrapy.conf import settings

class ChapterSpider(Spider):

    name = 'chapter'
    allowed_domains = []

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        cname = settings['MONGODB_DOCNAME']

        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbname]
        self.post = tdb[cname]

    def start_requests(self):
        results = self.post.find({},{"BookChaptersUrl":1})
        for each in results:
            url = each["BookChaptersUrl"]
            print(url)
            yield Request(url)

    def parse(self, response):

        clist = response.xpath('//article[@class="excerpt excerpt-c3"]')

        for c in clist:
            url = c.xpath('a/@href').extract()[0]
            title = c.xpath('a/text()').extract()[0]

            item = ChapterItem()
            item['ChpaterUrl'] = url
            item['ChpaterTitle'] = title

            yield Request(url,callback=self.parse_detail,meta={'item':item})


    def parse_detail(self,response):
        selector = Selector(response)
        item = response.meta["item"]

        rawcontent = response.xpath('//article[@class="article-content"]/p/text()').extract()
        content = " ".join(rawcontent)

        item['ChpaterContent'] = content
        yield item

# if __name__ == '__main__':
#     ChapterSpider().start_requests()