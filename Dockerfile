FROM python:3.10-alpine
EXPOSE 8000
RUN apk update
RUN apk add libpq-dev build-base
RUN addgroup -S hello && adduser -S hello -G hello -h /home/hello -g hello -s /bin/ash

USER hello
WORKDIR /app
ENV PATH="${PATH}:/home/hello/.local/bin"

COPY gunicorn.conf.py /app/gunicorn.conf.py
COPY requirements.txt /app/requirements.txt
COPY hello /app/hello
COPY migrations /app/migrations

RUN pip install -r requirements.txt
CMD gunicorn -c /app/gunicorn.conf.py
