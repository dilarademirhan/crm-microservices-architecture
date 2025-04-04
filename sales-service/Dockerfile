FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DOCKER=1
ENV SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@host.docker.internal:5432/salesdb

EXPOSE 5002

CMD ["python", "run.py"] 