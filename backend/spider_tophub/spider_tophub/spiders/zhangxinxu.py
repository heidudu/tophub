# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime ,timedelta
from spider_tophub.items import TopItem



class ZhangxinxuSpider(Spider):
    # 时间设置60分钟
    name = 'zhangxinxu'
    allowed_domains = ["http://www.zhangxinxu.com/"]
    start_urls = [
        "http://www.zhangxinxu.com/life/feed/",
        "http://www.zhangxinxu.com/wordpress/feed/"
    ]
    custom_settings = {
        "node_id": 63,
        "type": 0,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        now_time = datetime.now()

        for result in response.xpath('//channel/item'):

            node_id = 63
            title = result.xpath('title/text()').get()
            url = result.xpath('link/text()').get()
            # 'Wed, 13 Nov 2019 07:01:48 +0000'
            publish_at = datetime.strptime(result.xpath('pubDate/text()').get(),"%a, %d %b %Y %H:%M:%S +0000") + timedelta(hours=8)
            description_content = result.xpath('category[1]/text()').get()
            create_at = now_time
            update_at = now_time
            position = None
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)








# -*- coding: utf-8 -*-



