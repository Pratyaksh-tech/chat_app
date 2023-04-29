# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /App

# Copy the application files into the working directory
COPY . /App

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["app", "run", "--host=0.0.0.0"]
