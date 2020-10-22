FROM python:latest

RUN pip install --upgrade pip


ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /code
ADD . /code

RUN apt-get install libffi-dev
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install
