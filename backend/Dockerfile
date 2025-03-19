FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN sed -i 's/\r$//g' ./scripts/start.sh && chmod +x ./scripts/start.sh

RUN pip install --no-cache-dir -r requirements.txt

