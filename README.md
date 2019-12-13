# tophub
本项目结合自身所学，后端采用Python的flask框架，结合scrapy爬虫，前端使用React,再结合Elasticsearch的基础功能用于搜索，然后用Docker容器部署到服务器。
## 部署
```
1. git clone https://github.com/heidudu/tophub.git
2. 安装nodejs,docker,docker-compose
3. cd frontend
4. 安装环境包：npm install
5. 打包生产build文件夹：npm run build
6. 在 docker-compose.yml, backend/api_tophub/config.py,backend/spider_tophub/spider_tophub/settings 个人环境配置
7. docker-compose up
8. 进入backend 容器的spider_tophub目录，执行:scrapyd-deploy loachost

```
