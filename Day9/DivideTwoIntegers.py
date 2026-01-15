""" Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [-2^31, 2^31 - 1]. For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.


Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2. """

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge case for overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the quotient
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values to simplify the division logic
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        # Subtract divisor from dividend until dividend is less than divisor
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        
        # Apply the sign to the quotient
        return -quotient if negative else quotient
    
# Example usage:
solution = Solution()
print(solution.divide(10, 3))  # Output: 3
print(solution.divide(7, -3))  # Output: -2
