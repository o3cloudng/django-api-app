# FROM python:3.10-alpine

# ENV PYTHONUNBUFFERED=1

# # RUN useradd -ms /bin/bash user
# # USER user

# WORKDIR /usr/src/app
# COPY ./requirements.txt ./


# RUN pip install -r requirements.txt


# pull the official base image
FROM alpine:latest

# Create a group and user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Tell docker that all future commands should run as the appuser user
USER appuser

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
ADD . .
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project

# RUN python manage.py migrate

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

