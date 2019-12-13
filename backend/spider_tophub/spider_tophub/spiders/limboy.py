# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class LimboySpider(Spider):
    # 时间设置60分钟
    name = 'limboy'
    allowed_domains = ["limboy.me"]
    start_urls = [
        "https://limboy.me/"
    ]
    custom_settings = {
        "node_id": 58,
        "type": 0,
        #"USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",


    }

    def parse(self, response):
        time = datetime.now()

        for result in response.xpath('//ul[@class="posts"]/li'):
            node_id = 58
            title = result.xpath('./a/text()').get()
            url = "https://limboy.me" + result.xpath('./a/@href').get()
            publish_at = datetime.strptime(result.xpath('./span[1]/text()').get(), "%Y-%m-%d")
            description_content = result.xpath('./span[2]/text()').get()
            create_at = time
            update_at = time
            position = None
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)














