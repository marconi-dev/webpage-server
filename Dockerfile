FROM python:3.10-alpine

WORKDIR /app
COPY requirements.txt /app
COPY . /app

# add dependencies for mysqlclient lib
RUN apk add gcc musl-dev mariadb-connector-c-dev

RUN pip install --root-user-action=ignore -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--chdir=./webpage", "webpage.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=2"]
