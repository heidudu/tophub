# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime ,timedelta
from spider_tophub.items import TopItem
import json


class ZhihuDailySpider(Spider):
    # 时间设置60分钟
    name = 'zhihu_daily'
    allowed_domains = ["http://news-at.zhihu.com"]
    start_urls = [

        "http://news-at.zhihu.com/api/4/news/latest"
    ]
    custom_settings = {
        'node_id': 11,
        "type": 0,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        now_time = datetime.now()
        data = json.loads(response.text)

        for result in (data['stories']+data['top_stories']):
            node_id = 11
            title = result['title']
            url =  result['url']
            position = 0
            description_content = None
            create_at = now_time
            update_at = now_time
            publish_at = now_time
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)






