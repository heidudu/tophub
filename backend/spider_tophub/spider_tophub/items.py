# -*- coding: utf-8 -*-
from scrapy import Field, Item


class TopItem(Item):
    # # 来源
    # source = Field()
    # # 标题
    # title = Field()
    # # 链接
    # url = Field()
    # # 附加描述 如热搜度
    # description_title = Field()
    # # 附加描述值
    # description_content = Field()
    # # 创建日期
    # create_at = Field()
    # # 更新时间
    # update_at = Field()
    #
    # # 位置
    # position = Field()

    # 标题
    title = Field()
    # 链接
    url = Field()
    # 附加描述值
    description_content = Field()
    # 创建日期
    create_at = Field()
    # 更新时间
    update_at = Field()
    # 发布时间
    publish_at = Field()
    # 对应节点id
    node_id = Field()
    # 位置
    position = Field()


