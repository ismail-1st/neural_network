# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and the script
COPY neural_network.py /app

# Install the required package (numpy)
RUN pip install numpy

# Command to run your Python script
CMD ["python", "neural_network.py"]