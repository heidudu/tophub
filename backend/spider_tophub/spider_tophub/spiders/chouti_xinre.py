# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
import json


class ChoutiXinreSpider(Spider):
    # 时间设置1小时
    name = 'chouti_xinre'
    allowed_domains = ["https://dig.chouti.com/"]
    start_urls = [
        "https://dig.chouti.com/link/hot"
    ]
    custom_settings = {
        "node_id": 4,
        "type": 0,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        time = datetime.now()
        data = json.loads(response.text)['data']

        for result in data:
            publish_at = datetime.fromtimestamp(int(result["time_into_pool"]/1000000))
            title = result['title']
            url = 'https://m.chouti.com/link/' + str(result['id'])
            node_id = 4
            description_content = None
            create_at = time
            update_at = time
            position = 0
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=int(position))




