ARG PYTHON_VERSION="3.10.3-slim"

FROM python:${PYTHON_VERSION} as base

WORKDIR "/code"

RUN apt update && \
    apt install -y gcc

COPY requirements.txt /code/requirements.txt
COPY ./docker/docker-cmd.py /code/docker-cmd.py

RUN pip install --no-cache-dir -r requirements.txt

FROM base as dev

ENV STAGE="development"

CMD ./docker-cmd.py

FROM base as prod

ENV STAGE="production"

COPY ./app /code/app

CMD ./docker-cmd.py
