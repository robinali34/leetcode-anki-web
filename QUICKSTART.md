# 🚀 Quick Start Guide

Get up and running with LeetCode Anki Card Generator in under 5 minutes!

## ⚡ Super Quick Start

### 1. Install & Run
```bash
# On macOS/Linux
./install.sh

# On Windows
install.bat

# Or manually
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate.bat on Windows
pip install -r requirements.txt
python app.py
```

### 2. Open Browser
Navigate to: **http://localhost:5000**

### 3. Start Learning! 🎯

## 🎨 What You'll See

### Home Page Features
- **200+ LeetCode Problems** with colorful tag buttons
- **Rainbow Tag System**: 
  - 🔴 Red = Very popular topics (>150 problems)
  - 🌈 Rainbow colors = Other topics (≤150 problems)
- **Problem Cards** with difficulty levels and descriptions

### Navigation
- **Click any tag** → See all problems in that category
- **Click "View Details"** → Full problem with solutions
- **Click "Generate Cards"** → Create 7 Anki study cards

## 🃏 Generate Your First Cards

1. **Browse Problems**: Scroll through the home page
2. **Pick a Problem**: Click "View Details" on any problem
3. **Generate Cards**: Click "Generate Anki Cards"
4. **Study**: Review the generated flashcards

## 🌈 Understanding the Tag Colors

### Color Meanings
- **🔴 Red (Large)**: Massive topic areas (Array, String, etc.)
- **🟡 Yellow**: Popular topics (Two Pointers, Sliding Window)
- **🟢 Green**: Common topics (Tree, Graph)
- **🔵 Cyan**: Medium topics (Dynamic Programming, Backtracking)
- **🔵 Blue**: Growing topics (Heap, Priority Queue)
- **⚫ Gray**: Specialized topics (Trie, Segment Tree)
- **⚫ Black**: Niche topics (Union Find, Binary Indexed Tree)

### Button Sizes
- **Small**: ≤25 problems (focused topics)
- **Medium**: 26-75 problems (established topics)
- **Large**: 76+ problems (comprehensive topics)

## 🔍 Find Problems by Topic

### Popular Categories
- **Arrays & Strings**: Click red "Array" tag
- **Dynamic Programming**: Click cyan "Dynamic Programming" tag
- **Trees & Graphs**: Click green "Tree" or "Graph" tags
- **Two Pointers**: Click yellow "Two Pointers" tag

### Search & Filter
- **Tag Filtering**: Click any colored tag button
- **All Tags**: Click "View All Tags" for complete directory
- **Difficulty**: Problems show Easy/Medium/Hard badges

## 💻 Study with Solutions

### What You Get
1. **Problem Statement** - Full description
2. **Test Cases** - Example inputs/outputs
3. **Algorithm Approach** - Step-by-step strategy
4. **Complexity Analysis** - Time & space complexity
5. **Key Concepts** - Important topics to know
6. **Pseudocode** - Algorithm in plain English
7. **Python Code** - Complete, runnable solution

### Study Tips
- **Start with Easy problems** to build confidence
- **Generate cards** for problems you want to master
- **Review solutions** before attempting similar problems
- **Use tag colors** to identify your weak areas

## 🚨 Common Issues & Solutions

### Port Already in Use
```bash
# Kill existing process
lsof -ti:5000 | xargs kill -9

# Or use different port
export FLASK_RUN_PORT=5001
python app.py
```

### Import Errors
```bash
# Ensure virtual environment is active
source venv/bin/activate  # or venv\Scripts\activate.bat

# Reinstall dependencies
pip install -r requirements.txt
```

### No Problems Loading
```bash
# Initialize sample data
python -c "from leetcode_scraper import LeetCodeScraper; s=LeetCodeScraper(); s.initialize_sample_data()"
```

## 🎯 Next Steps

### Beginner Path
1. **Start with Easy problems** (green badges)
2. **Focus on Array/String tags** (red buttons)
3. **Generate cards** for each solved problem
4. **Review solutions** to understand patterns

### Intermediate Path
1. **Explore Medium problems** (yellow badges)
2. **Study Dynamic Programming** (cyan tags)
3. **Practice Two Pointers** (yellow tags)
4. **Master Tree/Graph algorithms** (green tags)

### Advanced Path
1. **Tackle Hard problems** (red badges)
2. **Deep dive into DP** (red "Dynamic Programming")
3. **Master advanced data structures** (gray/black tags)
4. **Contribute solutions** to help others

## 🔗 Useful URLs

- **Home**: http://localhost:5000
- **All Tags**: http://localhost:5000/all-tags
- **Specific Tag**: http://localhost:5000/tags/Array
- **Problem Details**: http://localhost:5000/problem/1

## 💡 Pro Tips

- **Bookmark your favorite problems** for quick access
- **Use tag colors** to plan your study schedule
- **Generate cards** for problems you struggle with
- **Review solutions** even for problems you solved
- **Focus on one topic** at a time using tag filtering

---

**Ready to start? Open http://localhost:5000 and begin your LeetCode journey! 🚀💻** 