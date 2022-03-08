# Reference: https://fastapi.tiangolo.com/deployment/docker/

FROM python:3.9

RUN apt-get install nano
RUN apt-get install libpq-dev

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt