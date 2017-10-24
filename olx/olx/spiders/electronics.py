# -*- coding: utf-8 -*-
import scrapy


class ElectronicsSpider(scrapy.Spider):
    name = 'electronics'
    allowed_domains = ['www.olx.in']
    start_urls = ['http://www.olx.in/']

    def parse(self, response):
        pass
