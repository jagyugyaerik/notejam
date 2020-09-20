FROM python:2-alpine

WORKDIR /app

COPY . /app

RUN apk add --virtual build-deps gcc musl-dev \
 && apk add --no-cache mariadb-dev
RUN pip install mysqlclient 
RUN apk del build-deps

RUN pip install -r requirements.txt

EXPOSE 5000/tcp

CMD ["python", "runserver.py"]