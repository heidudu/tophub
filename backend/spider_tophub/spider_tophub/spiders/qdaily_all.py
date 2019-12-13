# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class QdailyAllSpider(Spider):
    # 时间设置1.5分钟
    name = 'qdaily_all'
    allowed_domains = ["www.qdaily.com"]
    start_urls = [
        "https://www.qdaily.com/"
    ]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "node_id": 72,
        # 热搜型
        "type": 0
    }

    def parse(self, response):
        time = datetime.now()
        print("长度",len(response.xpath('//div[@class="page-content"]/div/div[contains(@class,"article")]')))
        for result in response.xpath('//div[@class="page-content"]/div/div[contains(@class,"article")]'):
            title =result.xpath('./a/div[2]/h3').xpath('string(.)').get()
            if title:
                url = 'https://www.qdaily.com' + result.xpath('./a/@href').get()
                node_id = 72
                create_at = time
                update_at = time
                "2019-12-02 14:27:56 +0800"
                publish_at = datetime.strptime(result.xpath('.//span[@class="smart-date"]/@data-origindate').get(), '%Y-%m-%d %H:%M:%S +0800')
                position = None
                description_content = None

                yield TopItem(publish_at=publish_at, title=title, url=url, node_id=node_id,
                              description_content=description_content, create_at=create_at, update_at=update_at,
                              position=position)






