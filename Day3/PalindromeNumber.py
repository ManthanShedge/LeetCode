""" Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left. """

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        palindrome_number = 0
        while num > 0:
            last_digit = num % 10
            palindrome_number = (palindrome_number * 10) + last_digit
            num //= 10
        return palindrome_number == x
    
# Example usage:
solution = Solution()
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121)) # Output: False
print(solution.isPalindrome(10))   # Output: False
print(solution.isPalindrome(12321))# Output: True
