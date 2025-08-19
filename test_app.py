#!/usr/bin/env python3
"""
Simple test script for the LeetCode Anki application
"""

import os
import sys
import json
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all modules can be imported"""
    try:
        from leetcode_scraper import LeetCodeScraper
        from card_generator import CardGenerator
        print("✓ All modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_scraper():
    """Test the LeetCode scraper"""
    try:
        from leetcode_scraper import LeetCodeScraper
        scraper = LeetCodeScraper()
        
        # Test sample data initialization
        if not os.path.exists('data/problems.json'):
            scraper.initialize_sample_data()
            print("✓ Sample data initialized")
        
        problems = scraper.get_all_problems()
        print(f"✓ Found {len(problems)} problems")
        
        if problems:
            problem = problems[0]
            print(f"  - Sample problem: {problem['title']} ({problem['difficulty']})")
        
        return True
    except Exception as e:
        print(f"✗ Scraper test failed: {e}")
        return False

def test_card_generator():
    """Test the card generator"""
    try:
        from card_generator import CardGenerator
        card_gen = CardGenerator()
        
        # Test getting all cards
        all_cards = card_gen.get_all_cards()
        print(f"✓ Found {len(all_cards)} existing cards")
        
        # Test stats
        stats = card_gen.get_study_stats()
        print(f"✓ Study stats: {stats['total_cards']} total, {stats['completion_rate']}% completion")
        
        return True
    except Exception as e:
        print(f"✗ Card generator test failed: {e}")
        return False

def test_data_structure():
    """Test data directory structure"""
    try:
        # Check if data directories exist
        required_dirs = ['data', 'data/cards']
        for dir_path in required_dirs:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                print(f"✓ Created directory: {dir_path}")
            else:
                print(f"✓ Directory exists: {dir_path}")
        
        # Check if problems.json exists
        if os.path.exists('data/problems.json'):
            with open('data/problems.json', 'r') as f:
                problems = json.load(f)
            print(f"✓ Problems file contains {len(problems)} problems")
        else:
            print("⚠ Problems file not found (will be created on first run)")
        
        return True
    except Exception as e:
        print(f"✗ Data structure test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing LeetCode Anki Application")
    print("=" * 40)
    
    tests = [
        ("Data Structure", test_data_structure),
        ("Module Imports", test_imports),
        ("LeetCode Scraper", test_scraper),
        ("Card Generator", test_card_generator),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing: {test_name}")
        try:
            if test_func():
                passed += 1
                print(f"✓ {test_name} passed")
            else:
                print(f"✗ {test_name} failed")
        except Exception as e:
            print(f"✗ {test_name} failed with exception: {e}")
    
    print("\n" + "=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to run.")
        print("\nTo start the application, run:")
        print("  python app.py")
        print("\nThen open your browser to: http://localhost:5000")
    else:
        print("⚠ Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 