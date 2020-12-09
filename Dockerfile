FROM python:3.9.1-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apk add --no-cache \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install --no-cache-dir psycopg2==2.8
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
