# -*- coding: utf-8 -*-
from flask import current_app
import requests


def run_spider(url, data):
    result= requests.post(url=url, data=data)
    return







def add_or_modify_job(spider_name, interval):
    url = current_app.config['SCRAPYD_URL'] + '/schedule.json'
    data = {"project": current_app.config["SCRAPY_PROJECT_NAME"], "spider": spider_name}
    result = current_app.scheduler.add_job(run_spider, args=[url, data], trigger="interval",  id=spider_name, replace_existing=True, minutes=interval)
    return None


def remove_job(spider_name):
    result = current_app.scheduler.get_job(spider_name)
    if result:
        current_app.scheduler.remove_job(spider_name)
    return None


# 移除不在task列表的jobs,添加不在jobs的tasks
# def refresh_jobs():
#     jobs = current_app.scheduler.get_jobs()
#     tasks = Task.query.all()
#     if (len(jobs)>0) and (len(tasks)>0):
#         jobs_ids = set([item.id for item in jobs])
#         tasks_names = set([item.name for item in tasks])
#         # jobs里面有多余
#         if len(jobs_ids-tasks_names) > 0:
#             for item in (jobs_ids-tasks_names):
#                 remove_job(item)
#
#     elif (len(jobs) > 0) and (len(tasks) == 0):
#         for item in jobs:
#             remove_job(item)



