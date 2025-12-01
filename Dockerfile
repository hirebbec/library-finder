FROM python:3.13-alpine

WORKDIR /usr/library-finder

ENV PYTHONUNBUFFERED=1 \
    TZ="Europe/Moscow"

COPY . .
