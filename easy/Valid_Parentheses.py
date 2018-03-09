"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and
"([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        stack = []
        mydir = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mydir.values():
                stack.append(char)
            elif char in mydir.keys():
                if stack == [] or mydir[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


test = Solution()
print(test.isValid("()[]{}"))
