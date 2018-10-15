FROM phusion/baseimage
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
COPY /apicode/ /code/