FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY ./core /app

EXPOSE 8000

