FROM python:3.9-slim

RUN adduser --disabled-password --gecos "" appuser

WORKDIR /app

COPY ./docker/backend/requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /app/requirements.txt

ENV PYTHONPATH=/app/src

COPY --chown=appuser:appuser ./backend/ .

USER appuser

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]