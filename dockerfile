FROM python:3.8.10

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt