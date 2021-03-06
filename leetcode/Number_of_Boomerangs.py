"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k)
such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all
in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

"""


class Solution(object):
    def boomerangs(self, nums):
        res = 0
        for p in nums:
            tem = {}
            for q in nums:
                dis = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                tem[dis] = tem.get(dis, 0) + 1
            for key in tem:
                res += tem[key] * (tem[key] - 1)
        return res


