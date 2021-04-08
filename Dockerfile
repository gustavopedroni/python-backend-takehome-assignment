# Pull base image
FROM python:3.9-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/app

# Install dependencies
RUN pip install pipenv

COPY Pipfile Pipfile.lock /usr/app/

RUN pipenv install --system --dev

COPY . /usr/app/src

WORKDIR /usr/app/src
