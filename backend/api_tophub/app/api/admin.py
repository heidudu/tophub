# -*- coding: utf-8 -*-
from . import api
from .decorators import admin_required
from flask import jsonify, request,current_app
from .errors import forbidden
from app.models import Node, Source, Topic,Task
from app import db
import requests
from app.utils import get_or_create
from datetime import datetime
from app.schendler import remove_job, add_or_modify_job



@api.route('/admin/nodes', methods=['GET'])
@admin_required()
def admin_get_nodes():
    try:
        data = {
            "data": [item.admin_to_json() for item in Node.query.all()],
            "source_lookup": {item.id: item.name for item in Source.query.all()},
            "topic_lookup": {item.id: item.name for item in Topic.query.all()}

        }
        return jsonify({
            "success": True,
            "data": data
        })
    except:
        return forbidden("未知的错误")


@api.route('/admin/nodes', methods=['POST'])
@admin_required()
def admin_add_nodes():
    new_data = request.get_json()['newData']
    result = Node.query.filter(Node.name == new_data['name'], Node.source_id == int(new_data['source_id'])).first()
    if result:
        return forbidden("已存在，不能重复添加")
    try:
        node = Node(type=int(new_data['type']),name=new_data['name'], source_id=int(new_data['source_id']), topic_id=int(new_data['topic_id']), num=int(new_data['num']))
        db.session.add(node)
        db.session.commit()
        return jsonify({
            'success': True,
            'data': True
        })
    except:
        db.session.rollback()
        return forbidden('添加失败')


@api.route('/admin/nodes', methods=['DELETE'])
@admin_required()
def admin_delete_nodes():
    old_data = request.get_json()['oldData']
    result = Node.query.filter(Node.name == old_data['name'], Node.source_id == int(old_data['source_id'])).first()
    if not result:
        return forbidden("不存在该节点")
    try:
        db.session.delete(result)
        db.session.commit()
        return jsonify({
            'success': True,
            'data': True
        })
    except:
        db.session.rollback()
        return forbidden('删除失败')


@api.route('/admin/nodes', methods=['PUT'])
@admin_required()
def admin_update_nodes():
    old_data = request.get_json()['oldData']
    new_data = request.get_json()['newData']
    result = Node.query.filter(Node.name == old_data['name'], Node.source_id == int(old_data['source_id'])).first()
    if not result:
        return forbidden("不存在该节点")
    try:
        result.name = new_data['name']
        result.source_id = int(new_data['source_id'])
        result.topic_id = int(new_data['topic_id'])
        result.num = int(new_data['num'])
        db.session.commit()
        return jsonify({
            'success': True,
            'data': True
        })
    except:
        db.session.rollback()
        return forbidden('修改失败')


# source处理
@api.route('/admin/source', methods=['GET'])
@admin_required()
def admin_get_source():
    try:
        data = {
            "data": [item.admin_to_json() for item in Source.query.all()],
        }
        return jsonify({
            "success": True,
            "data": data
        })
    except:
        return forbidden("未知的错误")


@api.route('/admin/source', methods=['POST'])
@admin_required()
def admin_add_source():
    new_data = request.get_json()['newData']
    result = Source.query.filter(Source.name == new_data['name']).first()
    if result:
        return forbidden("已存在，不能重复添加")
    try:
        source = Source(name=new_data['name'], img_url=new_data['img_url'])
        db.session.add(source)
        db.session.commit()
        return jsonify({
            'success': True,
            'data': True
        })
    except:
        db.session.rollback()
        return forbidden('添加失败')


@api.route('/admin/source', methods=['DELETE'])
@admin_required()
def admin_delete_source():
    old_data = request.get_json()['oldData']
    result = Source.query.filter(Source.name == old_data['name']).first()
    if not result:
        return forbidden("不存在该来源")
    try:
        db.session.delete(result)
        db.session.commit()
        return jsonify({
            'success': True,
            'data': True
        })
    except:
        db.session.rollback()
        return forbidden('删除失败')


@api.route('/admin/source', methods=['PUT'])
@admin_required()
def admin_update_source():
    old_data = request.get_json()['oldData']
    new_data = request.get_json()['newData']
    result = Source.query.filter(Source.name == old_data['name']).first()
    if not result:
        return forbidden("不存在该来源")
    try:
        result.name = new_data['name']
        result.img_url = new_data['img_url']
        db.session.commit()
        return jsonify({
            'success': True,
            'data': True
        })
    except:
        db.session.rollback()
        return forbidden('修改失败')

# topic处理
@api.route('/admin/topic', methods=['GET'])
@admin_required()
def admin_get_topic():
    try:
        data = {
            "data": [item.admin_to_json() for item in Topic.query.all()],
        }
        return jsonify({
            "success": True,
            "data": data
        })
    except:
        return forbidden("未知的错误")


