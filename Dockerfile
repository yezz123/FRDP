FROM ubuntu:16.04
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN apt-get update && apt-get upgrade -y

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./ /app

RUN apk add --no-cache --virtual .build-deps build-base \
  libressl-dev libffi-dev gcc musl-dev python3-dev \
  libc-dev libxslt-dev libxml2-dev bash \
  postgresql-dev \
  && pip install --upgrade pip setuptools wheel \
  && pip install --no-cache-dir -r /app/requirements.txt \
  && rm -rf /root/.cache/pip

ENV ACCESS_LOG=${ACCESS_LOG:-/proc/1/fd/1}
ENV ERROR_LOG=${ERROR_LOG:-/proc/1/fd/2}

ENTRYPOINT /usr/local/bin/gunicorn \
  -b 0.0.0.0:80 \
  -w 4 \
  -k uvicorn.workers.UvicornWorker main:app \
  --chdir /app \
  --access-logfile "$ACCESS_LOG" \
  --error-logfile "$ERROR_LOG"