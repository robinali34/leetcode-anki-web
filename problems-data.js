// Top 200 LeetCode Problems Data
const topLeetCodeProblems = [
    {
        id: 1,
        title: "Two Sum",
        difficulty: "Easy",
        tags: ["Array", "Hash Table"],
        acceptance: "52.3%",
        fullDescription: "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.",
        testCases: [
            { input: "nums = [2,7,11,15], target = 9", output: "[0,1]", explanation: "Because nums[0] + nums[1] == 9, we return [0, 1]." },
            { input: "nums = [3,2,4], target = 6", output: "[1,2]", explanation: "Because nums[1] + nums[2] == 6, we return [1, 2]." }
        ],
        pseudocode: "Use hash table to store complements",
        pythonCode: "Hash table approach with O(n) time complexity",
        timeComplexity: "O(n)",
        spaceComplexity: "O(n)",
        keyInsights: ["Hash table for O(1) lookups", "Check complement for each number"]
    },
    {
        id: 2,
        title: "Add Two Numbers",
        difficulty: "Medium",
        tags: ["Linked List", "Math", "Recursion"],
        acceptance: "38.9%",
        fullDescription: "You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.",
        testCases: [
            { input: "l1 = [2,4,3], l2 = [5,6,4]", output: "[7,0,8]", explanation: "342 + 465 = 807" }
        ],
        pseudocode: "Process digits with carry handling",
        pythonCode: "Linked list traversal with carry",
        timeComplexity: "O(max(m,n))",
        spaceComplexity: "O(max(m,n))",
        keyInsights: ["Handle carry-over", "Process from least significant digit"]
    },
    {
        id: 3,
        title: "Longest Substring Without Repeating Characters",
        difficulty: "Medium",
        tags: ["Hash Table", "String", "Sliding Window"],
        acceptance: "33.8%",
        fullDescription: "Given a string s, find the length of the longest substring without repeating characters. A substring is a contiguous non-empty sequence of characters within a string.",
        testCases: [
            { input: 's = "abcabcbb"', output: "3", explanation: "The answer is 'abc', with the length of 3." }
        ],
        pseudocode: "Sliding window with hash set",
        pythonCode: "Two pointers with character tracking",
        timeComplexity: "O(n)",
        spaceComplexity: "O(min(m,n))",
        keyInsights: ["Sliding window technique", "Expand right, contract left"]
    },
    {
        id: 4,
        title: "Median of Two Sorted Arrays",
        difficulty: "Hard",
        tags: ["Array", "Binary Search", "Divide and Conquer"],
        acceptance: "35.2%",
        fullDescription: "Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log(m+n)).",
        testCases: [
            { input: "nums1 = [1,3], nums2 = [2]", output: "2.00000", explanation: "merged array = [1,2,3] and median is 2." }
        ],
        pseudocode: "Binary search on partition",
        pythonCode: "Complex binary search implementation",
        timeComplexity: "O(log(min(m,n)))",
        spaceComplexity: "O(1)",
        keyInsights: ["Binary search on smaller array", "Find correct partition"]
    },
    {
        id: 5,
        title: "Longest Palindromic Substring",
        difficulty: "Medium",
        tags: ["String", "Dynamic Programming"],
        acceptance: "32.1%",
        fullDescription: "Given a string s, return the longest palindromic substring in s. A string is palindromic if it reads the same forward and backward.",
        testCases: [
            { input: 's = "babad"', output: '"bab"', explanation: '"aba" is also a valid answer.' }
        ],
        pseudocode: "Expand around center",
        pythonCode: "Center expansion approach",
        timeComplexity: "O(n²)",
        spaceComplexity: "O(1)",
        keyInsights: ["Check odd and even centers", "Expand outward"]
    },
    {
        id: 15,
        title: "3Sum",
        difficulty: "Medium",
        tags: ["Array", "Two Pointers", "Sorting"],
        acceptance: "32.1%",
        fullDescription: "Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.",
        testCases: [
            { input: "nums = [-1,0,1,2,-1,-4]", output: "[[-1,-1,2],[-1,0,1]]", explanation: "The triplets that sum to zero." }
        ],
        pseudocode: "Sort + two pointers",
        pythonCode: "Three pointer approach",
        timeComplexity: "O(n²)",
        spaceComplexity: "O(1)",
        keyInsights: ["Sort first", "Use two pointers", "Skip duplicates"]
    },
    {
        id: 17,
        title: "Letter Combinations of a Phone Number",
        difficulty: "Medium",
        tags: ["Hash Table", "String", "Backtracking"],
        acceptance: "56.3%",
        fullDescription: "Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.",
        testCases: [
            { input: 'digits = "23"', output: '["ad","ae","af","bd","be","bf","cd","ce","cf"]', explanation: "All possible combinations." }
        ],
        pseudocode: "Backtracking with digit mapping",
        pythonCode: "Recursive backtracking",
        timeComplexity: "O(4^n × n)",
        spaceComplexity: "O(n)",
        keyInsights: ["Backtracking approach", "Build combinations recursively"]
    },
    {
        id: 19,
        title: "Remove Nth Node From End of List",
        difficulty: "Medium",
        tags: ["Linked List", "Two Pointers"],
        acceptance: "40.1%",
        fullDescription: "Given the head of a linked list, remove the nth node from the end of the list and return its head.",
        testCases: [
            { input: "head = [1,2,3,4,5], n = 2", output: "[1,2,3,5]", explanation: "Remove the 2nd node from the end." }
        ],
        pseudocode: "Two pointer technique",
        pythonCode: "Fast and slow pointers",
        timeComplexity: "O(n)",
        spaceComplexity: "O(1)",
        keyInsights: ["Two pointer approach", "Handle edge cases"]
    },
    {
        id: 20,
        title: "Valid Parentheses",
        difficulty: "Easy",
        tags: ["String", "Stack"],
        acceptance: "40.1%",
        fullDescription: "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
        testCases: [
            { input: 's = "()"', output: "true", explanation: "Simple valid parentheses." }
        ],
        pseudocode: "Stack for matching",
        pythonCode: "Stack-based validation",
        timeComplexity: "O(n)",
        spaceComplexity: "O(n)",
        keyInsights: ["Use stack", "Check for matching pairs"]
    },
    {
        id: 21,
        title: "Merge Two Sorted Lists",
        difficulty: "Easy",
        tags: ["Linked List", "Recursion"],
        acceptance: "62.3%",
        fullDescription: "You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list.",
        testCases: [
            { input: "list1 = [1,2,4], list2 = [1,3,4]", output: "[1,1,2,3,4,4]", explanation: "Merged sorted list." }
        ],
        pseudocode: "Compare and merge",
        pythonCode: "Iterative merge",
        timeComplexity: "O(m+n)",
        spaceComplexity: "O(1)",
        keyInsights: ["Compare heads", "Build new list"]
    },
    {
        id: 22,
        title: "Generate Parentheses",
        difficulty: "Medium",
        tags: ["String", "Backtracking", "Dynamic Programming"],
        acceptance: "70.1%",
        fullDescription: "Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.",
        testCases: [
            { input: "n = 3", output: '["((()))","(()())","(())()","()(())","()()()"]', explanation: "All valid combinations." }
        ],
        pseudocode: "Backtracking with constraints",
        pythonCode: "Recursive generation",
        timeComplexity: "O(4^n/√n)",
        spaceComplexity: "O(n)",
        keyInsights: ["Track open/close count", "Backtracking approach"]
    },
    {
        id: 23,
        title: "Merge k Sorted Lists",
        difficulty: "Hard",
        tags: ["Linked List", "Divide and Conquer", "Heap (Priority Queue)"],
        acceptance: "47.1%",
        fullDescription: "You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list.",
        testCases: [
            { input: "lists = [[1,4,5],[1,3,4],[2,6]]", output: "[1,1,2,3,4,4,5,6]", explanation: "Merged sorted list." }
        ],
        pseudocode: "Min heap approach",
        pythonCode: "Priority queue merge",
        timeComplexity: "O(n log k)",
        spaceComplexity: "O(k)",
        keyInsights: ["Use min heap", "Compare heads efficiently"]
    },
    {
        id: 31,
        title: "Next Permutation",
        difficulty: "Medium",
        tags: ["Array", "Two Pointers"],
        acceptance: "37.1%",
        fullDescription: "Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.",
        testCases: [
            { input: "nums = [1,2,3]", output: "[1,3,2]", explanation: "Next permutation." }
        ],
        pseudocode: "Find decreasing suffix",
        pythonCode: "Two pointer approach",
        timeComplexity: "O(n)",
        spaceComplexity: "O(1)",
        keyInsights: ["Find decreasing suffix", "Swap and reverse"]
    },
    {
        id: 32,
        title: "Longest Valid Parentheses",
        difficulty: "Hard",
        tags: ["String", "Dynamic Programming", "Stack"],
        acceptance: "32.1%",
        fullDescription: "Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.",
        testCases: [
            { input: 's = "(()"', output: "2", explanation: "Longest valid substring is '()'." }
        ],
        pseudocode: "Stack with indices",
        pythonCode: "Stack-based solution",
        timeComplexity: "O(n)",
        spaceComplexity: "O(n)",
        keyInsights: ["Use stack", "Track valid lengths"]
    },
    {
        id: 33,
        title: "Search in Rotated Sorted Array",
        difficulty: "Medium",
        tags: ["Array", "Binary Search"],
        acceptance: "40.1%",
        fullDescription: "There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k.",
        testCases: [
            { input: "nums = [4,5,6,7,0,1,2], target = 0", output: "4", explanation: "Target found at index 4." }
        ],
        pseudocode: "Modified binary search",
        pythonCode: "Binary search with rotation handling",
        timeComplexity: "O(log n)",
        spaceComplexity: "O(1)",
        keyInsights: ["Modified binary search", "Handle rotation"]
    },
    {
        id: 34,
        title: "Find First and Last Position of Element in Sorted Array",
        difficulty: "Medium",
        tags: ["Array", "Binary Search"],
        acceptance: "42.1%",
        fullDescription: "Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.",
        testCases: [
            { input: "nums = [5,7,7,8,8,10], target = 8", output: "[3,4]", explanation: "Target appears at indices 3 and 4." }
        ],
        pseudocode: "Two binary searches",
        pythonCode: "Binary search for bounds",
        timeComplexity: "O(log n)",
        spaceComplexity: "O(1)",
        keyInsights: ["Two binary searches", "Find left and right bounds"]
    },
    {
        id: 39,
        title: "Combination Sum",
        difficulty: "Medium",
        tags: ["Array", "Backtracking"],
        acceptance: "65.1%",
        fullDescription: "Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.",
        testCases: [
            { input: "candidates = [2,3,6,7], target = 7", output: "[[2,2,3],[7]]", explanation: "Valid combinations." }
        ],
        pseudocode: "Backtracking with sum",
        pythonCode: "Recursive backtracking",
        timeComplexity: "O(2^n)",
        spaceComplexity: "O(n)",
        keyInsights: ["Backtracking approach", "Track current sum"]
    },
    {
        id: 42,
        title: "Trapping Rain Water",
        difficulty: "Hard",
        tags: ["Array", "Two Pointers", "Dynamic Programming", "Stack"],
        acceptance: "60.1%",
        fullDescription: "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
        testCases: [
            { input: "height = [0,1,0,2,1,0,1,3,2,1,2,1]", output: "6", explanation: "Total trapped water is 6 units." }
        ],
        pseudocode: "Two pointer approach",
        pythonCode: "Dynamic programming solution",
        timeComplexity: "O(n)",
        spaceComplexity: "O(1)",
        keyInsights: ["Two pointers", "Track left and right max"]
    },
    {
        id: 46,
        title: "Permutations",
        difficulty: "Medium",
        tags: ["Array", "Backtracking"],
        acceptance: "75.1%",
        fullDescription: "Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.",
        testCases: [
            { input: "nums = [1,2,3]", output: "[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]", explanation: "All permutations." }
        ],
        pseudocode: "Backtracking with swapping",
        pythonCode: "Recursive permutation generation",
        timeComplexity: "O(n!)",
        spaceComplexity: "O(n)",
        keyInsights: ["Backtracking", "Swap elements"]
    },
    {
        id: 48,
        title: "Rotate Image",
        difficulty: "Medium",
        tags: ["Array", "Math", "Matrix"],
        acceptance: "70.1%",
        fullDescription: "You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).",
        testCases: [
            { input: "matrix = [[1,2,3],[4,5,6],[7,8,9]]", output: "[[7,4,1],[8,5,2],[9,6,3]]", explanation: "Rotated 90 degrees clockwise." }
        ],
        pseudocode: "Transpose and reverse",
        pythonCode: "Matrix manipulation",
        timeComplexity: "O(n²)",
        spaceComplexity: "O(1)",
        keyInsights: ["Transpose matrix", "Reverse each row"]
    },
    {
        id: 49,
        title: "Group Anagrams",
        difficulty: "Medium",
        tags: ["Array", "Hash Table", "String", "Sorting"],
        acceptance: "70.1%",
        fullDescription: "Given an array of strings strs, group the anagrams together. You can return the answer in any order.",
        testCases: [
            { input: 'strs = ["eat","tea","tan","ate","nat","bat"]', output: '[["bat"],["nat","tan"],["ate","eat","tea"]]', explanation: "Grouped anagrams." }
        ],
        pseudocode: "Sort strings as keys",
        pythonCode: "Hash table with sorted keys",
        timeComplexity: "O(n × k log k)",
        spaceComplexity: "O(n × k)",
        keyInsights: ["Sort strings", "Use as hash keys"]
    },
    {
        id: 53,
        title: "Maximum Subarray",
        difficulty: "Medium",
        tags: ["Array", "Divide and Conquer", "Dynamic Programming"],
        acceptance: "50.1%",
        fullDescription: "Given an integer array nums, find the subarray with the largest sum, and return its sum.",
        testCases: [
            { input: "nums = [-2,1,-3,4,-1,2,1,-5,4]", output: "6", explanation: "Subarray [4,-1,2,1] has the largest sum 6." }
        ],
        pseudocode: "Kadane's algorithm",
        pythonCode: "Dynamic programming approach",
        timeComplexity: "O(n)",
        spaceComplexity: "O(1)",
        keyInsights: ["Kadane's algorithm", "Track current and max sum"]
    }
];

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = topLeetCodeProblems;
} 