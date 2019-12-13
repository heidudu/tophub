# -*- coding: utf-8 -*-

from . import api
from app.models.node import Node
from flask import jsonify, request
from .errors import forbidden


@api.route('/node/detail')
def node_detail():
    node_id = request.args.get("id")
    if not node_id:
        return forbidden('invalid node_id')
    data = {}
    result = Node.query.filter_by(uuid=node_id).first()
    if result:
        data['detail'] = result.to_json(need_history=True)
        # 获取相关节点
        related_list = Node.query.filter(Node.source_id == result.source_id, Node.id != result.id).all()
        if related_list:
            data['related'] = [node.tiny_to_json() for node in related_list]
        else:
            data['related'] = None
        return jsonify({
            "success": True,
            "data": data
        })
    else:
        return jsonify({'success': True, "data": None})

