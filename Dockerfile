FROM python:3.10.6-alpine

ENV PYTHONUNBUFFERED 1

# RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# # Tell docker that all future commands should run as the appuser user
# USER appuser

# COPY ./requirements.txt requirements.txt
COPY app/Pipfile ./ 
COPY app/Pipfile.lock ./ 

RUN apk add --update --no-cache postgresql-client jpeg-dev


RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN apk add --upgrade python3-tkinter

RUN pip3 install pipenv


# RUN pip3 install -r requirements.txt
RUN pipenv install

RUN apk del .tmp-build-deps

RUN mkdir /app

WORKDIR  /app

COPY ./app .


