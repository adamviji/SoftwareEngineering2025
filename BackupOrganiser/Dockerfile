FROM python:3.13-slim

WORKDIR /main

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy source code
COPY . .
# Expose Flask port
EXPOSE 5000
ENV PYTHONUNBUFFERED="yes"

# Run the application
ENTRYPOINT ["python3", "main.py"]
