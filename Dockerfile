FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl gcc build-essential libffi-dev libpq-dev libssl-dev pipx \
    && rm -rf /var/lib/apt/lists/*

RUN pipx install poetry
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
RUN poetry install --no-root --only main

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
RUN mkdir ./database/data
COPY database/connection ./database/connection
COPY database/schema.sql ./database/schema.sql
COPY database/data-setup.sql ./database/data-setup.sql

ENV VERSION="1.0.0"
ENV DEPLOYMENT="production"
ENV DEBUG="false"
ENV FIRST_SETUP="true"

EXPOSE 8080

CMD ["poetry", "run", "python", "main.py"]