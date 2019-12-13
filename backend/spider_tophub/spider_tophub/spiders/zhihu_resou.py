# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
import json
from spider_tophub.utils import int_to_str


class ToutiaoHotwordsSpider(Spider):
    # 时间设置2分钟
    name = 'zhihu_resou'
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
        "https://www.zhihu.com/api/v4/search/top_search"
    ]
    custom_settings = {
        "node_id": 15,
        "type": 1,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
         "ROBOTSTXT_OBEY": False


    }

    def parse(self, response):
        now_time = datetime.now()
        data = json.loads(response.text)['top_search']["words"]
        i = 0
        for result in data:
            i += 1
            node_id = 15
            title = result['display_query']
            url = 'https://www.zhihu.com/search?q={}&type=content'.format(result['display_query'])
            position = i
            description_content = None
            create_at = now_time
            update_at = now_time
            publish_at = now_time
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)











