FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /garbageCollectionProject
WORKDIR /garbageCollectionProject
COPY requirements.txt /garbageCollectionProject/
RUN pip install -r requirements.txt
RUN pip install pipenv
COPY . /garbageCollectionProject/
