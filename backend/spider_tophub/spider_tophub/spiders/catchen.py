# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class CatchenSpider(Spider):
    # 时间设置60分钟
    name = 'catchen'
    allowed_domains = ["chinese.catchen.me/"]
    start_urls = [
        "https://chinese.catchen.me/"
    ]
    custom_settings = {
        "node_id": 68,
        "type": 0,
        #"USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",


    }

    def parse(self, response):
        time = datetime.now()

        for result in response.xpath('//div[@class="date-outer"]'):
            node_id = 68
            title = result.xpath('.//h3[contains(@class,"post-title")]/a/text()').get()
            url = result.xpath('.//h3[contains(@class,"post-title")]/a/@href').get()
            "2019-11-15T21:04:00-08:00"
            publish_at = datetime.strptime(result.xpath('.//abbr[@class="published"]/@title').get()[:-6], "%Y-%m-%dT%H:%M:%S")
            description_content = result.xpath('.//span[@class="post-labels"]/a/text()').get()
            create_at = time
            update_at = time
            position = None
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)
















