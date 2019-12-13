# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class Pojie52RenqiremenSpider(Spider):

    name = 'pojie52_renqiremen'
    allowed_domains = ["https://www.52pojie.cn/"]
    start_urls = [
        "https://www.52pojie.cn/forum.php"
    ]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "node_id": 88,
        # 热搜型
        "type": 1
    }

    def parse(self, response):
        time = datetime.now()
        i = 0
        for result in response.xpath('//tr[@class="toptitle_7ree"]/following-sibling::*[1]/td[3]/div/div'):
            i += 1
            title = result.xpath('./a/text()').get()
            url = 'https://www.52pojie.cn/' + result.xpath('./a/@href').get()
            node_id = 88
            create_at = time
            update_at = time
            publish_at = time
            position = i
            description_content = None
            yield TopItem(publish_at=publish_at, title=title, url=url, node_id=node_id,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)






