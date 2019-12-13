# -*- coding: utf-8 -*-
from datetime import datetime
from app import db
from .base_search import SearchableMixin
from flask import current_app



class Top(SearchableMixin,db.Model):
    __tablename__ = 'top'
    __searchable__ = {
        'title': {"type": "text", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"},
        'description_content': {"type": "string", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"},
         'update_at': {"type": "long", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"},
        # 'update_at': {"type": "date", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"}

    }
    id = db.Column(db.Integer, primary_key=True)
    # 标题
    title = db.Column(db.String(256))
    # 链接
    url = db.Column(db.String(256))
    # 附加描述内容 如274.3万热度
    description_content = db.Column(db.String(64))
    # 创建日期
    create_at = db.Column(db.DateTime(), default=datetime.now())
    # 更新时间
    update_at = db.Column(db.DateTime(), default=datetime.now())
    # 排位
    position = db.Column(db.Integer, default=0)
    # 文章发布时间
    publish_at = db.Column(db.DateTime())
    # 归属节点id
    node_id = db.Column(db.Integer, db.ForeignKey('node.id'))

    # 联合唯一
    __table_args__ = (db.UniqueConstraint('node_id', 'url'),)

    def search_to_json(self):
        return {
            "url":self.url,
            "title": self.title,
            "source_img": self.node.source.img_url,
            "node_name": self.node.name,
            "source_name": self.node.source.name,
            "time": datetime.timestamp(self.update_at)

        }

    def to_json(self, latest=True,type=0):
        if latest:
            return {
                "url": self.url,
                "title": self.title,
                "description_content":self.description_content
            }
        else:
            if type == 0:
                return {
                    "url": self.url,
                    "title": self.title,
                    "description_content": self.description_content,
                    "time": datetime.timestamp(self.publish_at)
                }
            elif type == 1:
                return {
                    "url": self.url,
                    "title": self.title,
                    "description_content": self.description_content,
                    "time": datetime.timestamp(self.update_at)
                }

    @classmethod
    def search(cls, expression, page, per_page):
        if not current_app.elasticsearch:
            return [], 0, []
        # 中文分词器 ik 会将 query 拆分成哪些查找关键字，前端将通过正则表达式来高亮这些词

        search = current_app.elasticsearch.search(
            index=cls.__tablename__,
            body={'query': {
                'function_score': {
                    'query': {'multi_match': {'query': expression, 'fields': ['title','description_content']}},
                    'script_score': {
                        'script': "return ((0.08 / ((3.16*Math.pow(10,-11)) * Math.abs({0} - doc['update_at'].value) + 0.05)) + 1.0)".format(datetime.now().timestamp()*1000)

                    }

                }
            },
                'from': (page - 1) * per_page, 'size': per_page})
        ids = [int(hit['_id']) for hit in search['hits']['hits']]
        scores = [int(hit['_score']) for hit in search['hits']['hits']]
        total = search['hits']['total']['value']
        if total == 0:
            return cls.query.filter_by(id=0), 0, []
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(db.case(when, value=cls.id)), total, scores

    def __repr__(self):
        return '<Top %r>' % self.id
