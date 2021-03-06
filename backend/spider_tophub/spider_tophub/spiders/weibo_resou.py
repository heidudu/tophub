# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class WeiboResouSpider(Spider):
    # 时间设置1.5分钟
    name = 'weibo_resou'
    allowed_domains = ["s.weibo.com"]
    start_urls = [
        "https://s.weibo.com/top/summary?cate=realtimehot"
    ]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "node_id": 1,
        # 热搜型
        "type": 1
    }

    def parse(self, response):
        time = datetime.now()
        for result in response.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr'):
            title = result.xpath('td[2]/a/text()').get()
            url = 'https://s.weibo.com' + (result.xpath('td[2]/a/@href_to').get() if result.xpath('td[2]/a/@href_to').get() else result.xpath('td[2]/a/@href').get())
            node_id = 1
            create_at = time
            update_at = time
            publish_at = time
            position = result.xpath('td[contains(@class,"ranktop")]/text()').get()
            if position:
                description_content = int_to_str(int(result.xpath('td[2]/span/text()').get()))
                yield TopItem(publish_at=publish_at, title=title, url=url, node_id=node_id,
                              description_content=description_content, create_at=create_at, update_at=update_at,
                              position=position)




