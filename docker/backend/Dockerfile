FROM python:3.9

WORKDIR /app

COPY ./docker/backend/requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN export PYTHONPATH=$PYTHONPATH:/app/src

COPY ./backend/ .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
