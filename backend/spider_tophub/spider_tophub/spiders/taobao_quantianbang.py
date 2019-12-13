

# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime ,timedelta
from spider_tophub.items import TopItem
import json
from ..utils import int_to_str


class TaobaoQuantianbangSpider(Spider):
    # 时间设置30分钟
    name = 'taobao_quantianbang'
    allowed_domains = ["apimall.dataoke.com"]
    start_urls = [

        "http://apimall.dataoke.com//api/rushing-ranking/goods-list/v1?cId=0&type=2"
    ]
    custom_settings = {
        'node_id': 104,
        "type": 1,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        now_time = datetime.now()
        data = json.loads(response.text)['data']
        i = 0
        for result in data:
            i += 1
            node_id = 104
            title = result['dtitle'] + " 原价" + str(result['yuanjia']) + " 现价" + str(result['jiage'])
            url = 'http://shop.fulibus.net/index.php?r=/detailed&id={0}&jump=2'.format(str(result['id']))
            position = i
            description_content = "月销" + int_to_str(result['xiaoliang'])
            create_at = now_time
            update_at = now_time
            publish_at = now_time
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)








