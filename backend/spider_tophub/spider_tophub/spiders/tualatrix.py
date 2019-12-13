# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class TualatrixSpider(Spider):
    # 时间设置60分钟
    name = 'tualatrix'
    allowed_domains = ["imtx.me"]
    start_urls = [
        "https://imtx.me/"
    ]
    custom_settings = {
        "node_id": 57,
        "type": 0,
        #"USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",


    }

    def parse(self, response):
        time = datetime.now()

        for result in response.xpath('//li[@class="entry-item"]'):

            node_id = 57
            title = result.xpath('.//h2/a/text()').get()
            url = "https://imtx.me" + result.xpath('./div[2]/h2/a/@href').get()
            publish_at = datetime.strptime(result.xpath('.//time/text()').get(), "%b %d, %Y")
            # 相邻td第二个
            description_content = None
            create_at = time
            update_at = time
            position = None
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)












