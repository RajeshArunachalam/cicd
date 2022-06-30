FROM python:3.8.10
RUN apt-get -y update 
RUN mkdir /waterlabsCurie
WORKDIR /waterlabsCurie
ARG NAME
ARG PASSWORD
ARG DB_USERNAME
ARG HOST
ARG PORT
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8
ENV NAME=${NAME}
ENV PASSWORD=${PASSWORD}
ENV DB_USERNAME=${DB_USERNAME}
ENV HOST=${HOST}
ENV PORT=${PORT}
COPY requirements.txt /waterlabsCurie/
COPY . /waterlabsCurie/
RUN pip install -r requirements.txt
RUN celery -A curie worker -l INFO &
RUN ["chmod", "+x", "./backend.sh"  ]
CMD ./backend.sh
