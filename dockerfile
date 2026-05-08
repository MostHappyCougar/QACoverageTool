FROM python:3.11.15-trixie
COPY /code/cov_tool/requirements.txt .
RUN apt install build-essential & pip install --upgrade pip & pip install -r requirements.txt

COPY code .
RUN mkdir -p /volume/config
RUN mkdir -p /volume/input
RUN mkdir -p /volume/output
RUN apt update
RUN apt -y install graphviz

VOLUME ["./volume"]

ENTRYPOINT ./entrypoint.sh
