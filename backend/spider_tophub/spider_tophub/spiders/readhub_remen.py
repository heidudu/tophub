# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime ,timedelta
from spider_tophub.items import TopItem
import json


class ReadhubRemenSpider(Spider):
    # 时间设置30分钟
    name = 'readhub_remen'
    allowed_domains = ["https://readhub.cn", "https://api.readhub.cn"]
    start_urls = [

        "https://api.readhub.cn/topic?lastCursor=&pageSize=20"
    ]
    custom_settings = {
        'node_id': 7,
        "type": 0,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        now_time = datetime.now()
        data = json.loads(response.text)['data']

        for result in data:
            node_id = 7
            title = result['title']
            url = 'https://readhub.cn/topic/' + str(result['id'])
            position = 0
            description_content = None
            create_at = now_time
            update_at = now_time
            #转换为时间戳便于排序
            publish_at = datetime.strptime(result['createdAt'], "%Y-%m-%dT%H:%M:%S.%fZ") + timedelta(hours=8)
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)




