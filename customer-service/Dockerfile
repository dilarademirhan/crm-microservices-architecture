FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DOCKER=1
ENV MONGODB_URL="mongodb://mongodb:27017/customer-db"
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

EXPOSE 5001

CMD ["python", "run.py"]