#
# imagen de Docker para Graph4DS
#
# Incluye:
#  - Python2
#  - IPython Notebook
#  - SciPy, NumPy, etc (apra analisis de datos)
#  - graph-tool
#
# FROM ubuntu:15.04
FROM jupyter/datascience-notebook

MAINTAINER Ricardo Mansilla <ricardo.mansilla@me.com>

USER root
ADD /sudoers.txt /etc/sudoers
RUN chmod 440 /etc/sudoers
USER jovyan

ADD graph-tool.list /etc/apt/sources.list.d/graph-tool.list
RUN sudo apt-get update
RUN sudo apt-get install -y --force-yes python-graph-tool

WORKDIR /tutorials
