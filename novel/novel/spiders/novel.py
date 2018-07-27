from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from novel.items import *

from scrapy import Spider

class NovelSPider(Spider):

    name = 'NovelSPider'

    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):

        bookurllist = response.xpath('//article[@class="article-content"]//a/@href').extract()

        bookinfolist = response.xpath('//div[@class="homebook"]')

        for i in range(len(bookurllist)):
            url = bookurllist[i]
            bookname = bookinfolist[i].xpath('h2/text()').extract()[0]
            bookbrief = bookinfolist[i].xpath('p/text()').extract()[0]

            item = NovelItem()
            item['BookName'] = bookname
            item['BookChaptersUrl'] = url
            item['BookBrief'] = bookbrief
            yield item





