# -*- coding: utf-8 -*-
from datetime import datetime
from app import db
import shortuuid
from .news import Top
from .base_search import SearchableMixin


def get_tops(node_id, num, type=0, need_history=False):
    tops_items = {
        "latest": [],
        "history": []
    }
    if type == 0:
        # 普通型按照publish_at排序
        result = Top.query.filter(Top.node_id == node_id).order_by(Top.publish_at.desc())
        tops_items["latest"] = [item.to_json(latest=True, type=0) for item in result.limit(num).all()]
        if need_history:
            # 排除最新的，历史数据前300条
            tops_items["history"] = [item.to_json(latest=False, type=0) for item in result.slice(num, 300+num).all()]
    elif type == 1:
        result1 = Top.query.filter(Top.node_id == node_id, Top.position != 0).order_by(Top.position.asc()).limit(num)
        tops_items["latest"] = [item.to_json(latest=True, type=1) for item in result1]
        if need_history:
            result2 = Top.query.filter(Top.node_id == node_id, Top.position == 0).order_by(Top.update_at.desc()).limit(300)
            tops_items["history"] = [item.to_json(latest=False, type=1) for item in result2]
    return tops_items





# 如微博.热搜榜中的 热搜榜
class Node(SearchableMixin,db.Model):
    __tablename__ = 'node'
    __searchable__ = {
        'name': {"type": "text", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"}
    }
    id = db.Column(db.Integer, primary_key=True)
    # 对外id
    uuid = db.Column(db.String(64), default=shortuuid.uuid, unique=True)
    # 名称
    name = db.Column(db.String(32))
    # 创建时间
    create_at = db.Column(db.DateTime(), default=datetime.utcnow())
    # 类型 0正常型 1热搜型[正常型：按照发布时间排序。热搜型：首页显示条目按照posiniton显示，历史数据按照update时间排序]
    type = db.Column(db.Integer, default=0)
    # 首页显示条目数
    num = db.Column(db.Integer, default=15)
    # 来源
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    # 爬虫内容
    tops = db.relationship('Top', backref=db.backref('node'))
    # 归属topic
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))

    # 联合唯一
    __table_args__ = (
        db.UniqueConstraint('name', 'source_id'),
    )

    def admin_to_json(self):
        return {
            "topic_id": self.topic.id,
            "source_id": self.source.id,
            "name": self.name,
            "type": self.type,
            "num": self.num,
        }

    def tiny_to_json(self):
        return {
            "topic_name": self.topic.name,
            "id": self.uuid,
            "source_name": self.source.name,
            "source_img": self.source.img_url,
            "name": self.name,

        }

    def to_json(self, need_history=False):
        json_node = {
            "topic_name":self.topic.name,
            "id": self.uuid,
            "source_name": self.source.name,
            "source_img": self.source.img_url,
            "name": self.name,
            "tops": get_tops(self.id, self.num, self.type, need_history)

        }
        return json_node

    def __repr__(self):
        return '<Node id={0},name={1}>'.format(self.uuid, self.name)


