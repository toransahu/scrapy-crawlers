"""OLX Crawler."""
# -*- coding: utf-8 -*-

import scrapy


class ElectronicsSpider(scrapy.Spider):
    """Crawl electronics section."""

    name = 'electronics'
    allowed_domains = ['www.olx.in']
    start_urls = ['http://www.olx.in/']

    def parse(self, response):
        """Parse the content of the page."""
        pass
