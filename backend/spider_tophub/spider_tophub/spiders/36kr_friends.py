# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy import Request
from datetime import datetime
from spider_tophub.items import TopItem

import json
import time



class KrFriendsSpider(Spider):
    # 时间设置60分钟
    name = '36kr_friends'
    allowed_domains = ["36kr.com"]
    start_urls = [
        "https://36kr.com/user/375349"
    ]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "node_id": 2,
        # 普通型
        "type": 0
    }

    def parse(self, response):
        time_now = datetime.now()

        i = 20
        for result in json.loads(response.xpath('/html/body/script[1]').re(r"(window.initialState=)(.*\})")[1])['authorDetailData']['data']['authorArticleList']['data']:
            i -= 1
            item = TopItem()
            # 2019-11-13T20:01:05+08:00
            item['publish_at'] = datetime.strptime(result['published_at'], "%Y-%m-%dT%H:%M:%S+08:00")
            item['title'] = result['title']
            item['url'] = 'https://36kr.com/p/' + str(result['id'])
            item['node_id'] = 2
            item['position'] = 0
            item['create_at'] = time_now
            item['update_at'] = time_now
            yield Request(item['url'], meta={'item': item}, callback=self.detail_parse)
            yield item


    def detail_parse(self, response):
        item = response.meta['item']
        temp = response.xpath('//div[contains(@class,"articleDetailContent")]/p[1]/a/text()').get()
        if not temp:
            item['description_content'] = response.xpath('//div[contains(@class,"articleDetailContent")]/p[3]/a/text()').get()
        else:
            item['description_content'] = temp
        return item




