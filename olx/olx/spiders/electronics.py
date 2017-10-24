"""OLX Crawler."""
# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule


class ElectronicsSpider(CrawlSpider):
    """Crawl many pages of electronics section using CrawlSpider class."""

    name = 'electronics'
    allowed_domains = ['www.olx.in']
    start_urls = ['https://www.olx.in/tv-video-audio/',
                  'https://www.olx.in/computers-accessories/',
                  'https://www.olx.in/games-entertainment/'
                  ]


    def parse(self, response):
        """Parse the content of the page."""
        print('Processing..' + response.url)
