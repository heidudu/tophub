# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime ,timedelta
from spider_tophub.items import TopItem



class EstSpider(Spider):
    # 时间设置60分钟
    name = 'est'
    allowed_domains = ["blog.est.im"]
    start_urls = [

        "https://blog.est.im/"
    ]
    custom_settings = {
        "node_id": 70,
        "type": 0,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "ROBOTSTXT_OBEY": False
    }

    def parse(self, response):
        now_time = datetime.now()

        for result in response.xpath('//div[contains(@class,"blog-card")]/article'):

            node_id = 70
            title = result.xpath('./a/h2/text()').get()
            url = "https://blog.est.im/"+result.xpath('./a/@href').get()
            # '2019-10-31T19:59:27'
            publish_at = datetime.strptime(result.xpath('./div/p[1]/time/@datetime').get()[:-6],'%Y-%m-%dT%H:%M:%S')
            description_content = None
            create_at = now_time
            update_at = now_time
            position = None
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)










