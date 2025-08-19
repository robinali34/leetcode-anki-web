import json
import os
import uuid
from datetime import datetime, timedelta
import re

# Import the solution generator
try:
    from solution_generator import SolutionGenerator
except ImportError:
    # Fallback if solution_generator.py is not available
    class SolutionGenerator:
        def get_solution(self, problem_id):
            return {"pseudocode": "Solution not available", "python_code": "Solution not available"}

class CardGenerator:
    def __init__(self):
        self.cards_dir = "data/cards"
        self.progress_file = "data/study_progress.json"
        
        # Initialize solution generator
        self.solution_gen = SolutionGenerator()
        
        # Ensure directories exist
        os.makedirs(self.cards_dir, exist_ok=True)
        
        # Load study progress
        self.progress = self.load_progress()
    
    def load_progress(self):
        """Load study progress from file"""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_progress(self):
        """Save study progress to file"""
        os.makedirs(os.path.dirname(self.progress_file), exist_ok=True)
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def generate_cards(self, problem):
        """Generate Anki-style cards for a LeetCode problem"""
        cards = []
        
        # Card 1: Problem Statement
        cards.append({
            'id': str(uuid.uuid4()),
            'type': 'problem_statement',
            'front': f"Problem {problem['id']}: {problem['title']}",
            'back': self._clean_html(problem['content']),
            'tags': ['problem', 'statement'],
            'difficulty': problem['difficulty'],
            'created_at': datetime.now().isoformat(),
            'last_reviewed': None,
            'review_count': 0,
            'ease_factor': 2.5,
            'interval': 0
        })
        
        # Card 2: Example Test Cases
        if problem.get('example_testcases'):
            cards.append({
                'id': str(uuid.uuid4()),
                'type': 'test_cases',
                'front': f"Example test cases for {problem['title']}",
                'back': f"```\n{problem['example_testcases']}\n```",
                'tags': ['test_cases', 'examples'],
                'difficulty': problem['difficulty'],
                'created_at': datetime.now().isoformat(),
                'last_reviewed': None,
                'review_count': 0,
                'ease_factor': 2.5,
                'interval': 0
            })
        
        # Card 3: Algorithm Approach
        cards.append({
            'id': str(uuid.uuid4()),
            'type': 'algorithm',
            'front': f"What's the algorithm approach for {problem['title']}?",
            'back': self._generate_algorithm_hint(problem),
            'tags': ['algorithm', 'approach'],
            'difficulty': problem['difficulty'],
            'created_at': datetime.now().isoformat(),
            'last_reviewed': None,
            'review_count': 0,
            'ease_factor': 2.5,
            'interval': 0
        })
        
        # Card 4: Time/Space Complexity
        cards.append({
            'id': str(uuid.uuid4()),
            'type': 'complexity',
            'front': f"What's the time and space complexity for {problem['title']}?",
            'back': self._generate_complexity_hint(problem),
            'tags': ['complexity', 'analysis'],
            'difficulty': problem['difficulty'],
            'created_at': datetime.now().isoformat(),
            'last_reviewed': None,
            'review_count': 0,
            'ease_factor': 2.5,
            'interval': 0
        })
        
        # Card 5: Key Concepts
        if problem.get('tags'):
            cards.append({
                'id': str(uuid.uuid4()),
                'type': 'concepts',
                'front': f"What are the key concepts for {problem['title']}?",
                'back': f"Key concepts: {', '.join(problem['tags'])}",
                'tags': ['concepts', 'tags'],
                'difficulty': problem['difficulty'],
                'created_at': datetime.now().isoformat(),
                'last_reviewed': None,
                'review_count': 0,
                'ease_factor': 2.5,
                'interval': 0
            })
        
        # Card 6: Pseudocode Solution
        solution = self.solution_gen.get_solution(problem['id'])
        cards.append({
            'id': str(uuid.uuid4()),
            'type': 'pseudocode',
            'front': f"Show the pseudocode solution for {problem['title']}",
            'back': solution['pseudocode'],
            'tags': ['solution', 'pseudocode', 'algorithm'],
            'difficulty': problem['difficulty'],
            'created_at': datetime.now().isoformat(),
            'last_reviewed': None,
            'review_count': 0,
            'ease_factor': 2.5,
            'interval': 0
        })
        
        # Card 7: Python Code Solution
        cards.append({
            'id': str(uuid.uuid4()),
            'type': 'python_code',
            'front': f"Show the Python code solution for {problem['title']}",
            'back': f"```python\n{solution['python_code']}\n```",
            'tags': ['solution', 'python', 'implementation'],
            'difficulty': problem['difficulty'],
            'created_at': datetime.now().isoformat(),
            'last_reviewed': None,
            'review_count': 0,
            'ease_factor': 2.5,
            'interval': 0
        })
        
        return cards
    
    def _clean_html(self, html_content):
        """Clean HTML content for display"""
        if not html_content:
            return "No content available"
        
        # Remove HTML tags but preserve line breaks
        content = re.sub(r'<[^>]+>', '', html_content)
        content = re.sub(r'&nbsp;', ' ', content)
        content = re.sub(r'&lt;', '<', content)
        content = re.sub(r'&gt;', '>', content)
        content = re.sub(r'&amp;', '&', content)
        
        return content.strip()
    
    def _generate_algorithm_hint(self, problem):
        """Generate algorithm hints based on problem tags"""
        tags = [tag.lower() for tag in problem.get('tags', [])]
        
        hints = []
        if 'array' in tags:
            hints.append("Consider array traversal and manipulation")
        if 'hash table' in tags or 'hash' in tags:
            hints.append("Use hash table for O(1) lookups")
        if 'two pointers' in tags:
            hints.append("Consider using two pointers technique")
        if 'sliding window' in tags:
            hints.append("Use sliding window approach")
        if 'dynamic programming' in tags or 'dp' in tags:
            hints.append("Consider dynamic programming solution")
        if 'binary search' in tags:
            hints.append("Use binary search for optimization")
        if 'tree' in tags or 'binary tree' in tags:
            hints.append("Consider tree traversal (DFS/BFS)")
        if 'graph' in tags:
            hints.append("Use graph algorithms (DFS/BFS)")
        
        if not hints:
            hints.append("Analyze the problem step by step")
        
        return "\n".join(hints)
    
    def _generate_complexity_hint(self, problem):
        """Generate complexity hints based on problem type"""
        tags = [tag.lower() for tag in problem.get('tags', [])]
        
        if 'array' in tags and 'hash table' in tags:
            return "Time: O(n), Space: O(n) - typically one pass with hash table"
        elif 'two pointers' in tags:
            return "Time: O(n), Space: O(1) - two pointers traverse array once"
        elif 'sliding window' in tags:
            return "Time: O(n), Space: O(1) - maintain window while traversing"
        elif 'binary search' in tags:
            return "Time: O(log n), Space: O(1) - binary search on sorted data"
        elif 'dynamic programming' in tags:
            return "Time: O(n²) or O(n³), Space: O(n) - depends on state space"
        else:
            return "Analyze the algorithm to determine complexity"
    
    def save_cards(self, problem_id, cards):
        """Save cards for a specific problem"""
        cards_file = os.path.join(self.cards_dir, f"{problem_id}.json")
        
        with open(cards_file, 'w') as f:
            json.dump(cards, f, indent=2)
    
    def get_cards_for_problem(self, problem_id):
        """Get cards for a specific problem"""
        cards_file = os.path.join(self.cards_dir, f"{problem_id}.json")
        
        if os.path.exists(cards_file):
            try:
                with open(cards_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def get_all_cards(self):
        """Get all cards from all problems"""
        all_cards = []
        
        for filename in os.listdir(self.cards_dir):
            if filename.endswith('.json'):
                try:
                    with open(os.path.join(self.cards_dir, filename), 'r') as f:
                        cards = json.load(f)
                        all_cards.extend(cards)
                except:
                    continue
        
        return all_cards
    
    def get_due_cards(self):
        """Get cards that are due for review"""
        now = datetime.now()
        due_cards = []
        
        for card in self.get_all_cards():
            if self._is_card_due(card, now):
                due_cards.append(card)
        
        return due_cards
    
    def _is_card_due(self, card, now):
        """Check if a card is due for review"""
        if card['last_reviewed'] is None:
            return True
        
        last_reviewed = datetime.fromisoformat(card['last_reviewed'])
        interval_days = card['interval']
        
        return (now - last_reviewed).days >= interval_days
    
    def update_card_progress(self, card_id, difficulty):
        """Update study progress for a card using spaced repetition"""
        # Find the card
        all_cards = self.get_all_cards()
        card = None
        
        for c in all_cards:
            if c['id'] == card_id:
                card = c
                break
        
        if not card:
            return False
        
        # Update card progress
        now = datetime.now()
        card['last_reviewed'] = now.isoformat()
        card['review_count'] += 1
        
        # Calculate new interval using SuperMemo 2 algorithm
        if difficulty >= 4:  # Easy
            if card['interval'] == 0:
                card['interval'] = 1
            elif card['interval'] == 1:
                card['interval'] = 6
            else:
                card['interval'] = int(card['interval'] * card['ease_factor'])
            
            card['ease_factor'] = min(2.5, card['ease_factor'] + 0.1)
            
        elif difficulty == 3:  # Medium
            if card['interval'] > 0:
                card['interval'] = max(1, int(card['interval'] * 0.5))
            card['ease_factor'] = max(1.3, card['ease_factor'] - 0.15)
            
        else:  # Hard
            card['interval'] = 1
            card['ease_factor'] = max(1.3, card['ease_factor'] - 0.2)
        
        # Save updated card
        self._save_updated_card(card)
        
        # Update progress tracking
        self.progress[card_id] = {
            'last_reviewed': now.isoformat(),
            'difficulty': difficulty,
            'interval': card['interval'],
            'ease_factor': card['ease_factor']
        }
        self.save_progress()
        
        return True
    
    def _save_updated_card(self, updated_card):
        """Save an updated card back to its file"""
        # Find which problem this card belongs to
        all_cards = self.get_all_cards()
        
        for filename in os.listdir(self.cards_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.cards_dir, filename)
                try:
                    with open(filepath, 'r') as f:
                        cards = json.load(f)
                    
                    # Update the card if found
                    for i, card in enumerate(cards):
                        if card['id'] == updated_card['id']:
                            cards[i] = updated_card
                            with open(filepath, 'w') as f:
                                json.dump(cards, f, indent=2)
                            return
                except:
                    continue
    
    def get_study_stats(self):
        """Get study statistics"""
        all_cards = self.get_all_cards()
        total_cards = len(all_cards)
        reviewed_cards = len([c for c in all_cards if c['last_reviewed'] is not None])
        due_cards = len(self.get_due_cards())
        
        # Calculate average ease factor
        ease_factors = [c['ease_factor'] for c in all_cards if c['ease_factor'] > 0]
        avg_ease_factor = sum(ease_factors) / len(ease_factors) if ease_factors else 0
        
        # Calculate total review count
        total_reviews = sum(c['review_count'] for c in all_cards)
        
        return {
            'total_cards': total_cards,
            'reviewed_cards': reviewed_cards,
            'due_cards': due_cards,
            'avg_ease_factor': round(avg_ease_factor, 2),
            'total_reviews': total_reviews,
            'completion_rate': round((reviewed_cards / total_cards * 100) if total_cards > 0 else 0, 1)
        } 