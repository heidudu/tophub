# -*- coding: utf-8 -*-

from . import api
from app.models import Source,Node,Top
from flask import jsonify, request
from .errors import forbidden


@api.route('/search/list')
def search_list():
    q = request.args.get("q")
    if not q:
        return forbidden("invalid q")
    data = {
        "nodes":[],
        "content":[]
    }
    try:
        # 整理相关节点
        tmp = []
        sources, total, scores = Source.search(q, 1, 100)
        if total > 0:
            for item in sources.all():
                tmp.extend(item.nodes)
        nodes, total, scores = Node.search(q, 1, 100)
        if total > 0:
            tmp.extend(nodes.all())
        if tmp:
            # 数据去重后，获得完整内容
            data["nodes"] = [item.tiny_to_json() for item in list(set(tmp))]

        # 整理相关内容
        tops, total, scores = Top.search(q, 1, 100)
        if total > 0:
            data['content'] = [item.search_to_json() for item in tops.all()]
        return jsonify({
            "success": True,
            "data": data
        })
    except:
        return forbidden("检索失败")





