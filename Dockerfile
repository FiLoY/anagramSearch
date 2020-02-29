FROM python:3.8.1-slim

WORKDIR /app

EXPOSE 8080

ADD requirements.txt /app/

RUN pip install -r requirements.txt

ADD . /app/


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
