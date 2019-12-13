# -*- coding: utf-8 -*-
from datetime import datetime
from app import db
from .base_search import SearchableMixin


# 如微博.热搜榜中的 微博
class Source(SearchableMixin, db.Model):
    __tablename__ = 'source'
    __searchable__ = {
        'name': {"type": "text", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"}
    }
    id = db.Column(db.Integer, primary_key=True)
    # 名称
    name = db.Column(db.String(32), unique=True, index=True)
    # 图标名
    img_url = db.Column(db.Text)
    # 创建时间
    create_at = db.Column(db.DateTime(), default=datetime.utcnow())
    # 属于此来源的节点
    nodes = db.relationship('Node', backref=db.backref('source'))

    def admin_to_json(self):
        return {
            'name':self.name,
            'img_url': self.img_url
        }

    def __repr__(self):
        return '<Source  name=%r>' % self.name

