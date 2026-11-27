FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir flask redis

COPY app.py .
COPY templates/ ./templates/

EXPOSE 5002

CMD ["python", "app.py"]