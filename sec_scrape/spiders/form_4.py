# -*- coding: utf-8 -*-
import scrapy


class Form4Spider(scrapy.Spider):
    name = "form_4"
    allowed_domains = ["https://www.sec.gov"]
    start_urls = (
        'http://www.https://www.sec.gov/',
    )

    def parse(self, response):
        pass
