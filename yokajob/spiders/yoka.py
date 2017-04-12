# -*- coding: utf-8 -*-
import scrapy

from ..items import YokajobItem


class YokaSpider(scrapy.Spider):
    name = "yoka"
    allowed_domains = ["www.city.fukuoka.lg.jp"]
    start_urls = [
        'http://www.city.fukuoka.lg.jp/hofuku/shika-eiyo/health/kenko-dukuri/jisshiiryoukikanhigashi_2.html'
    ]

    def parse(self, response):
        for res in response.css(".borderAll > tbody > tr"):
            job = YokajobItem()
            job['title'] = res.xpath("//td[1]/span/text()").extract()
            job['address'] = res.xpath("//td[2]/span/text()").extract()
            job['tel'] = res.xpath("//td[3]/span/text()").extract()
            job['type'] = res.xpath("//td[4]/span/text()").extract()
            yield job
