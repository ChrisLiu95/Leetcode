"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


"""


class Solution(object):
    def generateParenthesis(self, n):
        res = []
        if not n:
            return res
        self.helper(res, "", n, n)
        return res

    def helper(self, res, s, left, right):
        if left > right:
            return
        if not left and not right:
            res.append(s)
        if left:
            self.helper(res, s + "(", left - 1, right)
        if right:
            self.helper(res, s + ")", left, right - 1)


test = Solution()
print(test.generateParenthesis(3))
