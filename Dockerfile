FROM python:3.6-slim

RUN pip install gunicorn

COPY *.py /opt/
WORKDIR /opt

ENTRYPOINT ["gunicorn",  "-c", "config.py", "app:app"]
