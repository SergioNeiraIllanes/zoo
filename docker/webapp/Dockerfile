FROM python:latest

RUN mkdir /webapp

WORKDIR /webapp

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8001