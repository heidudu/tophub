# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
from spider_tophub.utils import int_to_str


class RuanyifengSpider(Spider):
    # 时间设置1.5分钟 阮一峰
    name = 'ruanyifeng'
    allowed_domains = ["ruanyifeng.com"]
    start_urls = [
        "http://www.ruanyifeng.com/blog/archives.html"
    ]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "node_id": 48,
        # 热搜型
        "type": 0
    }

    def parse(self, response):
        time = datetime.now()
        for result in response.xpath('//*[@id="alpha-inner"]/div[3]/div/ul/li'):
            title = result.xpath('./a/text()').get()
            url = result.xpath('./a/@href').get()
            node_id = 48
            create_at = time
            update_at = time
            publish_at = datetime.strptime(result.xpath('./text()').get(), "%Y.%m.%d：")
            position = None
            description_content = None
            yield TopItem(publish_at=publish_at, title=title, url=url, node_id=node_id,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)
        result = response.xpath('//div[contains(@class,"entry-asset")]')
        title = result.xpath('./div[1]/h2/a/text()').get()
        url = result.xpath('./div[1]/h2/a/@href').get()
        node_id = 48
        create_at = time
        update_at = time
        position = None
        description_content = None
        publish_at = datetime.strptime(result.xpath('.//abbr/text()').get(), "%Y年%m月%d日 %H:%M")
        yield TopItem(publish_at=publish_at, title=title, url=url, node_id=node_id,
                      description_content=description_content, create_at=create_at, update_at=update_at,
                      position=position)


# -*- coding: utf-8 -*-

