FROM python:3.12.6-bookworm

WORKDIR /app

COPY requirements.chill.txt ./
COPY main.py ./
COPY .env ./

RUN pip install --no-cache-dir -r requirements.chill.txt

ENTRYPOINT ["chainlit", "run", "-h", "--host=0.0.0.0", "--port=8080", "main.py"]