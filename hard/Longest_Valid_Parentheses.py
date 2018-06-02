"""
Given a string containing just the characters '(' and ')', find the length of the longest
valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

...自己超级难想
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        stack = []
        start = -1

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if not stack:
                    start = i
                else:
                    stack.pop()
                    if not stack:
                        res = max(res, i - start)
                    else:
                        res = max(res, i - stack[-1])
        return res
