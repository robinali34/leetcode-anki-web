#!/usr/bin/env python3
"""
Sample LeetCode problems data for the first 200 problems
"""

SAMPLE_PROBLEMS = {
    "1": {
        "id": 1,
        "title": "Two Sum",
        "title_slug": "two-sum",
        "difficulty": "EASY",
        "status": "NOT_STARTED",
        "ac_rate": 49.2,
        "paid_only": False,
        "tags": ["Array", "Hash Table"],
        "content": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.",
        "example_testcases": "[2,7,11,15]\n9",
        "code_snippets": [],
        "last_updated": "2025-08-18T22:46:41.938863"
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
        "content": "You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.",
        "example_testcases": "[2,4,3]\n[5,6,4]",
        "code_snippets": [],
        "last_updated": "2025-08-18T22:46:41.938863"
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
        "last_updated": "2025-08-18T22:46:41.938863"
    },
    "4": {
        "id": 4,
        "title": "Median of Two Sorted Arrays",
        "title_slug": "median-of-two-sorted-arrays",
        "difficulty": "HARD",
        "status": "NOT_STARTED",
        "ac_rate": 35.2,
        "paid_only": False,
        "tags": ["Array", "Binary Search", "Divide and Conquer"],
        "content": "Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).",
        "example_testcases": "[1,3]\n[2]",
        "code_snippets": [],
        "last_updated": "2025-08-18T22:46:41.938863"
    },
    "5": {
        "id": 5,
        "title": "Longest Palindromic Substring",
        "title_slug": "longest-palindromic-substring",
        "difficulty": "MEDIUM",
        "status": "NOT_STARTED",
        "ac_rate": 32.1,
        "paid_only": False,
        "tags": ["String", "Dynamic Programming"],
        "content": "Given a string s, return the longest palindromic substring in s.",
        "example_testcases": "\"babad\"",
        "code_snippets": [],
        "last_updated": "2025-08-18T22:46:41.938863"
    },
    "6": {
        "id": 6,
        "title": "Zigzag Conversion",
        "title_slug": "zigzag-conversion",
        "difficulty": "MEDIUM",
        "status": "NOT_STARTED",
        "ac_rate": 42.3,
        "paid_only": False,
        "tags": ["String"],
        "content": "The string \"PAYPALISHIRING\" is written in a zigzag pattern on a given number of rows. Write the code that will take a string and make this conversion given a number of rows.",
        "example_testcases": "\"PAYPALISHIRING\"\n3",
        "code_snippets": [],
        "last_updated": "2025-08-18T22:46:41.938863"
    },
    "7": {
        "id": 7,
        "title": "Reverse Integer",
        "title_slug": "reverse-integer",
        "difficulty": "MEDIUM",
        "status": "NOT_STARTED",
        "ac_rate": 27.8,
        "paid_only": False,
        "tags": ["Math"],
        "content": "Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.",
        "example_testcases": "123",
        "code_snippets": [],
        "last_updated": "2025-08-18T22:46:41.938863"
    },
    "8": {
        "id": 8,
        "title": "String to Integer (atoi)",
        "title_slug": "string-to-integer-atoi",
        "difficulty": "MEDIUM",
        "status": "NOT_STARTED",
        "ac_rate": 16.9,
        "paid_only": False,
        "tags": ["String"],
        "content": "Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).",
        "example_testcases": "\"42\"",
        "code_snippets": [],
        "last_updated": "2025-08-18T22:46:41.938863"
    },
    "9": {
        "id": 9,
        "title": "Palindrome Number",
        "title_slug": "palindrome-number",
        "difficulty": "EASY",
        "status": "NOT_STARTED",
        "ac_rate": 52.4,
        "paid_only": False,
        "tags": ["Math"],
        "content": "Given an integer x, return true if x is a palindrome, and false otherwise.",
        "example_testcases": "121",
        "code_snippets": [],
        "last_updated": "2025-08-18T22:46:41.938863"
    },
    "10": {
        "id": 10,
        "title": "Regular Expression Matching",
        "title_slug": "regular-expression-matching",
        "difficulty": "HARD",
        "status": "NOT_STARTED",
        "ac_rate": 28.7,
        "paid_only": False,
        "tags": ["String", "Dynamic Programming", "Recursion"],
        "content": "Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where '.' matches any single character and '*' matches zero or more of the preceding element.",
        "example_testcases": "\"aa\"\n\"a\"",
        "code_snippets": [],
        "last_updated": "2025-08-18T22:46:41.938863"
    }
}

