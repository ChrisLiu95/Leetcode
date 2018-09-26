"""
题目大约如下:所有的同学都站在坐标系上的整数点,由原点看每个点,有的点被视线挡住了,
求(长度为N时)原点能看到多少点,如下图所示:比如N = 1时 输出3; N=2时 输出5; N=3时 输出9; N = 4时,输出13?我应该没有算错吧.

"""


class Solution(object):
    def visiblepoints(self, n):
        res = set()
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                res.add(j / i)
        return len(res) + 2


test = Solution()
print(test.visiblepoints(4))
