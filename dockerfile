# Base image with Python
FROM python:3.9-slim

# Create working directory
WORKDIR /app

# Copy the Python script and dataset into the container
COPY process_data.py /app/
COPY dataset /data

# Install dependencies
RUN pip install pandas

# Run the Python script
CMD ["python", "process_data.py"]
