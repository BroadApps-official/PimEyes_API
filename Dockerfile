FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=2.1.3

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

# копируем только файлы зависимостей (важно для кеша docker)
COPY pyproject.toml poetry.lock ./

# отключаем virtualenv внутри контейнера
RUN poetry config virtualenvs.create false

# устанавливаем зависимости
RUN poetry install --no-interaction --no-ansi --no-root

# копируем код
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]