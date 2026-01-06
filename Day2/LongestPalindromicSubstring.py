""" Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb" """

def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""

    start=end=0

    def expand(left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1  # valid palindrome bounds

    for i in range(len(s)):
            # Odd-length palindrome
            l1, r1 = expand(i, i)
            # Even-length palindrome
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

    return s[start:end + 1]

if __name__ == "__main__":
    test_strings = ["babad", "cbbd", "a", "ac", "racecar"]
    for test_str in test_strings:
        result = longest_palindromic_substring(test_str)
        print(f"The longest palindromic substring in '{test_str}' is: '{result}'")
