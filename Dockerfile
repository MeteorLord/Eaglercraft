# Use the official Python image as base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and other dependencies
RUN pip install Flask

# Expose the Flask port
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=serve.py

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
