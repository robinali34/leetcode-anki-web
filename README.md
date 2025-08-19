# 🎯 LeetCode Anki Card Generator

A web application that generates Anki cards from LeetCode problems to help you study algorithms and data structures effectively.

## 🌐 GitHub Pages Deployment

This project includes a static website version that can be hosted on GitHub Pages for easy access without running the Python application locally.

### Quick Deploy

1. **Automatic Deployment**: The `gh-pages` branch is automatically deployed via GitHub Actions when you push changes to it.

2. **Manual Update**: Use the provided script to update the static website:
   ```bash
   ./update-gh-pages.sh
   ```

3. **Access Your Website**: Once deployed, your website will be available at:
   ```
   https://robinali34.github.io/leetcode-anki-web/
   ```

### What's Included in Static Version

The static website includes:
- ✅ Main landing page (`index.html`)
- ✅ Documentation files
- ✅ Responsive design with Bootstrap
- ✅ All necessary assets and styling

### Branch Structure

- **`main`**: Full Python application with Flask backend
- **`gh-pages`**: Static website files for GitHub Pages hosting

## ✨ Features

- **📚 200+ LeetCode Problems**: Comprehensive collection of algorithm problems
- **🎨 Rainbow Tag System**: Color-coded problem categories with 7-rainbow colors
- **💻 Python Solutions**: Complete pseudocode and Python implementations
- **🃏 Anki Cards**: Generate 7 different types of study cards per problem
- **🔍 Smart Filtering**: Browse problems by tags, difficulty, or search
- **📊 Study Progress**: Track your learning progress across all problems
- **🌐 Web Interface**: Modern, responsive web application

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd lc-anki
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to: http://localhost:5000

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
Flask==2.3.3
requests==2.31.0
beautifulsoup4==4.12.2
lxml==4.9.3
```

## 🏗️ Project Structure

```
lc-anki/
├── app.py                 # Main Flask application
├── leetcode_scraper.py   # LeetCode data fetching
├── solution_generator.py # Problem solutions (pseudocode + Python)
├── card_generator.py     # Anki card generation
├── templates/            # HTML templates
│   ├── index.html       # Home page with tag filtering
│   ├── problem_detail.html # Problem view with solutions
│   ├── filtered_problems.html # Tag-filtered problem lists
│   └── all_tags.html    # Complete tag directory
├── static/              # CSS, JS, and static assets
├── data/               # Generated data storage
│   ├── problems.json   # Problem database
│   └── cards/          # Generated Anki cards
└── README.md           # This file
```

## 🎮 Usage

### 1. Browse Problems
- **Home Page**: View all problems with colorful tag filtering
- **Tag Colors**: 
  - 🔴 Red: >150 problems (most popular)
  - 🌈 Rainbow: ≤150 problems (7-color scheme)
- **Click Tags**: Navigate to filtered problem lists

### 2. View Problem Details
- Click "View Details" on any problem card
- See complete problem description
- Access pseudocode and Python solutions
- Generate Anki study cards

### 3. Generate Anki Cards
- Click "Generate Anki Cards" on any problem
- Creates 7 different types of study cards:
  - Problem Statement
  - Test Cases
  - Algorithm Approach
  - Time/Space Complexity
  - Key Concepts
  - Pseudocode Solution
  - Python Code Solution

### 4. Study Mode
- Use generated cards for spaced repetition learning
- Track your progress with difficulty ratings
- Review solutions and implementations

## 🎨 Tag System

### Color Scheme
- **🔴 Red (Large)**: Tags with >150 problems
- **🟡 Yellow**: Tags with count % 7 = 2
- **🟢 Green**: Tags with count % 7 = 3
- **🔵 Cyan**: Tags with count % 7 = 4
- **🔵 Blue**: Tags with count % 7 = 5
- **⚫ Gray**: Tags with count % 7 = 6
- **⚫ Black**: Tags with count % 7 = 0

### Button Sizes
- **Small**: ≤25 problems
- **Medium**: 26-75 problems
- **Large**: 76+ problems

## 🔧 Configuration

### Environment Variables
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
```