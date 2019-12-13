# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str
import json


class AcfunZhoubangSpider(Spider):
    # 时间设置1.5分钟
    name = 'acfun_zhoubang'
    allowed_domains = ["acfun.cn"]
    start_urls = [
        "https://www.acfun.cn/rest/pc-direct/rank/channel?channelId=&subChannelId=&rankLimit=30&rankPeriod=WEEK"
    ]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "node_id": 102,
        # 热搜型
        "type": 1
    }

    def parse(self, response):
        now_time = datetime.now()
        data = json.loads(response.text)['rankList']
        i = 0
        for result in data:
            i += 1
            node_id = 102
            title = result['contentTitle']
            url = result['shareUrl']
            position = i
            description_content = int_to_str(result['viewCount'])
            create_at = now_time
            update_at = now_time
            publish_at = now_time
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)











