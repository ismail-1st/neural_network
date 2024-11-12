# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt first for better caching
COPY requirements.txt /app

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY neural_network.py /app

# Creates a shortcut during the build
RUN echo 'python /app/neural_network.py' > /usr/local/bin/run && chmod +x /usr/local/bin/run

# Set up default command to run the script
CMD ["python", "neural_network.py"]
