from multiprocessing import Process
from scrapy import cmdline
import time
import logging


confs = [
    {
        "spider_name": "weibo_resou",
        "frequency": 90,
    },
    {
        "spider_name": "zhihu_rebang",
        "frequency": 600,
    },
    {
        "spider_name": "36kr_friends",
        "frequency": 3600,
    },
    {
        "spider_name": "36kr_rebang",
        "frequency": 3600,
    },
    {
        "spider_name": "chouti_xinre",
        "frequency": 3600,
    },
    {
        "spider_name": "fuliba_zuixin",
        "frequency": 3600,
    },
    {
        "spider_name": "github_trending",
        "frequency": 3600,
    },
    {
        "spider_name": "readhub_remen",
        "frequency": 1800,
    },
    {
        "spider_name": "smzdm_haowen",
        "frequency": 3600,
    },
    {
        "spider_name": "sspai_remen",
        "frequency": 7200,
    },
    {
        "spider_name": "zhihu_daily",
        "frequency": 3600,
    },
    {
        "spider_name": "pengpai_hotnews",
        "frequency": 300,
    },
    {
        "spider_name": "baidu_redian",
        "frequency": 120,
    },
    {
        "spider_name": "toutiao_hotwords",
        "frequency": 120,
    },
    {
        "spider_name": "zhihu_resou",
        "frequency": 120,
    },

]


def start_spider(spider_name, frequency):
    args = ["scrapy", "crawl", spider_name]
    while True:
        start = time.time()
        p = Process(target=cmdline.execute, args=(args,))
        p.start()
        p.join()
        logging.debug("### use time: %s" % (time.time() - start))
        time.sleep(frequency)


if __name__ == '__main__':
    for conf in confs:
        process = Process(target=start_spider, args=(conf["spider_name"], conf["frequency"]))
        process.start()








