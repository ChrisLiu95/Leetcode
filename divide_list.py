"""
一年半之前，我遇到一个问题：把一堆数平均分成N份，保证每一份的和接近于所有数之和除以N，

不要求平分以后的每份数据个数相等。这是有现实的程序设计需求的，当时是3份。首先想到要先进行排序，
再依次从已排序的数列中抽取，
 let's say, N = 3
"""


class Solution(object):
    def divideList(self, l, n):
        res = [[] for _ in range(n)]

        l.sort()
        # print(l)
        for num in l:
            temp = float("inf")
            index = 0
            for i in range(n):
                tempS = sum(res[i])
                if tempS < temp:
                    temp = tempS
                    index = i
            print(index)
            res[index].append(num)
        return res


test = Solution()
print(test.divideList([1, 3, 4, 5, 3, 4, 1, 2, 4, 6, 7, 0, 9, 2, 1], 4))
