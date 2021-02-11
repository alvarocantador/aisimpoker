FROM python:3.6.10-slim

WORKDIR /app

RUN apt-get update

RUN apt-get install libgomp1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT flask run
