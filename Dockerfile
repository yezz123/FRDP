# Pull base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y

RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel
RUN pip3 install gunicorn uvloop httptools



# Install dependencies
COPY pyproject.toml ./pyproject.toml
RUN pip install -e .[test,lint]

# Copy project
COPY . .

ENV ACCESS_LOG=${ACCESS_LOG:-/proc/1/fd/1}
ENV ERROR_LOG=${ERROR_LOG:-/proc/1/fd/2}
