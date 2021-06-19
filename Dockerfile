FROM python:3.9-slim-buster

RUN apt-get update

COPY ./requirements.txt /app/requirements.txt
RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt


RUN apt-get clean

WORKDIR /app

ENTRYPOINT [ "python" ]
