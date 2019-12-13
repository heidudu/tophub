from . import api
from app.models.node import Node
from flask import jsonify, request,g
from .errors import forbidden
from .decorators import login_required
from app import db


@api.route('/follow/list')
@login_required()
def follow_list():
    if not g.current_user.nodes:
        return jsonify({
            "success": True,
            "data": None
        })
    else:
        return jsonify({
            "success": True,
            "data": [item.uuid for item in g.current_user.nodes]
        })


@api.route('/follow/add', methods=['POST'])
@login_required()
def add_follow():

    target_id = request.get_json()['id']
    if not target_id:
        return forbidden("lack target_id")
    target = Node.query.filter(Node.uuid == target_id).first()
    if not target:
        return forbidden("invalid target_id")
    try:
        user = g.current_user
        user.nodes.append(target)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            "success": True,
            "data": target_id
        })

    except:
        db.session.rollback()
        return forbidden("add fail")




@api.route('/follow/remove', methods=['POST'])
@login_required()
def remove_follow():
    target_id = request.get_json()['id']
    if not target_id:
        return forbidden("lack target_id")
    target = Node.query.filter(Node.uuid == target_id).first()
    if not target:
        return forbidden("invalid target_id")

    if target not in g.current_user.nodes:
        return jsonify({
            "success": True,
            "data": target_id
        })

    try:
        user = g.current_user
        user.nodes.remove(target)
        db.session.add(user)
        db.session.commit()
    except:
        db.session.rollback()
        return forbidden("remove fail")

    return jsonify({
        "success": True,
        "data": target_id
    })


@api.route('/follow/detail')
@login_required()
def follow_detail():
    if not g.current_user.nodes:
        return jsonify({
            "success": True,
            "data": None
        })
    else:
        return jsonify({
            "success": True,
            "data": [item.to_json() for item in g.current_user.nodes]
        })