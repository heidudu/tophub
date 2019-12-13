from . import api
from app.models import Topic, Node
from flask import jsonify, request
from .errors import forbidden


@api.route('/topic/nav')
def topic_nav():
    topic_list = [topic.to_json() for topic in Topic.query.all()]

    return jsonify({
        "success": True,
        "data": topic_list
    })


@api.route('/topic/items')
def topic_items():
    topic_id = request.args.get("id")
    page = int(request.args.get('page', 1))
    if not topic_id:
        return forbidden('invalid topic_id')
    # result = Topic.query.filter_by(uuid=topic_id).first().nodes
    # if result:
    #     topic_items = [node.to_json(need_history=False) for node in result]
    #     return jsonify({
    #         "success": True,
    #         "data": topic_items
    #     })
    # else:
    #     return jsonify({'success': True, "data": None})
    topic = Topic.query.filter_by(uuid=topic_id).first()
    if not topic:
        return forbidden("invalid topic_id")
    pagination = Node.query.filter(Node.topic_id == topic.id).paginate(page, per_page=8, error_out=False)
    data = [node.to_json(need_history=False) for node in pagination.items]
    return jsonify({
        'success': True,
        "data": data,
        "has_next": pagination.has_next,
        "current_page": pagination.page
    })

