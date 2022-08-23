
FROM python:3.10-slim-buster
WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements/prod.requirements.txt .
RUN pip install -r prod.requirements.txt

EXPOSE 8007

COPY . .
WORKDIR /usr/app/src

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8007", "-k", "uvicorn.workers.UvicornWorker", "--workers", "2"]
