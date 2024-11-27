# Use the official Python 3.12 image as the base
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app will listen on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]