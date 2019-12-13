# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class Pojie52JinriretieSpider(Spider):

    name = 'pojie52_jinriretie'
    allowed_domains = ["www.52pojie.cn/"]
    start_urls = [
        "https://www.52pojie.cn/misc.php?mod=ranklist&type=thread&view=heats&orderby=today"
    ]
    custom_settings = {
        "ROBOTSTXT_OBEY": False,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "node_id": 87,
        # 热搜型
        "type": 1
    }

    def parse(self, response):
        time = datetime.now()
        i = 0
        for result in response.xpath('//*[@id="wp"]//tr[not(@class)]'):
            i += 1
            title = result.xpath('./th/a/text()').get()
            url = 'https://www.52pojie.cn/' + result.xpath('./th/a/@href').get()
            node_id = 87
            create_at = time
            update_at = time
            publish_at = time
            position = i
            description_content = None
            yield TopItem(publish_at=publish_at, title=title, url=url, node_id=node_id,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)








