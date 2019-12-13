# -*- coding: utf-8 -*-
from app import db


# user和node的多对多中间表
# class UserNode(db.Model):
#     __tablename__ = 'user_node'
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
#     node_id = db.Column(db.Integer, db.ForeignKey('node.id'), primary_key=True)

user_node = db.Table(
    "user_node",
    db.Column("user_id", db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column("node_id", db.Integer, db.ForeignKey('node.id'), primary_key=True)
)