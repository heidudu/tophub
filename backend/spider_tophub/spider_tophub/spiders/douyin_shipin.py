# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime ,timedelta
from spider_tophub.items import TopItem
import json
from ..utils import int_to_str


class DouyinShipinSpider(Spider):
    # 时间设置30分钟
    name = 'douyin_shipin'
    allowed_domains = ["iesdouyin.com"]
    start_urls = [

        "https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/aweme/"
    ]
    custom_settings = {
        'node_id': 99,
        "type": 1,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        now_time = datetime.now()
        data = json.loads(response.text)['aweme_list']
        i = 0
        for result in data:
            i += 1
            node_id = 99
            title = result['aweme_info']['desc']
            url = result['aweme_info']['share_url']
            position = i
            description_content = int_to_str(result['hot_value'])
            create_at = now_time
            update_at = now_time
            #转换为时间戳便于排序
            publish_at = now_time
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)






