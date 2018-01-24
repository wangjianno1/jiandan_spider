#!/usr/bin/env python
# -*- coding: utf-8 -*-  
"""
Author: wangjianno1@sina.com
Date:   2018-01-24 17:00
Desc:   scrapy spider
"""
import scrapy
from jiandan_spider.items import JianDanItem 


class JianDanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = []
    #start_urls = ["http://jiandan.net/ooxx/"]
    start_urls = ["http://www.sohu.com/"]

    def parse(self, response):
        item = JianDanItem()
        item['image_urls'] = response.xpath('//img//@src').extract()
        yield item

        #new_url= response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()
        #if new_url: yield scrapy.Request(new_url,callback=self.parse)
