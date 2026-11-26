# Stage 1: Build
FROM python:3.12-slim AS build

WORKDIR /app

RUN pip install --no-cache-dir --prefix=/install flask mysql-connector-python

# Stage 2: Runtime
FROM python:3.12-slim

WORKDIR /app

COPY --from=build /install /usr/local
COPY app.py .

EXPOSE 5002

CMD ["python", "app.py"]