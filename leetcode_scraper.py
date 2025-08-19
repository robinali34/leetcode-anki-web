import requests
import json
import os
from bs4 import BeautifulSoup
from datetime import datetime
import time
import random

# Import the comprehensive sample problems
try:
    from sample_problems import get_comprehensive_problems
except ImportError:
    # Fallback if sample_problems.py is not available
    def get_comprehensive_problems():
        return {}

class LeetCodeScraper:
    def __init__(self):
        self.base_url = "https://leetcode.com"
        self.problems_file = "data/problems.json"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Load existing problems if available
        self.problems = self.load_problems()
    
    def load_problems(self):
        """Load problems from local file"""
        if os.path.exists(self.problems_file):
            try:
                with open(self.problems_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_problems(self):
        """Save problems to local file"""
        os.makedirs(os.path.dirname(self.problems_file), exist_ok=True)
        with open(self.problems_file, 'w') as f:
            json.dump(self.problems, f, indent=2)
    
    def fetch_problems_list(self):
        """Fetch problems list from LeetCode GraphQL API"""
        query = """
        query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
            problemsetQuestionList: questionList(
                categorySlug: $categorySlug
                limit: $limit
                skip: $skip
                filters: $filters
            ) {
                total: totalNum
                questions: data {
                    acRate
                    difficulty
                    freqBar
                    frontendQuestionId: questionId
                    isFavor
                    paidOnly: isPaidOnly
                    status
                    title
                    titleSlug
                    topicTags {
                        name
                        id
                        slug
                    }
                    hasSolution
                    hasVideoSolution
                }
            }
        }
        """
        
        variables = {
            "categorySlug": "",
            "limit": 1000,
            "skip": 0,
            "filters": {}
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/graphql",
                json={"query": query, "variables": variables},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('data', {}).get('problemsetQuestionList', {}).get('questions', [])
            else:
                print(f"Failed to fetch problems: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"Error fetching problems: {e}")
            return []
    
    def fetch_problem_detail(self, title_slug):
        """Fetch detailed information for a specific problem"""
        query = """
        query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                boundTitleSlug
                title
                titleSlug
                content
                mysqlSchemas
                exampleTestcases
                codeSnippets {
                    lang
                    langSlug
                    code
                }
                solution {
                    id
                    canSeeDetail
                    paidOnly
                    hasVideoSolution
                    paidOnlyVideo
                    topicTags {
                        id
                        name
                        slug
                    }
                    solutionTags {
                        id
                        name
                        slug
                    }
                    solutionLanguageTags {
                        id
                        name
                        slug
                    }
                }
                topicTags {
                    id
                    name
                    slug
                }
                companyTagStats
                codeSnippets {
                    lang
                    langSlug
                    code
                }
                stats
                hints
                status
                sampleTestCase
                metaData
                judgerAvailable
                judgeType
                mysqlSchemas
                enableRunCode
                enableTestMode
                enableDebugger
                envInfo
                libraryUrl
                adminUrl
                challengeQuestion {
                    id
                    date
                    incompleteChallengeCount
                    streakCount
                    type
                }
                note
            }
        }
        """
        
        variables = {"titleSlug": title_slug}
        
        try:
            response = self.session.post(
                f"{self.base_url}/graphql",
                json={"query": query, "variables": variables},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('data', {}).get('question', {})
            else:
                print(f"Failed to fetch problem detail: {response.status_code}")
                return {}
                
        except Exception as e:
            print(f"Error fetching problem detail: {e}")
            return {}
    
    def update_problems(self):
        """Update problems list from LeetCode"""
        print("Fetching problems from LeetCode...")
        problems_list = self.fetch_problems_list()
        
        for problem in problems_list:
            problem_id = int(problem['frontendQuestionId'])
            
            if str(problem_id) not in self.problems:
                # Fetch detailed information
                detail = self.fetch_problem_detail(problem['titleSlug'])
                
                self.problems[str(problem_id)] = {
                    'id': problem_id,
                    'title': problem['title'],
                    'title_slug': problem['titleSlug'],
                    'difficulty': problem['difficulty'],
                    'status': problem['status'],
                    'ac_rate': problem['acRate'],
                    'paid_only': problem['paidOnly'],
                    'tags': [tag['name'] for tag in problem['topicTags']],
                    'content': detail.get('content', ''),
                    'example_testcases': detail.get('exampleTestcases', ''),
                    'code_snippets': detail.get('codeSnippets', []),
                    'last_updated': datetime.now().isoformat()
                }
                
                # Be respectful with rate limiting
                time.sleep(random.uniform(0.5, 1.5))
        
        self.save_problems()
        print(f"Updated {len(self.problems)} problems")

    def update_dynamic_programming_problems(self, max_count: int = 10000):
        """Fetch all problems, filter by Dynamic Programming tag, fetch details, and save.
        Args:
            max_count: upper bound to fetch from problem list (default high enough)
        """
        print("Fetching all problems to filter Dynamic Programming ones...")
        # Get a big list and filter locally to avoid GraphQL filter uncertainties
        all_list = []
        try:
            # questionList limit is typically capped ~1000; request a big limit once
            query = """
            query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
                problemsetQuestionList: questionList(
                    categorySlug: $categorySlug
                    limit: $limit
                    skip: $skip
                    filters: $filters
                ) {
                    total: totalNum
                    questions: data {
                        acRate
                        difficulty
                        frontendQuestionId: questionId
                        paidOnly: isPaidOnly
                        status
                        title
                        titleSlug
                        topicTags { name id slug }
                    }
                }
            }
            """
            variables = {
                "categorySlug": "",
                "limit": max_count,
                "skip": 0,
                "filters": {}
            }
            resp = self.session.post(f"{self.base_url}/graphql", json={"query": query, "variables": variables}, timeout=30)
            if resp.status_code == 200:
                data = resp.json().get('data', {}).get('problemsetQuestionList', {})
                all_list = data.get('questions', [])
                print(f"Fetched {len(all_list)} problems from LeetCode list")
            else:
                print(f"Failed to fetch problems list: {resp.status_code}")
        except Exception as e:
            print(f"Error listing problems: {e}")
            all_list = []

        # Filter for Dynamic Programming by tag slug or name
        dp_candidates = []
        for q in all_list:
            if any((t.get('slug') == 'dynamic-programming' or t.get('name', '').lower() == 'dynamic programming') for t in q.get('topicTags', [])):
                dp_candidates.append(q)
        print(f"Identified {len(dp_candidates)} Dynamic Programming problems from list")

        added = 0
        for q in dp_candidates:
            try:
                pid = int(q.get('frontendQuestionId'))
            except Exception:
                continue
            key = str(pid)
            if key in self.problems:
                # already have it
                continue
            # Fetch detail for rich content
            detail = self.fetch_problem_detail(q.get('titleSlug')) or {}
            self.problems[key] = {
                'id': pid,
                'title': q.get('title', ''),
                'title_slug': q.get('titleSlug', ''),
                'difficulty': q.get('difficulty', ''),
                'status': q.get('status', 'NOT_STARTED') or 'NOT_STARTED',
                'ac_rate': q.get('acRate', 0.0),
                'paid_only': bool(q.get('paidOnly')),
                'tags': [t.get('name') for t in (q.get('topicTags') or [])],
                'content': detail.get('content', ''),
                'example_testcases': detail.get('exampleTestcases', ''),
                'code_snippets': detail.get('codeSnippets', []),
                'last_updated': datetime.now().isoformat(),
            }
            added += 1
            # Gentle rate-limit
            time.sleep(random.uniform(0.3, 0.9))

        self.save_problems()
        print(f"Added {added} new Dynamic Programming problems. Total now: {len(self.problems)}")
    
    def get_all_problems(self):
        """Get all problems"""
        return list(self.problems.values())
    
    def get_problem_by_id(self, problem_id):
        """Get problem by ID"""
        return self.problems.get(str(problem_id))
    
    def search_problems(self, query):
        """Search problems by title or tags"""
        query = query.lower()
        results = []
        
        for problem in self.problems.values():
            if (query in problem['title'].lower() or 
                any(query in tag.lower() for tag in problem['tags'])):
                results.append(problem)
        
        return results
    
    def get_problems_by_difficulty(self, difficulty):
        """Get problems by difficulty level"""
        difficulty = difficulty.upper()
        return [p for p in self.problems.values() if p['difficulty'] == difficulty]
    
    def get_problems_by_tag(self, tag):
        """Get problems by tag"""
        tag = tag.lower()
        return [p for p in self.problems.values() if tag in [t.lower() for t in p['tags']]]
    
    def initialize_sample_data(self):
        """Initialize with first 200 LeetCode problems"""
        print("Loading comprehensive sample problems...")
        comprehensive_problems = get_comprehensive_problems()
        
        if comprehensive_problems:
            self.problems = comprehensive_problems
            self.save_problems()
            print(f"Initialized with {len(self.problems)} comprehensive LeetCode problems (1-200)")
        else:
            # Fallback to basic sample problems
            sample_problems = {
                "1": {
                    "id": 1,
                    "title": "Two Sum",
                    "title_slug": "two-sum",
                    "difficulty": "EASY",
                    "status": "NOT_STARTED",
                    "ac_rate": 49.2,
                    "paid_only": False,
                    "tags": ["Array", "Hash Table"],
                    "content": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
                    "example_testcases": "[2,7,11,15]\n9",
                    "code_snippets": [],
                    "last_updated": datetime.now().isoformat()
                },
                "2": {
                    "id": 2,
                    "title": "Add Two Numbers",
                    "title_slug": "add-two-numbers",
                    "difficulty": "MEDIUM",
                    "status": "NOT_STARTED",
                    "ac_rate": 38.1,
                    "paid_only": False,
                    "tags": ["Linked List", "Math", "Recursion"],
                    "content": "You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.",
                    "example_testcases": "[2,4,3]\n[5,6,4]",
                    "code_snippets": [],
                    "last_updated": datetime.now().isoformat()
                },
                "3": {
                    "id": 3,
                    "title": "Longest Substring Without Repeating Characters",
                    "title_slug": "longest-substring-without-repeating-characters",
                    "difficulty": "MEDIUM",
                    "status": "NOT_STARTED",
                    "ac_rate": 33.8,
                    "paid_only": False,
                    "tags": ["Hash Table", "String", "Sliding Window"],
                    "content": "Given a string s, find the length of the longest substring without repeating characters.",
                    "example_testcases": "\"abcabcbb\"",
                    "code_snippets": [],
                    "last_updated": datetime.now().isoformat()
                }
            }
            
            self.problems = sample_problems
            self.save_problems()
            print("Initialized with basic sample problems") 