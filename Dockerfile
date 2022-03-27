ARG PYTHON_VERSION="3.10.3-slim"
ARG APP_USER="application"

FROM python:${PYTHON_VERSION} as base

ENV APP_HOME="/home/application/movie-list"

RUN apt update && \
    apt install -y gcc

RUN useradd -ms /bin/bash application
USER application

ENV PATH="/home/application/.local/bin:$PATH"
SHELL ["/bin/bash", "-c"]

WORKDIR $APP_HOME

COPY --chown=application:application server.py "${APP_HOME}/server.py"

FROM base as dev

ENV STAGE="development"

COPY --chown=application:application requirements-dev.txt "${APP_HOME}/requirements-dev.txt"
RUN pip install -r requirements-dev.txt

CMD python server.py

FROM base as prod

ENV STAGE="production"

COPY --chown=application:application requirements.txt "${APP_HOME}/requirements.txt"
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=application:application ./app "${APP_HOME}/app"

CMD python server.py
