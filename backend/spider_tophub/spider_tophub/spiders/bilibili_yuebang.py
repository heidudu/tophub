# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class BilibiliYuebangSpider(Spider):
    # 时间设置1.5分钟
    name = 'bilibili_yuebang'
    allowed_domains = ["bilibili.com/"]
    start_urls = [
        "https://www.bilibili.com/ranking/all/0/0/30"
    ]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "node_id": 97,
        # 热搜型
        "type": 1
    }

    def parse(self, response):
        time = datetime.now()
        for result in response.xpath('//li[@class="rank-item"]'):
            title = result.xpath('.//a[@class="title"]/text()').get()
            url = 'https:' + result.xpath('.//a[@class="title"]/@href').get()
            node_id = 97
            create_at = time
            update_at = time
            publish_at = time
            position = result.xpath('./div[1]/text()').get()
            description_content = result.xpath('.//div[@class="detail"]/span/text()').get()
            yield TopItem(publish_at=publish_at, title=title, url=url, node_id=node_id,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)








