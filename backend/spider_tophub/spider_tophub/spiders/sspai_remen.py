# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
import json


class SspaiRemenSpider(Spider):
    # 时间设置120分钟
    name = 'sspai_remen'
    allowed_domains = ["sspai.com"]
    start_urls = [
        "https://sspai.com/api/v1/articles?offset=0&limit=20&has_tag=1&tag=%E7%83%AD%E9%97%A8%E6%96%87%E7%AB%A0&include_total=false&type=recommend_to_home"
    ]
    custom_settings = {
        "node_id": 9,
        "type": 0,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        now_time = datetime.now()
        data = json.loads(response.text)['list']

        for result in data:
            node_id = 9
            title = result['title']
            url = 'https://sspai.com/post/' + str(result['id'])
            publish_at = datetime.fromtimestamp(result["recommend_to_home_at"])
            description_content = result['author']['nickname']
            create_at = now_time
            update_at = now_time
            #转换为时间戳便于排序
            position = 0
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)






