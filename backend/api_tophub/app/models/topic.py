# -*- coding: utf-8 -*-
from datetime import datetime
from app import db
import shortuuid

# 例如：综合 科技 社区
class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.Integer, primary_key=True)
    # 对外显示的ID
    uuid = db.Column(db.String(64), default=shortuuid.uuid, unique=True)
    # 名称
    name = db.Column(db.String(32), unique=True)
    # 图标名
    icon_name = db.Column(db.String(32))
    # 创建时间
    create_at = db.Column(db.DateTime(), default=datetime.utcnow())
    # 主题下的节点
    nodes = db.relationship('Node', backref=db.backref('topic'))

    def admin_to_json(self):
        return {
            "icon_name": self.icon_name,
            "name": self.name
        }

    def to_json(self):
        json_topic = {
            "id": self.uuid,
            "icon": self.icon_name,
            "name": self.name
        }
        return json_topic

    def __repr__(self):
        return '<Topic id={0},name={1}>'.format(self.uuid, self.name)