@api.route('/admin/topic', methods=['POST'])
@admin_required()
def admin_add_topic():
    new_data = request.get_json()['newData']
    result = Topic.query.filter(Topic.name == new_data['name']).first()
    if result:
        return forbidden("已存在，不能重复添加")
    try:
        topic = Topic(name=new_data['name'], icon_name=new_data['icon_name'])
        db.session.add(topic)
        db.session.commit()
        return jsonify({
            'success': True,
            'data': True
        })
    except:
        db.session.rollback()
        return forbidden('添加失败')


@api.route('/admin/topic', methods=['DELETE'])
@admin_required()
def admin_delete_topic():
    old_data = request.get_json()['oldData']
    result = Topic.query.filter(Topic.name == old_data['name']).first()
    if not result:
        return forbidden("不存在该来源")
    try:
        db.session.delete(result)
        db.session.commit()
        return jsonify({
            'success': True,
            'data': True
        })
    except:
        db.session.rollback()
        return forbidden('删除失败')


@api.route('/admin/topic', methods=['PUT'])
@admin_required()
def admin_update_topic():
    old_data = request.get_json()['oldData']
    new_data = request.get_json()['newData']
    result = Topic.query.filter(Topic.name == old_data['name']).first()
    if not result:
        return forbidden("不存在该来源")
    try:
        result.name = new_data['name']
        result.icon_name = new_data['icon_name']
        db.session.commit()
        return jsonify({
            'success': True,
            'data': True
        })
    except:
        db.session.rollback()
        return forbidden('修改失败')


# project处理
@api.route('/admin/spider', methods=['GET'])
@admin_required()
def admin_get_spider():
    result1 = requests.get(url=(current_app.config['SCRAPYD_URL']+'/listversions.json'), params={"project": current_app.config["SCRAPY_PROJECT_NAME"]})
    if result1.status_code != 200:
        return forbidden("请求失败")
    result2 = requests.get(url=(current_app.config['SCRAPYD_URL']+'/listspiders.json'), params={"project": current_app.config["SCRAPY_PROJECT_NAME"]})
    if result2.status_code != 200:
        return forbidden("请求失败")
    spiders = []
    # 删除不在spiders的task
    result = Task.query.filter(Task.name.notin_(result2.json()['spiders'])).all()
    if len(result) > 0:
        for u in result:
            remove_job(u.name)
            db.session.delete(u)
        db.session.commit()

    # 获取task状态
    if len(result2.json()['spiders']) > 0:
        for item in result2.json()['spiders']:
            task = get_or_create(Task, name=item)
            spiders.append({
                "spider_name": task.name,
                "interval": task.interval,
                "status": 1 if (current_app.scheduler.get_job(task.name) and current_app.scheduler.get_job(task.name).next_run_time) else 0,
                "project_name": current_app.config["SCRAPY_PROJECT_NAME"],
                "current_version": datetime.fromtimestamp(int(result1.json()['versions'][-1])).strftime("%Y-%m-%d %H:%M:%S"),
                "history_version": datetime.fromtimestamp(int(result1.json()['versions'][-2])).strftime("%Y-%m-%d %H:%M:%S")
            })

    return jsonify({
        "success": True,
        "data": {
            "data": spiders,
            "project_name": current_app.config["SCRAPY_PROJECT_NAME"],
            "current_version": datetime.fromtimestamp(int(result1.json()['versions'][-1])).strftime("%Y-%m-%d %H:%M:%S"),
            "history_version": datetime.fromtimestamp(int(result1.json()['versions'][-2])).strftime("%Y-%m-%d %H:%M:%S"),
        }
    })


@api.route('/admin/spider', methods=['PUT'])
@admin_required()
def admin_update_spider():
    old_data = request.get_json()['oldData']
    new_data = request.get_json()['newData']
    result = Task.query.filter(Task.name == old_data['spider_name']).first()
    if not result:
        return forbidden("不存在该任务")
    try:
        result.interval = int(new_data['interval'])
        db.session.commit()
        # 在运行状态的job同步修改时间
        if int(new_data['status']) == 1 and current_app.scheduler.get_job(new_data['spider_name']).next_run_time:
            add_or_modify_job(new_data['spider_name'],int(new_data['interval']))

        return jsonify({
            'success': True,
            'data': True
        })
    except:
        db.session.rollback()
        return forbidden('修改失败')


@api.route('/admin/runspider', methods=['POST'])
@admin_required()
def admin_run_spider():

    data = request.get_json()['data']

    for item in data:
        add_or_modify_job(item['spider_name'], int(item['interval']))
    return jsonify({
        'success': True,
        'data':True
    })



@api.route('/admin/stopspider', methods=['POST'])
@admin_required()
def admin_stop_spider():

    data = request.get_json()['data']
    try:
        for item in data:
            remove_job(item['spider_name'])
        return jsonify({
            'success': True,
            'data':True
        })
    except:
        return forbidden("未知的错误")


