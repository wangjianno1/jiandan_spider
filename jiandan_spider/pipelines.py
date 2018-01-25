#!/usr/bin/env python
# -*- coding: utf-8 -*-  
"""
Author: wangjianno1@sina.com
Date:   2018-01-24 17:00
Desc:   Scrapy Pipeline
"""
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class JianDanPipeline(object):
    def process_item(self, item, spider):
        print item['image_urls']
        return item

class JianDanImagesPipeline(ImagesPipeline):
    """继承自ImagesPipeline的自定义图片保存的Pipeline
    """
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            if image_url.startswith('//'): image_url = 'http:' + image_url
            yield scrapy.Request(image_url, meta={'dom_title': item['dom_title']})
     
    def file_path(self, request, response=None, info=None):
        """修改图片的默认保存路径
        """
        dom_title = request.meta['dom_title'].encode('utf-8')
        image_guid = request.url.split('/')[-1]
        relative_path = 'full/{}/{}'.format(dom_title, image_guid)
        return relative_path

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
