# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class DoubanHuati24(Spider):
    # 时间设置1.5分钟
    name = 'douban_huati24'
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://www.douban.com/gallery/"
    ]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "node_id": 45,
        # 热搜型
        "type": 1,
        "ROBOTSTXT_OBEY": False,
    }

    def parse(self, response):
        time = datetime.now()
        i = 0
        for result in response.xpath('//*[@id="content"]/div/div[2]/div[3]//li'):
            i += 1
            title = result.xpath('./a/text()').get()
            url = result.xpath('./a/@href').get()
            node_id = 45
            create_at = time
            update_at = time
            publish_at = time
            position = i
            description_content = result.xpath('./span/text()').get()
            yield TopItem(publish_at=publish_at, title=title, url=url, node_id=node_id,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)





