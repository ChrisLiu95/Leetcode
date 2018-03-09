"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes
difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1

"""


class Solution(object):
    def findMinDifference(self, timePoints):

        Tinterval = []
        for time in timePoints:
            Tinterval.append(time.split(":"))
        Tinterval = [int(x[0]) * 60 + int(x[1]) for x in Tinterval]
        Tinterval.sort()
        res = float('inf')
        for i in range(1, len(Tinterval)):
            res = min(abs(Tinterval[i] - Tinterval[i - 1]), abs(Tinterval[i - 1] + 24 * 60 - Tinterval[i]), res)
        res = min(abs(Tinterval[0] - Tinterval[len(Tinterval) - 1]),
                  abs(Tinterval[0] + 24 * 60 - Tinterval[len(Tinterval) - 1]), res)

        return res


test = Solution()
print(test.findMinDifference(["23:59", "00:00"]))
