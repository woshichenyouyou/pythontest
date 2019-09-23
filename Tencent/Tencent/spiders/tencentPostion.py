# -*- coding: utf-8 -*-
import scrapy


class TencentpostionSpider(scrapy.Spider):
    name = "tencentPostion"
    allowed_domains = ["tencent.com"]
    start_urls = (
        'http://www.tencent.com/',
    )

    def parse(self, response):
        pass
