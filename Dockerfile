
# Use an official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 8080

# Run the Flask app
CMD ["python3", "app.py"]
