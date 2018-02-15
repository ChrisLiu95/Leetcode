"""
Write a function that takes an integer n and return all possible combinations of its factors.

Note:
You may assume that n is always positive.
Factors should be greater than 1 and less than n.

input: 37
output:
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

"""


class Solution(object):
    def getFactors(self, n):
        ans, stack, x = [], [], 2
        while True:
            if x > n / x:
                if not stack:
                    return ans
                ans.append(stack + [int(n)])
                x = stack.pop()
                n *= x
                x += 1
            elif n % x == 0:
                stack.append(x)
                n /= x
            else:
                x += 1


test = Solution()
print(test.getFactors(12))
