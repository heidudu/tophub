# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime ,timedelta
from spider_tophub.items import TopItem



class MrpmSpider(Spider):
    # 时间设置60分钟
    name = 'mrpm'
    allowed_domains = ["http://mrpm.cc/"]
    start_urls = [
        "http://mrpm.cc/",

    ]
    custom_settings = {
        "node_id": 64,
        "type": 0,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        now_time = datetime.now()

        for result in response.xpath('//article'):

            node_id = 64
            title = result.xpath('./header/h1/a/text()').get()
            url = result.xpath('./header/h1/a/@href').get()
            # '2019-10-23T22:42:06+08:00'
            publish_at = datetime.strptime(result.xpath('./header/div/a/time/@datetime').get(), '%Y-%m-%dT%H:%M:%S+08:00')
            description_content = None
            create_at = now_time
            update_at = now_time
            position = None
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)








# -*- coding: utf-8 -*-





