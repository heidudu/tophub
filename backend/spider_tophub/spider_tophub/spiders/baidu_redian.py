# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class BaiduRedianSpider(Spider):
    # 时间设置60分钟
    name = 'baidu_redian'
    allowed_domains = ["top.baidu.com"]
    start_urls = [
        "http://top.baidu.com/buzz?b=1&c=513&fr=topcategory_c513"
    ]
    custom_settings = {
        "node_id": 13,
        "type": 1,
        #"USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "ROBOTSTXT_OBEY": False

    }

    def parse(self, response):
        time = datetime.now()
        i = 0
        for result in response.xpath('//td[@class="keyword"]'):
            i += 1
            node_id = 13
            title = result.xpath('a/text()').get()
            url = result.xpath('a/@href').get()
            publish_at = time
            # 相邻td第二个
            description_content = int_to_str(int(result.xpath('./following-sibling::td[2]/span/text()').get()))
            create_at = time
            update_at = time
            position = i
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)








