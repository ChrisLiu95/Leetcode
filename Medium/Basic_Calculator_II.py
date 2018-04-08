"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

"""

import re


class Solution(object):
    def calculate(self, s):

        """
        3 * 2 + 4
        """
        res = 0
        sign = 1
        num = 0
        tokens = iter(re.findall('\d+|\S', s))

        for token in tokens:
            if token.isdigit():
                num = int(token)
            elif token in "+-":
                res += sign * num
                sign = 1 if token == "+" else -1
            else:
                temp = int(next(tokens))
                num = num * temp if token == "*" else num / temp

        return res + sign * num
