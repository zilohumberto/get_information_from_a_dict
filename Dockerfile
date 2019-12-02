from ubuntu:16.04

LABEL Creator: "Humberto Felipe Rodriguez Rodriguez"

RUN apt update -y

# Install dependencies
RUN apt-get update && apt-get install -yq --no-install-recommends python3 python3-virtualenv git

RUN apt install -yq  python3-pip

RUN apt install -yq python3-setuptools

RUN pip3 install --upgrade pip

RUN pip3 install --upgrade setuptools

RUN apt-get -yq install python3-tk

RUN pip3 install pipenv

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ADD . /trustart
WORKDIR /trustart

ENV PYTHONPATH /trustart/

RUN pipenv --python python3 install
