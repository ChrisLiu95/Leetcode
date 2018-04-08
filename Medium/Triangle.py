"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to
adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
从下往上扫，分别两两比较

important

"""


class Solution(object):
    def minimumTotal(self, triangle):
        f = [0] * (len(triangle) + 1)  # 防止越界
        for row in triangle[::-1]:
            for i in range(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]


test = Solution()
print(test.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
