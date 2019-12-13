# -*- coding: utf-8 -*-
from scrapy.spiders import Spider,CSVFeedSpider
from datetime import datetime ,timedelta
from spider_tophub.items import TopItem



class FulibaZuixinSpider(Spider):
    # 时间设置60分钟
    name = 'fuliba_zuixin'
    allowed_domains = ["https://fulibus.net"]
    start_urls = [
        # "https://fulibus.net/"
        "https://fulibus.net/feed"
    ]
    custom_settings = {
        "node_id": 5,
        "type": 1,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        now_time = datetime.now()
        i = 0
        for result in response.xpath('//channel/item'):
            i += 1
            node_id = 5
            title = result.xpath('title/text()').get()
            url = result.xpath('link/text()').get()
            # 'Wed, 13 Nov 2019 07:01:48 +0000'
            publish_at = datetime.strptime(result.xpath('pubDate/text()').get(),"%a, %d %b %Y %H:%M:%S +0000") + timedelta(hours=8)
            description_content = result.xpath('category/text()').get()
            create_at = now_time
            update_at = now_time
            position = i
            if position:
                yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                              description_content=description_content, create_at=create_at, update_at=update_at,
                              position=position)






