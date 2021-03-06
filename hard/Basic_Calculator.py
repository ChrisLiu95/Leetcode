"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10 * num + int(ss)
            elif ss in ["-", "+"]:
                res += sign * num
                num = 0
                sign = [-1, 1][ss == "+"]
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign


test = Solution()
print(test.calculate("123"))
