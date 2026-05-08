#!/bin/bash

echo "🔄 Restarting MemoryCare Application..."

# Kill any running app.py processes
echo "⏹️  Stopping old processes..."
pkill -f "python.*app.py" || echo "No running processes found"

# Wait a moment
sleep 2

# Navigate to remindp2 directory
cd "$(dirname "$0")"

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source ../venv/bin/activate 2>/dev/null || source ../.venv/bin/activate 2>/dev/null || echo "⚠️  Virtual environment not found, using system Python"

# Install/upgrade dependencies
echo "📦 Checking dependencies..."
pip install -q -r requirements.txt

# Start the application
echo "🚀 Starting application..."
echo "================================"
python app.py

# Made with Bob
