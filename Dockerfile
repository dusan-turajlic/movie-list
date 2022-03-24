ARG PYTHON_VERSION="3.10.3-slim"

FROM python:${PYTHON_VERSION} as base

WORKDIR /app

RUN apt update && \
    apt install -y gcc

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

FROM base as dev

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000

FROM base as prod

COPY main.py /app/main.py

CMD uvicorn main:app --host 0.0.0.0 --port 80
