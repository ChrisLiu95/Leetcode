"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

notice that only "69" , "11" "00", "96" "88" look same when rotated 180 degrees
"""


class Solution(object):
    def __init__(self, num):
        self.num = str(num)

    def judge(self):
        mymap = {("0", "0"), ("1", "1"), ("8", "8"), ("9", "6"), ("6", "9")}
        j, k = 0, len(self.num)-1
        while j <= k:
            if (self.num[j], self.num[k]) not in mymap:
                return False
            j, k = j+1, k-1
        return True


test = Solution(6969)
print(test.judge())

