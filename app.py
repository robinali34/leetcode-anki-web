from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import json
from datetime import datetime
from leetcode_scraper import LeetCodeScraper
from card_generator import CardGenerator
from solution_generator import SolutionGenerator

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Initialize components
scraper = LeetCodeScraper()
card_gen = CardGenerator()
solution_gen = SolutionGenerator()

# Ensure data directory exists
os.makedirs('data', exist_ok=True)
os.makedirs('data/cards', exist_ok=True)

@app.route('/')
def index():
    """Main page showing all problems"""
    problems = scraper.get_all_problems()
    return render_template('index.html', problems=problems)

@app.route('/problem/<int:problem_id>')
def problem_detail(problem_id):
    """Show detailed view of a specific problem"""
    problem = scraper.get_problem_by_id(problem_id)
    if not problem:
        return redirect(url_for('index'))
    
    # Get existing cards for this problem
    cards = card_gen.get_cards_for_problem(problem_id)
    
    return render_template('problem_detail.html', problem=problem, cards=cards)

@app.route('/generate_cards/<int:problem_id>', methods=['POST'])
def generate_cards(problem_id):
    """Generate Anki cards for a specific problem"""
    problem = scraper.get_problem_by_id(problem_id)
    if not problem:
        return jsonify({'error': 'Problem not found'}), 404
    
    # Generate cards
    cards = card_gen.generate_cards(problem)
    
    # Save cards
    card_gen.save_cards(problem_id, cards)
    
    return jsonify({'success': True, 'cards_count': len(cards)})

@app.route('/study')
def study_mode():
    """Study mode interface"""
    all_cards = card_gen.get_all_cards()
    return render_template('study.html', cards=all_cards)

@app.route('/api/cards/<int:problem_id>')
def get_cards_api(problem_id):
    """API endpoint to get cards for a problem"""
    cards = card_gen.get_cards_for_problem(problem_id)
    return jsonify(cards)

@app.route('/api/update_card_progress', methods=['POST'])
def update_card_progress():
    """Update study progress for a card"""
    data = request.get_json()
    card_id = data.get('card_id')
    difficulty = data.get('difficulty')  # 1-5 scale
    
    if card_gen.update_card_progress(card_id, difficulty):
        return jsonify({'success': True})
    return jsonify({'error': 'Failed to update progress'}), 400

@app.route('/api/solution/<int:problem_id>')
def get_solution(problem_id):
    """Get solution for a specific problem"""
    solution = solution_gen.get_solution(problem_id)
    if solution:
        return jsonify({'success': True, 'solution': solution})
    return jsonify({'error': 'Solution not found'}), 404

@app.route('/search')
def search():
    """Search problems by title or tags"""
    query = request.args.get('q', '').lower()
    if not query:
        return redirect(url_for('index'))
    
    problems = scraper.search_problems(query)
    return render_template('search_results.html', problems=problems, query=query)

@app.route('/difficulty/<difficulty>')
def filter_by_difficulty(difficulty):
    """Filter problems by difficulty level"""
    problems = scraper.get_problems_by_difficulty(difficulty)
    return render_template('filtered_problems.html', problems=problems, difficulty=difficulty)

@app.route('/tags/<tag>')
def filter_by_tag(tag):
    """Filter problems by tag"""
    problems = scraper.get_problems_by_tag(tag)
    return render_template('filtered_problems.html', problems=problems, tag=tag)

@app.route('/all-tags')
def all_tags():
    """Show all available tags with problem counts"""
    all_problems = scraper.get_all_problems()
    tag_counts = {}
    
    for problem in all_problems:
        for tag in problem.get('tags', []):
            if tag in tag_counts:
                tag_counts[tag] += 1
            else:
                tag_counts[tag] = 1
    
    # Sort tags by count (descending) then alphabetically
    sorted_tags = sorted(tag_counts.items(), key=lambda x: (-x[1], x[0]))
    
    return render_template('all_tags.html', tags=sorted_tags)

@app.route('/stats')
def stats():
    """Show study statistics"""
    stats_data = card_gen.get_study_stats()
    return render_template('stats.html', stats=stats_data)

if __name__ == '__main__':
    # Create sample data if none exists
    if not os.path.exists('data/problems.json'):
        print("Initializing with sample LeetCode problems...")
        scraper.initialize_sample_data()
    
    print("🚀 Starting LeetCode Anki Card Generator...")
    print("📖 Open your browser to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000) 