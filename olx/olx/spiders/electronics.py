"""OLX Crawler."""
# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ElectronicsSpider(CrawlSpider):
    """
    Crawl many pages of electronics section using CrawlSpider class.

    CrawlSpider: This class makes crawling many pages of a site easier.

    """

    name = 'electronics'
    allowed_domains = ['www.olx.in']
    start_urls = [
        'https://www.olx.in/tv-video-audio/',
        'https://www.olx.in/computers-accessories/',
        'https://www.olx.in/games-entertainment/'
    ]
    """
    Rules of navigating the site.

    LinkExtractor: actually takes parameters to draw navigation boundaries.
    restrict_css parameter: to set the class for NEXT page. Use inspect element
                            to find the class.
    follow parameter: to navigate till rule fails
    callback: parsing function to callback
    """
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        """Parse the content of the page."""
        print('Processing..' + response.url)
