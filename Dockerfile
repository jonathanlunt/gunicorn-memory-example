FROM python:3.6-alpine3.8

RUN pip install gunicorn

COPY *.py /opt/
WORKDIR /opt

ENTRYPOINT ["gunicorn", "app:app", "-c", "config.py"]
