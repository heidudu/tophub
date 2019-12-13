# -*- coding: utf-8 -*-
from scrapy.spiders import Spider,CSVFeedSpider,XMLFeedSpider
from datetime import datetime ,timedelta
from spider_tophub.items import TopItem



class DevtangSpider(XMLFeedSpider):
    # 时间设置60分钟
    name = 'devtang'
    allowed_domains = ["blog.devtang.com/"]
    start_urls = [

        "http://blog.devtang.com/atom.xml"
    ]
    namespaces = [('atom', 'http://www.w3.org/2005/Atom')]
    iterator = 'xml'  # 缺省的iternodes，貌似对于有namespace的xml不行
    itertag = 'atom:entry'
    custom_settings = {
        "node_id": 56,
        "type": 0,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "ROBOTSTXT_OBEY": False
    }

    def parse_node(self, response, node):
        now_time = datetime.now()
        item = TopItem()
        item['node_id'] = 56
        item['title'] = node.xpath('atom:title/text()').get()
        item['url'] = node.xpath('atom:link/@href').get()
        item['publish_at'] = datetime.strptime(node.xpath('atom:published/text()').get(),"%Y-%m-%dT%H:%M:%S.000Z") + timedelta(hours=8)
        item['description_content'] = None
        item['create_at'] = now_time
        item['update_at'] = now_time
        item['position'] = None
        return item









