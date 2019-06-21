FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install --no-cache-dir psycopg2 \
    && apk del --no-cache .build-deps
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
