# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem


class GithubTrendingtodaySpider(Spider):
    # 时间设置60分钟
    name = 'github_trendingtoday'
    allowed_domains = ["github.com"]
    start_urls = [
        "https://github.com/trending"
    ]
    custom_settings = {
        "node_id": 6,
        "type": 1,
        #"USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "ROBOTSTXT_OBEY": False

    }

    def parse(self, response):
        time = datetime.now()
        i = 0
        for result in response.xpath('//article[@class="Box-row"]'):
            i += 1
            node_id = 6
            title = result.xpath('h1/a/@href').get()[1:]
            url = 'https://github.com' + result.xpath('h1/a/@href').get()
            publish_at = time
            description_content = result.xpath('div[2]/a[1]')[0].xpath('string(.)').get().replace(' ', '').replace('\n', '').replace(',', '') + " stars"
            create_at = time
            update_at = time
            position = i
            yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                          description_content=description_content, create_at=create_at, update_at=update_at,
                          position=position)






