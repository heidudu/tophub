# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class News163QuanfollowtodaySpider(Spider):
    # 时间设置60*8分钟
    name = 'news163_quanfollowtoday'
    allowed_domains = ["news.163.com"]
    start_urls = [
        "http://news.163.com/rank/"
    ]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "node_id": 32,
        # 热搜型
        "type": 1
    }

    def parse(self, response):
        time = datetime.now()
        for result in response.xpath('//div[contains(@class,"areabg1")]/div[3]/div/div[2]//tr[position()>=2]'):
            title = result.xpath('td[1]/a/text()').get()
            url = result.xpath('td[1]/a/@href').get()
            node_id = 32
            create_at = time
            update_at = time
            publish_at = time
            position = int(result.xpath('td[1]/span/text()').get())
            description_content = int_to_str(int(result.xpath('td[2]/text()').get()))
            yield TopItem(publish_at=publish_at, title=title, url=url, node_id=node_id,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)








