###########
#  BASE   #
###########

FROM python:3.11-alpine3.16 as base

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


###########
# BUILDER #
###########

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
ENV POETRY_VERSION=1.4.0

RUN apk add --no-cache gcc libffi-dev musl-dev postgresql-dev
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl


###########
#  FINAL  #
###########
FROM base as final

COPY . .
RUN apk add --no-cache libffi libpq
COPY --from=builder /venv /venv
ENV PATH=/venv/bin:$PATH


