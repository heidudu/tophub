# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
import json
from spider_tophub.utils import int_to_str


class ToutiaoHotwordsSpider(Spider):
    # 时间设置2分钟
    name = 'toutiao_hotwords'
    allowed_domains = ["ib.snssdk.com"]
    start_urls = [
        "https://ib.snssdk.com/api/suggest_words/?business_id=10017"
    ]
    custom_settings = {
        "node_id": 14,
        "type": 1,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "ROBOTSTXT_OBEY": False


    }

    def parse(self, response):
        now_time = datetime.now()
        data = json.loads(response.text)['data'][0]["words"]
        i = 0
        for result in data:
            i += 1
            node_id = 14
            title = result['word']
            url = 'https://m.toutiao.com/search/?keyword=' + result['word']
            position = i
            description_content = int_to_str(result['params']['fake_click_cnt'])
            create_at = now_time
            update_at = now_time
            #转换为时间戳便于排序
            publish_at = now_time
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)









