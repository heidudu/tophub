# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime ,timedelta
from spider_tophub.items import TopItem
import json


class SmzdmHaojiaplSpider(Spider):
    # 时间设置30分钟
    name = 'smzdm_haojiapl'
    allowed_domains = ["smzdm.com"]
    start_urls = [

        "https://www.smzdm.com/top/json_more?rank_type=pinlei&rank_id=11&hour="
    ]
    custom_settings = {
        'node_id': 105,
        "type": 1,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        now_time = datetime.now()
        data = json.loads(response.text)['data']['list']
        for tmp in data:
            for result in tmp:
                node_id = 105
                title = result['article_title']
                url = 'https://www.smzdm.com/p/' + result['article_id']
                position = result['sort']
                description_content = result['article_price']
                create_at = now_time
                update_at = now_time
                publish_at = now_time
                yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                              description_content=description_content, create_at=create_at, update_at=update_at,
                              position=position)






