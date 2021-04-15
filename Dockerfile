FROM python:3.9-slim
LABEL MAINTAINER="mehdy.khoshnoody@gmail.com"

ENV PYTHONBUFFERED 1

RUN apt update && apt install -y python3-dev build-essential
RUN pip install daphne pipenv

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pipenv install --system

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
