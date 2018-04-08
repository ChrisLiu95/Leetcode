"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

"""


class Solution(object):
    def getRow(self, rowIndex):
        def cal(k, index):
            temp1 = 1
            temp2 = 1
            for i in range(k - index + 1, k + 1):
                temp1 *= i
            for i in range(1, index + 1):
                temp2 *= i
            return temp1 // temp2

        res = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            res[i] = cal(rowIndex, i)
        return res


test = Solution()
print(test.getRow(3))
