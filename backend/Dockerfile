FROM python:3.7

COPY requirements.txt /home/backend/
WORKDIR /home/backend
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple 
COPY . /home/backend
CMD bash run.sh