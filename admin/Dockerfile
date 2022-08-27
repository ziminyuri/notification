FROM python:3.9.6-alpine

# рабочая директория внутри проекта
WORKDIR /usr/src/app

# переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgre
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
        pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .

CMD ["gunicorn", "-w", "1", "config.wsgi:application", "--bind", "0.0.0.0:8000"]