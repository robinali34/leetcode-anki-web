@echo off
echo 🚀 Installing LeetCode Anki Card Generator...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.7+ first.
    pause
    exit /b 1
)

echo ✅ Python detected

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️ Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo 📚 Installing dependencies...
pip install -r requirements.txt

REM Create data directories
echo 📁 Creating data directories...
if not exist "data" mkdir data
if not exist "data\cards" mkdir data\cards

REM Initialize sample data
echo 🎯 Initializing sample data...
python -c "from leetcode_scraper import LeetCodeScraper; s=LeetCodeScraper(); s.initialize_sample_data()"

echo.
echo 🎉 Installation completed successfully!
echo.
echo 📖 To start the application:
echo    1. Activate virtual environment: venv\Scripts\activate.bat
echo    2. Run the app: python app.py
echo    3. Open browser: http://localhost:5000
echo.
echo 🔧 For future sessions, just run:
echo    venv\Scripts\activate.bat && python app.py
echo.
echo Happy coding! 🚀💻
pause 