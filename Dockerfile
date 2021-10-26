FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
RUN apk add --update openssh
ENV STATIC_URL /static
ENV STATIC_PATH /Desktop/DevelopEirs/docker-services/app/static
COPY ./requirements.txt /Desktop/DevelopEirs/docker-services/requirements.txt
RUN pip install -r /Desktop/DevelopEirs/docker-services/requirements.txt