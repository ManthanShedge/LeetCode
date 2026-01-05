# Given a string s, find the length of the longest substring without duplicate characters.

""" Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. """

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    left_pointer = 0
    max_length = 0

    for right_pointer in range(len(s)):
        current_char = s[right_pointer]
        if current_char in char_index_map and char_index_map[current_char] >= left_pointer:
            left_pointer = char_index_map[current_char] + 1
        char_index_map[current_char] = right_pointer
        max_length = max(max_length, right_pointer - left_pointer + 1)

    return max_length

if __name__ == "__main__":
    test_strings = ["abcabcbb", "bbbbb", "pwwkew"]
    for test_str in test_strings:
        result = length_of_longest_substring(test_str)
        print(f"The length of the longest substring without repeating characters in '{test_str}' is: {result}")