# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class DoubanGroup(Spider):
    # 时间设置1.5分钟
    name = 'douban_group'
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://www.douban.com/group/explore"
    ]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "node_id": 47,
        # 热搜型
        "type": 1,
        "ROBOTSTXT_OBEY": False,
    }

    def parse(self, response):
        time = datetime.now()
        i = 0
        for result in response.xpath('//*[@class="channel-item"]/div[2]'):
            i += 1
            title = result.xpath('./h3/a/text()').get()
            url = result.xpath('./h3/a/@href').get()
            node_id = 47
            create_at = time
            update_at = time
            publish_at = time
            position = i
            description_content = result.xpath('.//span[@class="from"]/a/text()').get()
            yield TopItem(publish_at=publish_at, title=title, url=url, node_id=node_id,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)





# -*- coding: utf-8 -*-

