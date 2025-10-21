FROM python:3.13-slim

WORKDIR /main
# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# Copy source code
COPY ./src ./src
# Expose Flask port
EXPOSE 5000
ENV PYTHONUNBUFFERED="yes"
# Run the application
ENTRYPOINT ["python3", "src/restinterface.py"]