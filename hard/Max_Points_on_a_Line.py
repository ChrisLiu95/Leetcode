"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

"""

import numpy as np


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        res = 0

        for i in range(len(points)):
            mydir = {"inf": 1}
            same = 0
            for j in range(len(points)):
                if j == i:
                    continue
                dx, dy = points[j].x - points[i].x, points[j].y - points[i].y
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                slope = dy * np.longdouble(1) / dx if dx != 0 else "inf"
                if slope not in mydir:
                    mydir[slope] = 1
                mydir[slope] += 1
            res = max(res, max(mydir.values()) + same)
        return res


test = Solution()
print(test.maxPoints([Point(1, 1), Point(2, 2), Point(3, 3)]))
