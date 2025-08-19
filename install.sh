#!/bin/bash

echo "🚀 Installing LeetCode Anki Card Generator..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.7"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python $python_version is installed, but Python $required_version+ is required."
    exit 1
fi

echo "✅ Python $python_version detected"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create data directories
echo "📁 Creating data directories..."
mkdir -p data/cards

# Initialize sample data
echo "🎯 Initializing sample data..."
python3 -c "from leetcode_scraper import LeetCodeScraper; s=LeetCodeScraper(); s.initialize_sample_data()"

echo ""
echo "🎉 Installation completed successfully!"
echo ""
echo "📖 To start the application:"
echo "   1. Activate virtual environment: source venv/bin/activate"
echo "   2. Run the app: python app.py"
echo "   3. Open browser: http://localhost:5000"
echo ""
echo "🔧 For future sessions, just run:"
echo "   source venv/bin/activate && python app.py"
echo ""
echo "Happy coding! 🚀💻" 