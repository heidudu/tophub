# -*- coding: utf-8 -*-
from datetime import datetime
from app import db
from .user_node import user_node




class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    # 角色 0：用户，  100：超级管理员
    role = db.Column(db.Integer, default=0)
    # 昵称
    nickname = db.Column(db.String(64), unique=True)
    # 创建日期
    create_at = db.Column(db.DateTime(), default=datetime.utcnow())
    # 头像
    avatar = db.Column(db.String(64))
    # 访问令牌
    access_token = db.Column(db.String(64))
    # 与其他表正反向引用
    auth = db.relationship('Auth', uselist=False, backref=db.backref('user'))
    tokens = db.relationship('Token', backref=db.backref('user'))
    # 订阅的节点
    nodes = db.relationship("Node", secondary=user_node, backref=db.backref('users'))


    def to_json(self):
        json_user = {
            'id': self.id,
            'nickname': self.nickname,
            'avatar': self.avatar,
            'role': 'admin' if self.role == 100 else 'user'

        }
        return json_user

    def __repr__(self):
        return '<User %r>' % self.nickname


