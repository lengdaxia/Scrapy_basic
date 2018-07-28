# -*- coding: utf-8 -*-
import scrapy
from douban.items import *
from scrapy import Request
import re

class Top250booksSpider(scrapy.Spider):


    name = "top250books"
    start_urls = ['https://book.douban.com/top250?start=0']

    def parse(self, response):
        blist = response.xpath('//tr[@class="item"]')

        for book in blist:
            item = DoubanMovieItem()
            item['isRead'] = False

            title = book.xpath('td[2]/div/a/@title').extract_first()
            posturl = book.xpath('td[1]/a/img/@src').extract_first()
            info = book.xpath('td[2]/p[@class="pl"]/text()').extract_first()
            rate = book.xpath('td[2]/div[2]/span[2]/text()').extract_first()
            commentNo = book.xpath('td[2]/div[2]/span[3]/text()').extract_first()
            quote = book.xpath('td[2]/p[@class="quote"]/span/text()').extract_first()

            item['bookName'] = title
            item['bookPostUrl'] = posturl
            item['bookInfo'] = info
            item['bookRate'] = rate
            item['bookCommentNum'] = re.findall('(\d+)',commentNo)[0]
            item['bookQuote'] = quote
            yield item

        # continue next page parse if nextpagelink exist
        nextPageLink = response.xpath('//span[@class="next"]/a/@href').extract()
        if nextPageLink:
            nextPageLink = nextPageLink[0]
            print(nextPageLink)
            yield Request(nextPageLink,callback=self.parse)