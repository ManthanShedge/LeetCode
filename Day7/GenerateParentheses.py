""" Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"] """

def generateParenthesis(n):
    res = []
    stack = [("", 0, 0)]  # (current_string, open_count, close_count)

    while stack:
        curr, open_count, close_count = stack.pop()

        # If complete, add to result
        if len(curr) == 2 * n:
            res.append(curr)
            continue

        # Try adding '('
        if open_count < n:
            stack.append((curr + "(", open_count + 1, close_count))

        # Try adding ')'
        if close_count < open_count:
            stack.append((curr + ")", open_count, close_count + 1))

    return res

# Example usage:
n = 3
print(generateParenthesis(n))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
