FROM python:3.12.4-bookworm

WORKDIR /app

COPY requirements.txt ./
COPY ./.chainlit ./
COPY chainlit.md ./
COPY main.py ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["chainlit", "run", "-h", "--port", "8080", "main.py"]