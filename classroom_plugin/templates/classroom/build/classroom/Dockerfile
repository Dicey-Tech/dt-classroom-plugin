FROM docker.io/ubuntu:20.04
LABEL maintainer="Sofiane Bebert <s.bebert@diceytech.co.uk>"

RUN apt update && \
    apt upgrade -y && \
    # python 3.8
    apt install -y language-pack-en git python3 python3-pip libmysqlclient-dev
RUN ln -s /usr/bin/python3 /usr/bin/python


RUN mkdir /openedx
RUN git clone https://github.com/Dicey-Tech/dt-classroom --branch bbrsofiane/initial-development --depth 1 /openedx/dt-classroom
# --branch {{ OPENEDX_COMMON_VERSION }}
WORKDIR /openedx/dt-classroom

# python requirements
RUN pip3 install -r requirements/base.txt


EXPOSE 8180
CMD gunicorn --workers=2 --name classroom --bind=0.0.0.0:8180 --max-requests=1000 classroom.wsgi:application