# Add more problems with realistic names
ADDITIONAL_PROBLEMS = {
    "11": {"title": "Container With Most Water", "difficulty": "MEDIUM", "tags": ["Array", "Two Pointers", "Greedy"]},
    "12": {"title": "Integer to Roman", "difficulty": "MEDIUM", "tags": ["Hash Table", "Math", "String"]},
    "13": {"title": "Roman to Integer", "difficulty": "EASY", "tags": ["Hash Table", "Math", "String"]},
    "14": {"title": "Longest Common Prefix", "difficulty": "EASY", "tags": ["String"]},
    "15": {"title": "3Sum", "difficulty": "MEDIUM", "tags": ["Array", "Two Pointers", "Sorting"]},
    "16": {"title": "3Sum Closest", "difficulty": "MEDIUM", "tags": ["Array", "Two Pointers", "Sorting"]},
    "17": {"title": "Letter Combinations of a Phone Number", "difficulty": "MEDIUM", "tags": ["Hash Table", "String", "Backtracking"]},
    "18": {"title": "4Sum", "difficulty": "MEDIUM", "tags": ["Array", "Two Pointers", "Sorting"]},
    "19": {"title": "Remove Nth Node From End of List", "difficulty": "MEDIUM", "tags": ["Linked List", "Two Pointers"]},
    "20": {"title": "Valid Parentheses", "difficulty": "EASY", "tags": ["String", "Stack"]},
    "21": {"title": "Merge Two Sorted Lists", "difficulty": "EASY", "tags": ["Linked List", "Recursion"]},
    "22": {"title": "Generate Parentheses", "difficulty": "MEDIUM", "tags": ["String", "Dynamic Programming", "Backtracking"]},
    "23": {"title": "Merge k Sorted Lists", "difficulty": "HARD", "tags": ["Linked List", "Divide and Conquer", "Heap"]},
    "24": {"title": "Swap Nodes in Pairs", "difficulty": "MEDIUM", "tags": ["Linked List", "Recursion"]},
    "25": {"title": "Reverse Nodes in k-Group", "difficulty": "HARD", "tags": ["Linked List", "Recursion"]},
    "26": {"title": "Remove Duplicates from Sorted Array", "difficulty": "EASY", "tags": ["Array", "Two Pointers"]},
    "27": {"title": "Remove Element", "difficulty": "EASY", "tags": ["Array", "Two Pointers"]},
    "28": {"title": "Find the Index of the First Occurrence in a String", "difficulty": "EASY", "tags": ["String", "Two Pointers", "String Matching"]},
    "29": {"title": "Divide Two Integers", "difficulty": "MEDIUM", "tags": ["Math", "Bit Manipulation"]},
    "30": {"title": "Substring with Concatenation of All Words", "difficulty": "HARD", "tags": ["String", "Hash Table", "Sliding Window"]}
}

def get_comprehensive_problems():
    """Get comprehensive problem data for first 200 problems"""
    problems = {}
    
    # Add the detailed sample problems
    for key, problem in SAMPLE_PROBLEMS.items():
        problems[key] = problem.copy()
    
    # Add additional problems with generated content
    for key, problem in ADDITIONAL_PROBLEMS.items():
        problem_id = int(key)
        problems[key] = {
            "id": problem_id,
            "title": problem["title"],
            "title_slug": problem["title"].lower().replace(" ", "-").replace("(", "").replace(")", ""),
            "difficulty": problem["difficulty"],
            "status": "NOT_STARTED",
            "ac_rate": round(30 + (problem_id % 40) * 1.5, 1),
            "paid_only": False,
            "tags": problem["tags"],
            "content": f"This is the LeetCode problem: {problem['title']}. It involves working with {', '.join(problem['tags']).lower()} concepts and requires efficient algorithmic thinking.",
            "example_testcases": f"Example input for {problem['title']}",
            "code_snippets": [],
            "last_updated": "2025-08-18T22:46:41.938863"
        }
    
    # Generate remaining problems up to 200
    for i in range(31, 201):
        # Generate realistic problem data
        if i <= 50:
            difficulty = "EASY"
            ac_rate = round(45 + (i % 20) * 2, 1)
        elif i <= 150:
            difficulty = "MEDIUM"
            ac_rate = round(30 + (i % 30) * 1.5, 1)
        else:
            difficulty = "HARD"
            ac_rate = round(20 + (i % 25) * 1.2, 1)
        
        # Generate realistic tags based on problem number
        tag_options = [
            ["Array", "Hash Table"], ["String", "Two Pointers"], ["Linked List", "Math"],
            ["Tree", "Depth-First Search"], ["Tree", "Breadth-First Search"], ["Dynamic Programming"],
            ["Backtracking"], ["Greedy"], ["Binary Search"], ["Stack", "Queue"],
            ["Heap", "Priority Queue"], ["Graph", "Breadth-First Search"], ["Graph", "Depth-First Search"],
            ["Union Find"], ["Trie"], ["Segment Tree"], ["Binary Indexed Tree"]
        ]
        tags = tag_options[i % len(tag_options)]
        
        problems[str(i)] = {
            "id": i,
            "title": f"Problem {i}",
            "title_slug": f"problem-{i}",
            "difficulty": difficulty,
            "status": "NOT_STARTED",
            "ac_rate": ac_rate,
            "paid_only": False,
            "tags": tags,
            "content": f"This is problem #{i} in the LeetCode collection. It involves working with {', '.join(tags).lower()} concepts and requires efficient algorithmic thinking.",
            "example_testcases": f"Example input for problem {i}",
            "code_snippets": [],
            "last_updated": "2025-08-18T22:46:41.938863"
        }
    
    return problems

if __name__ == "__main__":
    problems = get_comprehensive_problems()
    print(f"Generated {len(problems)} problems")
    print("Sample problems:")
    for i in range(1, 6):
        print(f"{i}: {problems[str(i)]['title']} ({problems[str(i)]['difficulty']})") 