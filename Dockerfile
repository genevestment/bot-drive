FROM python:3.10-slim
RUN apt-get update -qy \
 && apt-get -qy install \
    build-essential \
    g++ \
    wget \
 && rm -rf /var/lib/apt/lists/* \
 && pip install --upgrade coverage pip-tools pytype yapf

ENV PYTHONUNBUFFERED=0
ENV PROJECT github.com/genevestment/bot-drive
WORKDIR /src/$PROJECT
