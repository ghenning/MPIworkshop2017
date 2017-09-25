FROM ubuntu:16.04

ENV DEBIAN_FRONTENT noninteractive

USER root

RUN apt-get update && apt-get install -y \
    python \
    python-setuptools \
    python-pip


RUN apt-get -y clean

RUN pip install pip -U && \
    pip install setuptools -U && \
    pip install numpy -U && \
    pip install scipy -U && \
    pip install matplotlib -U
