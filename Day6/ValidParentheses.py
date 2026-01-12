""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false """

class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False

        return not stack
    
# Example usage:
solution = Solution()
print(solution.isValid("()"))        # True
print(solution.isValid("()[]{}"))    # True
print(solution.isValid("(]"))        # False
print(solution.isValid("([)]"))      # False
print(solution.isValid("{[]}"))      # True