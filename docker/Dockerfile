ARG PYTHON_VERSION="3.10.3-slim"

FROM python:${PYTHON_VERSION} as base

WORKDIR "/code"

RUN apt update && \
    apt install -y gcc

COPY requirements.txt /code/requirements.txt
COPY ./docker/docker-entrypoint.py /code/docker-entrypoint.py

FROM base as dev

ENV STAGE="development"

CMD ./docker-entrypoint.py

FROM base as prod

ENV STAGE="production"

COPY ./app /code/app

CMD ['./docker-entrypoint.py']
