# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Specify the port number the container should expose
EXPOSE 5000

# Define the command to run the application
CMD ["python", "./app.py"]
