# google interview question, judge whether a number is the power of two
# tricks: if the number is the power of 2, then (num & num-1) == 0


class Solution(object):

    def __init__(self, num):
        self.num = num

    def power_of_two(self):
        if self.num & (self.num-1) == 0:
            return True
        return False


test = Solution(64)
print(test.power_of_two())
