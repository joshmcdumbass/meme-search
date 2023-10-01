# Stage 1: Install dependencies
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Stage 2: Set config and run app
ENV FLASK_ENV=production
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]