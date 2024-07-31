#!/bin/bash

# Set up virtual environment for the backend
echo "Setting up virtual environment for the backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start the FastAPI backend with Gunicorn
echo "Starting the FastAPI backend with Gunicorn..."
gunicorn -c gunicorn_config.py -k uvicorn.workers.UvicornWorker main:app &
BACKEND_PID=$!
cd ..

# Start the frontend using a local server (e.g., using serve or http-server)
echo "Setting up frontend..."
cd frontend
npm install
npx webpack serve &
FRONTEND_PID=$!

# Function to stop the backend and frontend when the script is terminated
cleanup() {
    echo "Stopping the frontend..."
    kill $FRONTEND_PID
    echo "Stopping the backend..."
    kill $BACKEND_PID
    exit 0
}

# Trap SIGINT and SIGTERM to clean up
trap cleanup SIGINT SIGTERM

# Wait for both processes to finish
wait $BACKEND_PID
wait $FRONTEND_PID
