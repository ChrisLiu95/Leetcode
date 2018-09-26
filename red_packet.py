import random


class Solution(object):
    def redPacket(self, num, money):
        res = []
        people = num

        for i in range(num):
            people -= 1
            temp = 0
            if people > 0:
                temp = random.randint(1, money - people)
                res.append(temp / 100)
            else:
                res.append(money / 100)
            money -= temp
        return res

    def redPacket2(self, nums, money):
        res = []
        for i in range(nums):
            res.append(random.random())
        res = [i / sum(res) * money / 100 for i in res]
        return res


test = Solution()
print(test.redPacket2(5, 500))
