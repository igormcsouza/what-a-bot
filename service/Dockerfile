FROM python:3.8

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /app
COPY *.lock *.toml /app/
COPY libs/* /app/libs/
RUN poetry install

COPY . /app

CMD poetry run test