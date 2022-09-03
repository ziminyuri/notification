FROM python:3.10-slim-buster
WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements/prod.requirements.txt .
RUN pip install -r prod.requirements.txt

COPY . .
WORKDIR /usr/app/src

CMD ["python", "main.py"]
