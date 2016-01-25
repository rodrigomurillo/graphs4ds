#
# imagen de Docker para Graph4DS
#
# Incluye:
#  - Python2
#  - graph-tool
#
FROM ubuntu:15.04

MAINTAINER Ricardo Mansilla <ricardo.mansilla@me.com>

RUN whoami

ADD graph-tool.list /etc/apt/sources.list.d/graph-tool.list
RUN apt-get update
RUN apt-get install -y --force-yes python-graph-tool

WORKDIR /source
