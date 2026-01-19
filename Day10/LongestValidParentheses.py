""" Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0 """

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]  # Initialize stack with -1 to handle base case
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '(' onto the stack
            else:
                stack.pop()  # Pop the last '(' index
                if not stack:
                    stack.append(i)  # If stack is empty, push current index
                else:
                    max_length = max(max_length, i - stack[-1])  # Calculate valid length
        
        return max_length
    
# Example usage:
solution = Solution()
s1 = "(()"
print(solution.longestValidParentheses(s1))  # Output: 2
s2 = ")()())"
print(solution.longestValidParentheses(s2))  # Output: 4
s3 = ""
print(solution.longestValidParentheses(s3))  # Output: 0