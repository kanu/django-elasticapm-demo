# pull official base image
FROM python:3.7

# set work directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /usr/src/app/
WORKDIR /usr/src/app/demo
