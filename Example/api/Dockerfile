# FROM fmonsanto/pygdal

# RUN mkdir -p /code/
# WORKDIR /code
# ADD requirements.txt /code/
# ADD /apicode/ /code/
# RUN pip install -r requirements.txt	



FROM phusion/baseimage
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
# RUN pip install -r requirements.txt
EXPOSE 5000
COPY /apicode/ /code/
# ENTRYPOINT ["python"]
# CMD ["app.py"]
