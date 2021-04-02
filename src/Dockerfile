# Pull base image
FROM python:3.9-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src

# Install dependencies
RUN pip install pipenv

COPY Pipfile Pipfile.lock /usr/src/

RUN pipenv install --system --dev

COPY . /usr/src/

