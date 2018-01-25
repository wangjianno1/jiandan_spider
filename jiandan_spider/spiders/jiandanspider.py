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
    #start_urls = ["http://www.sohu.com/"]

    def parse(self, response):
        current_page_title = response.xpath('//title/text()').extract_first()
        #print current_page_title
        item = JianDanItem()
        item['image_urls'] = response.xpath('//img//@src').extract()
        item['dom_title']  = current_page_title
        yield item

        #new_url = 'http://djc027.com' + response.xpath('//a//@href').extract()[-2]
        #new_url = response.xpath('//a//@href').extract_first()
        #print new_url
        #if new_url: yield scrapy.Request(new_url,callback=self.parse)
