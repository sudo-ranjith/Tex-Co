#!/bin/bash

# Simple frontend server for local development - Mac/Linux

echo "🌐 Starting Tex & Co Frontend..."
echo ""

# Check if node is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed!"
    echo "📥 Download from: https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js found"
echo ""

# Check if http-server is installed
if ! npm list -g http-server &> /dev/null; then
    echo "📦 Installing http-server..."
    npm install -g http-server
fi

echo ""
echo "🚀 Starting server on port 3000..."
echo ""
echo "📱 Open browser: http://localhost:3000"
echo "🛑 Press Ctrl+C to stop"
echo ""

# Start the server from frontend directory
cd "$(dirname "$0")/frontend"
npx http-server . -p 3000 -o index.html
