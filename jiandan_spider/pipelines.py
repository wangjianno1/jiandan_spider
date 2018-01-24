#!/usr/bin/env python
# -*- coding: utf-8 -*-  
"""
Author: 
Date:   2018-01-24 17:00
Desc:
"""
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class JianDanPipeline(object):
    def process_item(self, item, spider):
        print "MMMMMMMMMMMMMMMMMMMMMMMMMMM"
        print item['image_urls']
        return item

class JianDanImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            if image_url.startswith('//'): image_url = 'http:' + image_url
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
