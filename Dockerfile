# Use an official minimal base image with Python 3.11
FROM python:3.11.3-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0

# Install system dependencies (e.g., gcc for building wheels)
RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose Flask port
EXPOSE 5000

# Default command (can be overridden in docker run)
CMD ["flask", "run"]
