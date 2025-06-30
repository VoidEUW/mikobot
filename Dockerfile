FROM python:3.13-rc-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc curl libffi-dev libpq-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY api ./api
COPY routes ./routes
COPY templates ./templates
COPY static ./static
COPY bot ./bot
COPY main.py ./
COPY config.py ./
COPY init.py ./
COPY extensions.py ./
RUN mkdir ./database
COPY database/connection ./database/connection
COPY database/schema.sql ./database/schema.sql
COPY database/data-setup.sql ./database/data-setup.sql

ENV VERSION="1.0.0"
ENV DEPLOYMENT="production"
ENV DEBUG="false"
ENV FIRST_SETUP="true"

EXPOSE 8080

CMD ["python3", "main.py"]
