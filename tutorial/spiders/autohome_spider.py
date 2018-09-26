#! python 3
# encoding: utf-8


import scrapy
from tutorial.items import AhItem

class AutohomeSpider(scrapy.Spider):
    name = 'autohome'
    allowed_domains = ['autohome.com.cn']
    start_urls = [
        # 小型SUV、紧凑型SUV、中型SUV、中大型SUV
        # 大型SUV、微型车、小型车、紧凑型车
        # 中型车、中大型车、大型车、MPV
        # 跑车、皮卡、微面
        'https://k.autohome.com.cn/suva01',
        'https://k.autohome.com.cn/suva1',
        'https://k.autohome.com.cn/suvb1',
        'https://k.autohome.com.cn/suvc1',
        'https://k.autohome.com.cn/suvd1',
        'https://k.autohome.com.cn/a001',
        'https://k.autohome.com.cn/a01',
        'https://k.autohome.com.cn/a1',
        'https://k.autohome.com.cn/b1',
        'https://k.autohome.com.cn/c1',
        'https://k.autohome.com.cn/d1',
        'https://k.autohome.com.cn/mpv1',
        'https://k.autohome.com.cn/p1',
        'https://k.autohome.com.cn/s1',
        'https://k.autohome.com.cn/mb1'
    ]

    def parse(self, response):
        for sel in response.xpath('//dd/ul/li'):
            item = AhItem()#Ah = Autohome
            item['chexin'] = sel.xpath('div[2]/a/text()').extract()
            item['pingfen'] = sel.xpath('div[3]/a/span[2]/text()').extract()
            item['renshu'] = sel.xpath('div[4]/a/text()').extract()
            item['link'] = sel.xpath('div[2]/a/@href').extract()
            yield item
