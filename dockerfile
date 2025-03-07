# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY app/requirements.txt /app/requirements.txt

# Install the required packages
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code into the container
COPY app /app/
COPY static /static/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
