# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem



class SmzdmHaowenSpider(Spider):
    # 时间设置60分钟
    name = 'smzdm_haowen'
    allowed_domains = ["post.smzdm.com"]
    start_urls = [
        "https://post.smzdm.com/hot_1/"
    ]
    custom_settings = {
        "node_id": 8,
        "type": 1,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    def parse(self, response):
        time_now = datetime.now()
        i = 0
        for result in response.xpath('//*[@id="feed-main-list"]/li'):
            i += 1
            node_id = 8
            title = result.xpath('.//h5[@class="z-feed-title"]/a/text()').get()
            url = result.xpath('.//h5[@class="z-feed-title"]/a/@href').get()
            # 2019-11-13 10:16:00
            publish_at = datetime.strptime(result.xpath('./@data-publish-time').get(), "%Y-%m-%d %H:%M:%S")
            create_at = time_now
            update_at = time_now
            position = i
            description_content = None
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)






