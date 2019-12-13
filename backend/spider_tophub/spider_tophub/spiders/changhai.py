# -*- coding: utf-8 -*-
from scrapy.spiders import Spider,CSVFeedSpider,XMLFeedSpider
from datetime import datetime ,timedelta
from spider_tophub.items import TopItem



class ChanghaiSpider(XMLFeedSpider):
    # 时间设置60分钟
    name = 'changhai'
    allowed_domains = ["changhai.org"]
    start_urls = [

        "https://www.changhai.org/feed.xml"
    ]
    iterator = 'xml'  # 缺省的iternodes，貌似对于有namespace的xml不行
    itertag = 'rss'
    custom_settings = {
        "node_id": 65,
        "type": 0,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "ROBOTSTXT_OBEY": False
    }

    def parse_node(self, response, selector):
        now_time = datetime.now()
        for node in selector.xpath('./channel/item'):
            item = TopItem()
            item['node_id'] = 65
            item['title'] = node.xpath('./title/text()').get()
            item['url'] = node.xpath('./link/text()').get()
            "28 Nov 2019 07:40:00 EST"
            item['publish_at'] = datetime.strptime(node.xpath('./pubDate/text()').get(),"%d %b %Y %H:%M:%S EST") + timedelta(hours=13)
            item['description_content'] = None
            item['create_at'] = now_time
            item['update_at'] = now_time
            item['position'] = None
            yield item











