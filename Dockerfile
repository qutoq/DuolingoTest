FROM python:3.10-slim

RUN mkdir /web
WORKDIR /web
COPY . /web

RUN pip install --no-cache-dir --upgrade -r requirements.txt
