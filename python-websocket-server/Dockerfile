FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src/ ./src/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the WebSocket server
CMD ["python", "src/server.py"]