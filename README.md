📁 1. Project Structure
Make sure your project directory looks like this:

perl
Copy
Edit
my-flask-app/
├── app.py                # ← your Flask code
├── requirements.txt      # ← dependencies
├── Dockerfile            # ← for Docker build
├── templates/
│   └── hello.html        # ← Flask template file
└── data/
    └── testfile.txt      # ← for /read_file route
📜 2. Create requirements.txt
List dependencies used in your script:

txt
Copy
Edit
Flask==2.3.3
Add any other packages if needed.

🐳 3. Create a Dockerfile
Dockerfile
Copy
Edit
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
CMD ["python", "app.py"]
🏗️ 4. Build the Docker Image
Open a terminal in the my-flask-app directory:

bash
Copy
Edit
docker build -t flask-color-app .
🚀 5. Run the Container
bash
Copy
Edit
docker run -p 8080:8080 -v $(pwd)/data:/data flask-color-app
You can also set environment variables:

bash
Copy
Edit
docker run -p 8080:8080 -e APP_COLOR=blue -v $(pwd)/data:/data flask-color-app
🧪 6. Access the App
Visit http://localhost:8080 in your browser.

You can try:

/ → shows a random or preset color

/color/red → switches to red

/read_file → shows contents of testfile.txt
