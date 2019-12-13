# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
import json


class IfanrLatestSpider(Spider):
    # 时间设置1小时
    name = 'ifanr_latest'
    allowed_domains = ["sso.ifanr.com"]
    start_urls = [
        "https://sso.ifanr.com/api/v5/wp/web-feed/"
    ]
    custom_settings = {
        "node_id": 82,
        "type": 0,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        time = datetime.now()
        data = json.loads(response.text)['objects']

        for result in data:
            publish_at = datetime.fromtimestamp(int(result["created_at"]))
            title = result['post_title']
            url = result['post_url']
            node_id = 82
            description_content = None
            create_at = time
            update_at = time
            position = 0
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=int(position))






