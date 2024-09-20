FROM python:3.10.11-bullseye

RUN apt update -y && apt upgrade -y
RUN apt -y install task-japanese locales-all
RUN apt -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt install -y vim less

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools

RUN mkdir /root/work

