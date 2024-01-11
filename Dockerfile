FROM python:3.10

RUN cat /etc/os-release

COPY requirements.txt ./requirements.txt

RUN apt-get install tzdata && \
    cp /usr/share/zoneinfo/Asia/Almaty  /etc/localtime && \
    /usr/local/bin/python -m pip install --upgrade pip && pip install -r /requirements.txt
