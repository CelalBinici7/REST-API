FROM python:3

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT python api_2.py


