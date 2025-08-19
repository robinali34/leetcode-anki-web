#!/usr/bin/env python3
"""
Solution generator for LeetCode problems
Provides pseudocode and Python code solutions
"""

class SolutionGenerator:
    def __init__(self):
        self.solutions = {
            # Two Sum - Most popular hash table approach
            "1": {
                "pseudocode": """PSEUDOCODE for Two Sum:
1. Create an empty hash map to store numbers and their indices
2. Iterate through the array with index i and value num
3. Calculate complement = target - num
4. If complement exists in hash map, return [hash_map[complement], i]
5. Otherwise, store num and its index i in hash map
6. If no solution found, return empty array

Time Complexity: O(n) - single pass through array
Space Complexity: O(n) - hash map storage""",
                
                "python_code": """def twoSum(nums, target):
    # Hash map to store numbers and their indices
    num_map = {}
    
    # Iterate through array
    for i, num in enumerate(nums):
        # Calculate complement
        complement = target - num
        
        # If complement exists, we found our pair
        if complement in num_map:
            return [num_map[complement], i]
        
        # Store current number and index
        num_map[num] = i
    
    # No solution found
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(f"Indices: {result}")  # Output: [0, 1]"""
            },
            
            # Add Two Numbers - Linked list manipulation
            "2": {
                "pseudocode": """PSEUDOCODE for Add Two Numbers:
1. Initialize dummy head node and current pointer
2. Initialize carry = 0
3. While l1 or l2 or carry exists:
   a. Get values from l1 and l2 (0 if None)
   b. Calculate sum = val1 + val2 + carry
   c. Create new node with value = sum % 10
   d. Update carry = sum // 10
   e. Move pointers forward
4. Return dummy.next

Time Complexity: O(max(m,n)) - where m,n are list lengths
Space Complexity: O(max(m,n)) - new result list""",
                
                "python_code": """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # Dummy head node
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    # Process both lists
    while l1 or l2 or carry:
        # Get values (0 if list is exhausted)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        
        # Create new node
        current.next = ListNode(total % 10)
        current = current.next
        
        # Move pointers forward
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
    return dummy.next

# Example usage
# l1 = 2 -> 4 -> 3 (represents 342)
# l2 = 5 -> 6 -> 4 (represents 465)
# Result: 7 -> 0 -> 8 (represents 807)"""
            },
            
            # Longest Substring Without Repeating Characters - Sliding window
            "3": {
                "pseudocode": """PSEUDOCODE for Longest Substring Without Repeating Characters:
1. Initialize variables:
   - start = 0 (start of current window)
   - max_length = 0
   - char_map = {} (to store character positions)
2. Iterate through string with index i and char c
3. If c exists in char_map and position >= start:
   - Update start = char_map[c] + 1
4. Update char_map[c] = i
5. Update max_length = max(max_length, i - start + 1)
6. Return max_length

Time Complexity: O(n) - single pass through string
Space Complexity: O(min(m,n)) - where m is charset size""",
                
                "python_code": """def lengthOfLongestSubstring(s):
    # Track character positions
    char_map = {}
    start = 0
    max_length = 0
    
    # Iterate through string
    for i, char in enumerate(s):
        # If character exists and is within current window
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        
        # Update character position
        char_map[char] = i
        
        # Update max length
        max_length = max(max_length, i - start + 1)
    
    return max_length

# Example usage
s = "abcabcbb"
result = lengthOfLongestSubstring(s)
print(f"Longest substring length: {result}")  # Output: 3 ("abc")"""
            },
            
            # Median of Two Sorted Arrays - Binary search approach
            "4": {
                "pseudocode": """PSEUDOCODE for Median of Two Sorted Arrays:
1. Ensure nums1 is the smaller array
2. Perform binary search on nums1:
   a. Calculate partitionX = (left + right) // 2
   b. Calculate partitionY = (m + n + 1) // 2 - partitionX
   c. Get maxLeftX, minRightX, maxLeftY, minRightY
3. Check if partition is correct:
   - maxLeftX <= minRightY AND maxLeftY <= minRightX
4. If correct, calculate median based on total length
5. If maxLeftX > minRightY, move right = partitionX - 1
6. If maxLeftY > minRightX, move left = partitionX + 1

Time Complexity: O(log(min(m,n))) - binary search on smaller array
Space Complexity: O(1) - constant extra space""",
                
                "python_code": """def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is smaller
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        # Partition nums1
        partitionX = (left + right) // 2
        partitionY = (m + n + 1) // 2 - partitionX
        
        # Get values around partitions
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == m else nums1[partitionX]
        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == n else nums2[partitionY]
        
        # Check if partition is correct
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            # Calculate median
            if (m + n) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            right = partitionX - 1
        else:
            left = partitionX + 1
    
    return 0.0

# Example usage
nums1 = [1, 3]
nums2 = [2]
result = findMedianSortedArrays(nums1, nums2)
print(f"Median: {result}")  # Output: 2.0"""
            },
            
            # Longest Palindromic Substring - Expand around center
            "5": {
                "pseudocode": """PSEUDOCODE for Longest Palindromic Substring:
1. Initialize start = 0, max_length = 1
2. For each character at index i:
   a. Check odd-length palindromes: expandAroundCenter(i, i)
   b. Check even-length palindromes: expandAroundCenter(i, i+1)
3. expandAroundCenter function:
   a. While left >= 0 and right < len(s) and s[left] == s[right]
   b. Decrement left, increment right
   c. Update start and max_length if current length > max_length
4. Return s[start:start + max_length]

Time Complexity: O(n²) - for each character, expand palindrome
Space Complexity: O(1) - constant extra space""",
                
                "python_code": """def longestPalindrome(s):
    if not s:
        return ""
    
    start = 0
    max_length = 1
    
    def expandAroundCenter(left, right):
        nonlocal start, max_length
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Update if current palindrome is longer
        if right - left - 1 > max_length:
            start = left + 1
            max_length = right - left - 1
    
    # Check each character as center
    for i in range(len(s)):
        # Odd length palindromes
        expandAroundCenter(i, i)
        # Even length palindromes
        expandAroundCenter(i, i + 1)
    
    return s[start:start + max_length]

# Example usage
s = "babad"
result = longestPalindrome(s)
print(f"Longest palindrome: {result}")  # Output: "bab" or "aba\""""
            },
            
            # Zigzag Conversion - Row-by-row approach
            "6": {
                "pseudocode": """PSEUDOCODE for Zigzag Conversion:
1. If numRows == 1, return the original string
2. Create an array of numRows empty strings
3. Initialize currentRow = 0 and direction = 1 (down)
4. For each character in the string:
   a. Add character to currentRow string
   b. If currentRow == 0, set direction = 1 (down)
   c. If currentRow == numRows-1, set direction = -1 (up)
   d. Update currentRow += direction
5. Join all rows and return

Time Complexity: O(n) - single pass through string
Space Complexity: O(n) - store result strings""",
                
                "python_code": """def convert(s, numRows):
    if numRows == 1:
        return s
    
    # Create rows
    rows = [""] * numRows
    currentRow = 0
    direction = 1  # 1 for down, -1 for up
    
    # Process each character
    for char in s:
        rows[currentRow] += char
        
        # Change direction at boundaries
        if currentRow == 0:
            direction = 1
        elif currentRow == numRows - 1:
            direction = -1
        
        currentRow += direction
    
    # Join all rows
    return "".join(rows)

# Example usage
s = "PAYPALISHIRING"
numRows = 3
result = convert(s, numRows)
print(f"Zigzag conversion: {result}")  # Output: "PAHNAPLSIIGYIR\""""
            },
            
            # Reverse Integer - Mathematical approach
            "7": {
                "pseudocode": """PSEUDOCODE for Reverse Integer:
1. Handle edge case: if x == 0, return 0
2. Determine sign: is_negative = x < 0
3. Convert to positive: x = abs(x)
4. Initialize result = 0
5. While x > 0:
   a. digit = x % 10
   b. result = result * 10 + digit
   c. x = x // 10
6. Apply sign: result = -result if is_negative
7. Check overflow: if result > 2^31 - 1 or < -2^31, return 0
8. Return result

Time Complexity: O(log n) - number of digits
Space Complexity: O(1) - constant extra space""",
                
                "python_code": """def reverse(x):
    # Handle edge case
    if x == 0:
        return 0
    
    # Determine sign and convert to positive
    is_negative = x < 0
    x = abs(x)
    
    result = 0
    while x > 0:
        digit = x % 10
        result = result * 10 + digit
        x //= 10
    
    # Apply sign
    if is_negative:
        result = -result
    
    # Check overflow (32-bit signed integer)
    if result > 2**31 - 1 or result < -2**31:
        return 0
    
    return result

# Example usage
x = 123
result = reverse(x)
print(f"Reversed: {result}")  # Output: 321"""
            },
            
            # String to Integer (atoi) - Parsing with validation
            "8": {
                "pseudocode": """PSEUDOCODE for String to Integer (atoi):
1. Skip leading whitespace
2. Handle sign: check for '+' or '-'
3. Read digits until non-digit character
4. Convert digits to integer
5. Apply sign
6. Handle overflow: clamp to 32-bit range
7. Return result

Time Complexity: O(n) - single pass through string
Space Complexity: O(1) - constant extra space""",
                
                "python_code": """def myAtoi(s):
    if not s:
        return 0
    
    # Skip leading whitespace
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    
    if i >= len(s):
        return 0
    
    # Handle sign
    sign = 1
    if s[i] == '+' or s[i] == '-':
        sign = -1 if s[i] == '-' else 1
        i += 1
    
    # Read digits
    result = 0
    while i < len(s) and s[i].isdigit():
        digit = int(s[i])
        result = result * 10 + digit
        i += 1
    
    # Apply sign
    result *= sign
    
    # Handle overflow
    if result > 2**31 - 1:
        return 2**31 - 1
    elif result < -2**31:
        return -2**31
    
    return result

# Example usage
s = "42"
result = myAtoi(s)
print(f"Converted: {result}")  # Output: 42"""
            },
            
            # Palindrome Number - Mathematical approach
            "9": {
                "pseudocode": """PSEUDOCODE for Palindrome Number:
1. Handle edge cases: negative numbers are not palindromes
2. If x == 0, return True
3. Initialize reversed_num = 0
4. While x > reversed_num:
   a. digit = x % 10
   b. reversed_num = reversed_num * 10 + digit
   c. x = x // 10
5. Check if x == reversed_num (even digits) or x == reversed_num // 10 (odd digits)
6. Return True if palindrome, False otherwise

Time Complexity: O(log n) - number of digits
Space Complexity: O(1) - constant extra space""",
                
                "python_code": """def isPalindrome(x):
    # Negative numbers are not palindromes
    if x < 0:
        return False
    
    # Single digit numbers are palindromes
    if x < 10:
        return True
    
    # Handle trailing zeros
    if x != 0 and x % 10 == 0:
        return False
    
    reversed_num = 0
    while x > reversed_num:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    
    # For even digits: x == reversed_num
    # For odd digits: x == reversed_num // 10
    return x == reversed_num or x == reversed_num // 10

# Example usage
x = 121
result = isPalindrome(x)
print(f"Is palindrome: {result}")  # Output: True"""
            },
            
            # Regular Expression Matching - Dynamic programming
            "10": {
                "pseudocode": """PSEUDOCODE for Regular Expression Matching:
1. Use dynamic programming with 2D table dp[i][j]
2. Base cases:
   - dp[0][0] = True (empty strings match)
   - dp[0][j] = False for j > 0 (empty pattern doesn't match non-empty string)
3. For each character in pattern:
   a. If current char is '*':
      - Check if previous char matches 0 or more times
   b. If current char is '.' or matches string char:
      - Check if previous characters match
4. Return dp[len(s)][len(p)]

Time Complexity: O(m*n) - where m,n are string and pattern lengths
Space Complexity: O(m*n) - DP table storage""",
                
                "python_code": """def isMatch(s, p):
    # Create DP table
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns with *
    for j in range(1, len(p) + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    
    # Fill DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2]  # 0 occurrences
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]  # 1+ occurrences
    
    return dp[len(s)][len(p)]

# Example usage
s = "aa"
p = "a*"
result = isMatch(s, p)
print(f"Pattern matches: {result}")  # Output: True"""
            },
            
            # Container With Most Water - Two pointers
            "11": {
                "pseudocode": """PSEUDOCODE for Container With Most Water:
1. Initialize two pointers: left = 0, right = len(height) - 1
2. Initialize max_area = 0
3. While left < right:
   a. Calculate current area = min(height[left], height[right]) * (right - left)
   b. Update max_area = max(max_area, current_area)
   c. Move the pointer with smaller height inward
4. Return max_area

Time Complexity: O(n) - single pass with two pointers
Space Complexity: O(1) - constant extra space""",
                
                "python_code": """def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        
        # Update max area
        max_area = max(max_area, area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Example usage
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = maxArea(height)
print(f"Max area: {result}")  # Output: 49"""
            },
            
            # Integer to Roman - Greedy approach
            "12": {
                "pseudocode": """PSEUDOCODE for Integer to Roman:
1. Create mapping of integer values to Roman numerals
2. Sort values in descending order
3. Initialize result = ""
4. For each value in sorted order:
   a. While num >= value:
      - Append corresponding Roman numeral to result
      - Subtract value from num
5. Return result

Time Complexity: O(1) - fixed number of Roman numerals
Space Complexity: O(1) - constant storage for mapping""",
                
                "python_code": """def intToRoman(num):
    # Roman numeral mapping
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    result = ""
    
    # Convert to Roman numerals
    for value, numeral in values:
        while num >= value:
            result += numeral
            num -= value
    
    return result

# Example usage
num = 1994
result = intToRoman(num)
print(f"Roman numeral: {result}")  # Output: "MCMXCIV\""""
            },
            
            # Roman to Integer - Left-to-right parsing
            "13": {
                "pseudocode": """PSEUDOCODE for Roman to Integer:
1. Create mapping of Roman numerals to integer values
2. Initialize result = 0
3. Iterate through string from left to right:
   a. If current value < next value:
      - Subtract current value from result
   b. Else:
      - Add current value to result
4. Return result

Time Complexity: O(n) - single pass through string
Space Complexity: O(1) - constant storage for mapping""",
                
                "python_code": """def romanToInt(s):
    # Roman numeral mapping
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    result = 0
    
    # Convert from left to right
    for i in range(len(s)):
        current = roman_map[s[i]]
        
        # Check if we need to subtract
        if i + 1 < len(s) and current < roman_map[s[i + 1]]:
            result -= current
        else:
            result += current
    
    return result

# Example usage
s = "MCMXCIV"
result = romanToInt(s)
print(f"Integer: {result}")  # Output: 1994"""
            },
            
            # Longest Common Prefix - Horizontal scanning
            "14": {
                "pseudocode": """PSEUDOCODE for Longest Common Prefix:
1. If strs is empty, return ""
2. Initialize prefix = strs[0]
3. For each string in strs[1:]:
   a. While prefix is not a prefix of current string:
      - Remove last character from prefix
      - If prefix becomes empty, return ""
4. Return prefix

Time Complexity: O(S) - where S is sum of all characters
Space Complexity: O(1) - constant extra space""",
                
                "python_code": """def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with first string as prefix
    prefix = strs[0]
    
    # Check each string
    for s in strs[1:]:
        # Reduce prefix until it's a prefix of current string
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Example usage
strs = ["flower", "flow", "flight"]
result = longestCommonPrefix(strs)
print(f"Common prefix: {result}")  # Output: "fl\""""
            },
            
            # 3Sum - Two pointers with sorting
            "15": {
                "pseudocode": """PSEUDOCODE for 3Sum:
1. Sort the array
2. Initialize result = []
3. For each i from 0 to len(nums) - 2:
   a. Skip duplicates for i
   b. Initialize left = i + 1, right = len(nums) - 1
   c. While left < right:
      - Calculate sum = nums[i] + nums[left] + nums[right]
      - If sum == 0: add triplet, skip duplicates, move pointers
      - If sum < 0: left += 1
      - If sum > 0: right -= 1
4. Return result

Time Complexity: O(n²) - two nested loops
Space Complexity: O(1) - excluding output storage""",
                
                "python_code": """def threeSum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(f"3Sum result: {result}")  # Output: [[-1,-1,2], [-1,0,1]]"""
            },
            
            # 3Sum Closest - Two pointers with sorting
            "16": {
                "pseudocode": """PSEUDOCODE for 3Sum Closest:
1. Sort the array
2. Initialize closest_sum = sum of first three elements
3. For each i from 0 to len(nums) - 2:
   a. Skip duplicates for i
   b. Initialize left = i + 1, right = len(nums) - 1
   c. While left < right:
      - Calculate sum = nums[i] + nums[left] + nums[right]
      - Update closest_sum if current sum is closer to target
      - If sum == target, return target
      - If sum < target: left += 1
      - If sum > target: right -= 1
4. Return closest_sum

Time Complexity: O(n²) - two nested loops
Space Complexity: O(1) - constant extra space""",
                
                "python_code": """def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = sum(nums[:3])
    
    for i in range(len(nums) - 2):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            # Update closest sum if current is closer
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum == target:
                return target
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return closest_sum

# Example usage
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(f"Closest sum: {result}")  # Output: 2"""
            },
            
            # Letter Combinations of a Phone Number - Backtracking
            "17": {
                "pseudocode": """PSEUDOCODE for Letter Combinations of a Phone Number:
1. Create mapping of digits to letters
2. Initialize result = []
3. Define backtrack function:
   a. If current combination length == digits length:
      - Add combination to result
      - Return
   b. Get letters for current digit
   c. For each letter:
      - Add letter to combination
      - Recurse with next digit
      - Remove letter (backtrack)
4. Call backtrack with empty combination
5. Return result

Time Complexity: O(4^n) - where n is digits length
Space Complexity: O(n) - recursion stack depth""",
                
                "python_code": """def letterCombinations(digits):
    if not digits:
        return []
    
    # Digit to letter mapping
    digit_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index, combination):
        # Base case: combination is complete
        if len(combination) == len(digits):
            result.append(''.join(combination))
            return
        
        # Get letters for current digit
        current_digit = digits[index]
        letters = digit_map[current_digit]
        
        # Try each letter
        for letter in letters:
            combination.append(letter)
            backtrack(index + 1, combination)
            combination.pop()  # Backtrack
    
    backtrack(0, [])
    return result

# Example usage
digits = "23"
result = letterCombinations(digits)
print(f"Combinations: {result}")  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]"""
            },
            
            # 4Sum - Two pointers with sorting and deduplication
            "18": {
                "pseudocode": """PSEUDOCODE for 4Sum:
1. Sort the array
2. Initialize result = []
3. For each i from 0 to len(nums) - 3:
   a. Skip duplicates for i
   b. For each j from i + 1 to len(nums) - 2:
      - Skip duplicates for j
      - Initialize left = j + 1, right = len(nums) - 1
      - While left < right:
         * Calculate sum = nums[i] + nums[j] + nums[left] + nums[right]
         * If sum == target: add quadruplet, skip duplicates, move pointers
         * If sum < target: left += 1
         * If sum > target: right -= 1
4. Return result

Time Complexity: O(n³) - three nested loops
Space Complexity: O(1) - excluding output storage""",
                
                "python_code": """def fourSum(nums, target):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 3):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range(i + 1, len(nums) - 2):
            # Skip duplicates for j
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            
            left, right = j + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    
    return result

# Example usage
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
print(f"4Sum result: {result}")  # Output: [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]"""
            },
            
            # Remove Nth Node From End of List - Two pointers
            "19": {
                "pseudocode": """PSEUDOCODE for Remove Nth Node From End of List:
1. Create dummy head node
2. Initialize first and second pointers at dummy
3. Move first pointer n + 1 steps forward
4. Move both pointers until first reaches end
5. Second pointer will be at node before target
6. Remove target node: second.next = second.next.next
7. Return dummy.next

Time Complexity: O(n) - single pass through list
Space Complexity: O(1) - constant extra space""",
                
                "python_code": """def removeNthFromEnd(head, n):
    # Create dummy head
    dummy = ListNode(0)
    dummy.next = head
    
    # Initialize two pointers
    first = dummy
    second = dummy
    
    # Move first pointer n + 1 steps forward
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove nth node from end
    second.next = second.next.next
    
    return dummy.next

# Example usage
# head = 1 -> 2 -> 3 -> 4 -> 5
# n = 2
# Result: 1 -> 2 -> 3 -> 5"""
            },
            
            # Valid Parentheses - Stack approach
            "20": {
                "pseudocode": """PSEUDOCODE for Valid Parentheses:
1. Initialize stack = []
2. Create mapping of closing to opening brackets
3. For each character in string:
   a. If character is opening bracket: push to stack
   b. If character is closing bracket:
      - If stack is empty: return False
      - If top of stack doesn't match: return False
      - Pop from stack
4. Return True if stack is empty, False otherwise

Time Complexity: O(n) - single pass through string
Space Complexity: O(n) - stack storage""",
                
                "python_code": """def isValid(s):
    # Stack to track opening brackets
    stack = []
    
    # Mapping of closing to opening brackets
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Process each character
    for char in s:
        if char in '({[':
            # Opening bracket
            stack.append(char)
        else:
            # Closing bracket
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    # Check if all brackets are matched
    return len(stack) == 0

# Example usage
s = "()[]{}"
result = isValid(s)
print(f"Valid parentheses: {result}")  # Output: True"""
            },
            
            # Merge Two Sorted Lists - Iterative approach
            "21": {
                "pseudocode": """PSEUDOCODE for Merge Two Sorted Lists:
1. Create dummy head node
2. Initialize current pointer at dummy
3. While both l1 and l2 exist:
   a. Compare l1.val and l2.val
   b. Connect current.next to smaller node
   c. Move current and smaller list pointer forward
4. Connect remaining nodes from either list
5. Return dummy.next

Time Complexity: O(m + n) - where m,n are list lengths
Space Complexity: O(1) - constant extra space""",
                
                "python_code": """def mergeTwoLists(l1, l2):
    # Create dummy head
    dummy = ListNode(0)
    current = dummy
    
    # Merge while both lists have nodes
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Connect remaining nodes
    current.next = l1 if l1 else l2
    
    return dummy.next

# Example usage
# l1 = 1 -> 2 -> 4
# l2 = 1 -> 3 -> 4
# Result: 1 -> 1 -> 2 -> 3 -> 4 -> 4"""
            },
            
            # Generate Parentheses - Backtracking
            "22": {
                "pseudocode": """PSEUDOCODE for Generate Parentheses:
1. Initialize result = []
2. Define backtrack function with open_count, close_count, combination:
   a. If combination length == 2*n: add to result, return
   b. If open_count < n: add '(', recurse, remove '('
   c. If close_count < open_count: add ')', recurse, remove ')'
3. Call backtrack with (0, 0, "")
4. Return result

Time Complexity: O(4^n/√n) - Catalan number
Space Complexity: O(n) - recursion stack depth""",
                
                "python_code": """def generateParenthesis(n):
    result = []
    
    def backtrack(open_count, close_count, combination):
        # Base case: combination is complete
        if len(combination) == 2 * n:
            result.append(combination)
            return
        
        # Add opening parenthesis if possible
        if open_count < n:
            backtrack(open_count + 1, close_count, combination + '(')
        
        # Add closing parenthesis if valid
        if close_count < open_count:
            backtrack(open_count, close_count + 1, combination + ')')
    
    backtrack(0, 0, "")
    return result

# Example usage
n = 3
result = generateParenthesis(n)
print(f"Parentheses: {result}")  # Output: ["((()))","(()())","(())()","()(())","()()()"]"""
            },
            
            # Merge k Sorted Lists - Divide and conquer
            "23": {
                "pseudocode": """PSEUDOCODE for Merge k Sorted Lists:
1. If lists is empty: return None
2. If only one list: return it
3. Use divide and conquer:
   a. Split lists into two halves
   b. Recursively merge each half
   c. Merge the two merged halves
4. Return merged result

Time Complexity: O(n log k) - where n is total nodes, k is number of lists
Space Complexity: O(log k) - recursion stack depth""",
                
                "python_code": """def mergeKLists(lists):
    if not lists:
        return None
    
    if len(lists) == 1:
        return lists[0]
    
    # Divide and conquer
    mid = len(lists) // 2
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])
    
    return mergeTwoLists(left, right)

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 if l1 else l2
    return dummy.next

# Example usage
# lists = [[1,4,5], [1,3,4], [2,6]]
# Result: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6"""
            },
            
            # Swap Nodes in Pairs - Iterative approach
            "24": {
                "pseudocode": """PSEUDOCODE for Swap Nodes in Pairs:
1. Create dummy head node
2. Initialize current pointer at dummy
3. While current.next and current.next.next exist:
   a. Get first and second nodes
   b. Update pointers to swap nodes
   c. Move current forward by 2
4. Return dummy.next

Time Complexity: O(n) - single pass through list
Space Complexity: O(1) - constant extra space""",
                
                "python_code": """def swapPairs(head):
    # Create dummy head
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    # Swap pairs while possible
    while current.next and current.next.next:
        # Get first and second nodes
        first = current.next
        second = current.next.next
        
        # Swap nodes
        first.next = second.next
        second.next = first
        current.next = second
        
        # Move to next pair
        current = current.next.next
    
    return dummy.next

# Example usage
# head = 1 -> 2 -> 3 -> 4
# Result: 2 -> 1 -> 4 -> 3"""
            },
            
            # Reverse Nodes in k-Group - Recursive approach
            "25": {
                "pseudocode": """PSEUDOCODE for Reverse Nodes in k-Group:
1. Check if k nodes exist from current position
2. If not: return head unchanged
3. Reverse first k nodes:
   a. Initialize prev = None, current = head
   b. For k iterations: reverse links
4. Recursively reverse next k-group
5. Connect reversed groups
6. Return new head

Time Complexity: O(n) - single pass through list
Space Complexity: O(n/k) - recursion stack depth""",
                
                "python_code": """def reverseKGroup(head, k):
    # Check if k nodes exist
    count = 0
    current = head
    while current and count < k:
        current = current.next
        count += 1
    
    # If less than k nodes, return unchanged
    if count < k:
        return head
    
    # Reverse first k nodes
    prev = None
    current = head
    for _ in range(k):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    # Recursively reverse next k-group
    head.next = reverseKGroup(current, k)
    
    return prev

# Example usage
# head = 1 -> 2 -> 3 -> 4 -> 5
# k = 2
# Result: 2 -> 1 -> 4 -> 3 -> 5"""
            }
        }
    
    def get_solution(self, problem_id):
        """Get solution for a specific problem"""
        problem_id_str = str(problem_id)
        
        if problem_id_str in self.solutions:
            return self.solutions[problem_id_str]
        
        # Generate generic solution for problems without specific solutions
        return self._generate_generic_solution(problem_id)
    
    def _generate_generic_solution(self, problem_id):
        """Generate a generic solution template for problems without specific solutions"""
        return {
            "pseudocode": f"""PSEUDOCODE for Problem {problem_id}:
1. Analyze the problem requirements
2. Identify the key data structures needed
3. Design the algorithm step by step
4. Consider edge cases and boundary conditions
5. Optimize for time and space complexity
6. Test with example cases

General Approach:
- Read and understand the problem statement
- Break down into smaller subproblems if possible
- Choose appropriate data structures (arrays, hash tables, trees, graphs)
- Implement the solution with proper error handling
- Verify correctness with test cases""",
            
            "python_code": f"""def solve_problem_{problem_id}(input_data):
    \"\"\"
    Solution for Problem {problem_id}
    
    Args:
        input_data: The input data for the problem
        
    Returns:
        The solution to the problem
    \"\"\"
    # TODO: Implement your solution here
    
    # Step 1: Parse and validate input
    if not input_data:
        return None
    
    # Step 2: Initialize variables and data structures
    result = 0
    
    # Step 3: Implement the main algorithm
    # This is where you'll write your specific solution
    
    # Step 4: Handle edge cases
    # Consider what happens with empty inputs, invalid data, etc.
    
    # Step 5: Return the result
    return result

# Example usage
# input_data = "your input here"
# result = solve_problem_{problem_id}(input_data)
# print(f"Result: {{result}}")

# Test cases
def test_problem_{problem_id}():
    # Add your test cases here
    test_cases = [
        # ("input", "expected_output"),
    ]
    
    for input_data, expected in test_cases:
        result = solve_problem_{problem_id}(input_data)
        print(f"Input: {{input_data}}")
        print(f"Expected: {{expected}}, Got: {{result}}")
        print(f"Pass: {{result == expected}}\\n")

# Run tests
# test_problem_{problem_id}()"""
        }
    
    def get_all_solutions(self):
        """Get all available solutions"""
        return self.solutions
    
    def add_solution(self, problem_id, pseudocode, python_code):
        """Add a new solution for a problem"""
        self.solutions[str(problem_id)] = {
            "pseudocode": pseudocode,
            "python_code": python_code
        }

# Example usage
if __name__ == "__main__":
    generator = SolutionGenerator()
    
    # Test getting a solution
    solution = generator.get_solution(1)
    print("Problem 1 - Two Sum:")
    print("Pseudocode:")
    print(solution["pseudocode"])
    print("\nPython Code:")
    print(solution["python_code"])
    
    # Test generic solution
    generic = generator.get_solution(999)
    print("\nGeneric Solution Template:")
    print(generic["pseudocode"][:200] + "...") 