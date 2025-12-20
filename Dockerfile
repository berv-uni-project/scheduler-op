FROM python:3.15.0a3-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apk add --no-cache \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x startup.sh
ENTRYPOINT [ "./startup.sh" ]
