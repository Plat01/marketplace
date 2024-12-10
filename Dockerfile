FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update && apt upgrade -y

ADD pyproject.toml /app

RUN pip install --upgrade pip
# RUN pip install --proxy="http://root:<password>@109.120.155.18:1234" poetry  # or just add '"dns": ["8.8.8.8", "8.8.4.4"]' on /etc/docker/daemon.json
RUN pip install poetry  

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app