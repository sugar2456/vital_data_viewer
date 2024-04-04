FROM python:3.9

WORKDIR /app

COPY ./docker/backend/requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend/ .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
