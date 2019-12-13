# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
import json


class ZhihuRebangSpider(Spider):
    # 时间设置10分钟
    name = 'zhihu_rebang'
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
         # "https://www.zhihu.com/api/v3/explore/guest/feeds?limit=50"
        "https://www.zhihu.com/billboard"
    ]
    custom_settings = {
        "node_id": 10,
        "type": 1,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "ROBOTSTXT_OBEY": False,

    }
#
    #def parse(self, response):
    #    time = datetime.now()
    #    data = json.loads(response.text)['data']
    #    for result in data:
    #        source = self.name
    #        title = result['question']['title']
    #        url = 'https://www.zhihu.com/question/' + str(result['question']['id'])
    #        description_title = '微博热榜'
    #        description_content = result.xpath('td[2]/span/text()').get()
    #        create_at = time
    #        update_at = time
    #        position = result.xpath('td[contains(@class,"ranktop")]/text()').get()
    #        if position:
    #            yield TopItem(source=source, title=title, url=url, description_title=description_title,
    #                          description_content=description_content, create_at=create_at, update_at=update_at,
    #                          position=position)
    '''
        data
            initialState
                topstory
                    hotList
        {'styleType': '1', 'feedSpecific': {'trend': 0, 'score': 1567.060267638933, 'debut': False, 'answerCount': 411}, 'target': {'labelArea': {'trend': 0, 'type': 'trend', 'nightColor': '#B7302D', 'normalColor': '#F1403C'}
, 'metricsArea': {'text': '5007 万热度'}, 'titleArea': {'text': '如何看待华为 HR 胡玲于 2019.10.30 在华为内部论坛心声社区的发帖？'}, 'excerptArea': {'text': '华为 2012 实验室 HR 胡玲在华为心声论坛实名发帖，内容直指部
分 HR 领导、华为部分 HR 政策导向及华为企业文化，并称：“奉劝各位兄弟，不要相信 HR，他们没有诚信“。 发帖原文截图如下（以下截图来自公开网络）：'}, 'imageArea': {'url': ''}, 'link': {'url': 'https://www.zhihu.com/questi
on/353381490'}}, 'cardId': 'Q_353381490', 'attachedInfo': 'CjcIABADGgg0MDgwNzE0NiD7xuntBTAuOIMYQAByCTM1MzM4MTQ5MHgAqgEJYmlsbGJvYXJk0gEA', 'type': 'hot_list_feed', 'id': '0_1572528576.22'}

            
    '''
    def parse(self, response):
        data = json.loads(response.xpath('//script[@id="js-initialData"]/text()').get())['initialState']['topstory']['hotList']

        for index, result in enumerate(data):
            time = datetime.now()
            node_id = 10
            title = result['target']['titleArea']['text']
            url = result['target']['link']['url']
            publish_at = time
            description_content = result['target']['metricsArea']['text']
            create_at = time
            update_at = time
            position = index+1
            if position:
                yield TopItem(node_id=node_id, title=title, url=url, publish_at=publish_at,
                              description_content=description_content, create_at=create_at, update_at=update_at,
                              position=position)





