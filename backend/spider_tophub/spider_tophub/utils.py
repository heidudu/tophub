# -*- coding: utf-8 -*-
from os.path import realpath, dirname
import json
from spider_tophub.settings import ELASTICSEARCH_URL
from elasticsearch import Elasticsearch


def get_config(name):
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


# 如72000 =》 7.2万
def int_to_str(num):
    return str(round(num/10000, 1)) + "万"





def add_to_index(id, title, description_content,update_at, index="top" ):
    elasticsearch = Elasticsearch([ELASTICSEARCH_URL])
    if not elasticsearch:
        return
    if not elasticsearch.indices.exists(index=index):  # 如果是第一次插入，Index 还没创建
        # 创建 Index
        elasticsearch.indices.create(index=index, ignore=400)
        # IK 模板，这里假设每个字段都用 text 类型，如果你要修改，也可以通过 __searchable__ 传递过来

        searchable = {
            'title': {"type": "text", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"},
            'description_content': {"type": "string", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"},
            'update_at': {"type": "long", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"},
            # 'update_at': {"type": "date", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"}

        }

        mapping = {
            index: {
                "properties": searchable
            }
        }
        elasticsearch.indices.put_mapping(index=index, body=mapping)
    payload = {
        "title": title,
        "description_content":description_content,
        "update_at":int(update_at.timestamp()*1000)
    }
    elasticsearch.index(index=index, id=id, body=payload)



