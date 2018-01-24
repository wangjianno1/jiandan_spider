#!/usr/bin/env python
# -*- coding: utf-8 -*-  
"""
Author: 
Date:   2018-01-24 17:00
Desc:   
""" 

import scrapy


class JianDanItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
