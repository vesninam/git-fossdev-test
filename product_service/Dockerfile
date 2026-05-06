FROM python:3.12-slim


WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --only main --no-root

COPY src/app ./app

#poetry run uvicorn src.app.main:app \
# --port 8001 --host 127.0.0.1
CMD ["poetry", "run", "uvicorn", "app.main:app", \
     "--host", "0.0.0.0", "--port", "8000"]

