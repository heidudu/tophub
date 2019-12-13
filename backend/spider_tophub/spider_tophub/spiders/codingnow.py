# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class CodingnowSpider(Spider):
    # 时间设置60分钟
    name = 'codingnow'
    allowed_domains = ["blog.codingnow.com"]
    start_urls = [
        "https://blog.codingnow.com/"
    ]
    custom_settings = {
        "node_id": 55,
        "type": 0,
        #"USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",


    }

    def parse(self, response):
        time = datetime.now()

        for result in response.xpath('//*[@id="alpha-inner"]/div[@class="entry"]'):

            node_id = 55
            title = result.xpath('./h3/text()').get()
            url = result.xpath('.//p[@class="entry-more-link"]/a/@href').get()
            publish_at = datetime.strptime(result.xpath('./preceding-sibling::*[2]/text()').get(), "%B %d, %Y")
            # 相邻td第二个
            description_content = None
            create_at = time
            update_at = time
            position = None
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)










