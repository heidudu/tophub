# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
import json
from spider_tophub.utils import int_to_str


class PearvideoZongbangSpider(Spider):

    name = 'pearvideo_zongbang'
    allowed_domains = ["www.pearvideo.com"]
    start_urls = [
        "https://www.pearvideo.com/popular"
    ]
    custom_settings = {
        "node_id": 16,
        "type": 1,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
         "ROBOTSTXT_OBEY": False


    }

    def parse(self, response):
        now_time = datetime.now()

        i = 0
        for result in response.xpath('//ul[@class="popular-list"]/li'):
            i += 1
            node_id = 16
            title = result.xpath('div[2]/a/h2/text()').get()
            url = "https://www.pearvideo.com/" + result.xpath('div[2]/a/@href').get()
            position = i
            description_content = result.xpath('div[2]/div/span[@class="fav"]/text()').get()
            create_at = now_time
            update_at = now_time
            publish_at = now_time
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)













