# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from datetime import datetime
from spider_tophub.items import TopItem
import json
from spider_tophub.utils import int_to_str


class KrZixunSpider(Spider):
    # 时间设置1小时
    name = '36kr_rebang'
    allowed_domains = ["https://36kr.com/"]
    start_urls = [
        "https://36kr.com/newsflashes"
    ]
    custom_settings = {
        "node_id": 3,
        "type": 1,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    # def parse(self, response):
    #     time = datetime.now()
    #     i = 0
    #     for result in response.xpath('//div[@class="kr-hotlist"]/div[2]/div'):
    #         i += 1
    #         item = TopItem()
    #         item['source'] = self.name
    #         item['description_title'] = '36氪24小时热榜'
    #         item['description_num'] = 0
    #         item['create_at'] = time
    #         item['update_at'] = time
    #         item['position'] = i
    #         if result.xpath('./@class').get() == 'hotlist-item-toptwo':
    #             item['title'] = result.xpath('.//a[@class="hotlist-item-toptwo-title"]/p/text()').get()
    #             item['url'] = 'https://36kr.com' + result.xpath('.//a[@class="hotlist-item-toptwo-title"]/@href').get()
    #         else:
    #             item['title'] = result.xpath('.//a[contains(@class,"hotlist-item-other-title")]/text()').get()
    #             item['url'] = 'https://36kr.com' + result.xpath('.//a[contains(@class,"hotlist-item-other-title")]/@href').get()
    #         yield item
    '''
        tree
            newsflashCatalogData
                code
                data
                    newsflashList
                    hotlist
                        code
                        data(list\10个)
    dict_keys(['id', 'goods_id', 'column_id', 'monographic_id', 'related_company_id', 'related_company_type', 'related_company_name', 'total_words', 'close_comment', 'title', 'catch_title', 'summary', 'cover', 'related_po
    st_ids', 'extraction_tags', 'extra', 'user_id', 'published_at', 'created_at', 'updated_at', 'counters', 'related_posts', 'is_free', 'is_tovc', 'template_info', 'has_audio', 'entity_flag', 'title_mobile', 'cover_mobile
    ', 'column', 'db_counters', 'user'])
    channel
    userInfo

    '''

    def parse(self, response):
        time = datetime.now()
        i = 0
        for result in json.loads(response.xpath('/html/body/script[1]').re(r"(window.initialState=)(.*\})")[1])['newsflashCatalogData']['data']['hotlist']['data']:
            i += 1
            item = TopItem()
            item['node_id'] = 3
            item['publish_at'] = datetime.strptime(result['published_at'], "%Y-%m-%d %H:%M:%S")
            item['description_content'] = int_to_str(result['counters']['view_count'])
            item['create_at'] = time
            item['update_at'] = time
            item['position'] = i
            item['title'] = result['title']
            item['url'] = 'https://36kr.com/p/' + str(result['id'])
            yield item








