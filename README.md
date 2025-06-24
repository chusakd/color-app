# Flask Color Application - Docker Setup

This is a simple Flask application that displays different colored backgrounds and shows the hostname. The application can be easily containerized using Docker.

## Files Created

- `Dockerfile` - Container configuration
- `requirements.txt` - Python dependencies
- `app.py` - Flask application code
- `templates/hello.html` - HTML template
- `.dockerignore` - Files to exclude from Docker build
- `docker-compose.yml` - Container orchestration

## Building and Running

### Option 1: Using Docker directly

```bash
# Build the image
docker build -t flask-color-app .

# Run the container
docker run -p 8080:8080 flask-color-app

# Run with custom color
docker run -p 8080:8080 -e APP_COLOR=red flask-color-app
```

### Option 2: Using Docker Compose

```bash
# Build and run
docker-compose up --build

# Run in background
docker-compose up -d

# Stop
docker-compose down
```

## Application Features

- **Home page** (`/`) - Shows hostname with random color background
- **Color routes** (`/color/<color>`) - Set specific background colors
- **File reading** (`/read_file`) - Displays contents of a test file

## Environment Variables

- `APP_COLOR` - Set background color (red, green, blue, pink, yellow, white, purple)

## Accessing the Application

Once running, visit: http://localhost:8080

## Available Colors

- Red: http://localhost:8080/color/red
- Blue: http://localhost:8080/color/blue
- Green: http://localhost:8080/color/green
- Pink: http://localhost:8080/color/pink
- Yellow: http://localhost:8080/color/yellow
- White: http://localhost:8080/color/white
- Purple: http://localhost:8080/color/purple
