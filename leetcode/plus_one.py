# input an array like [1,2,3,4]
# output an array like [1,2,3,5] 1234+1=1235
# [1,2,9,9] --> [1,3,0,0] ; [9,9]-->[1,0,0]


class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def plus_one(self):

        length = len(self.nums)
        carry = 1
        new_array = [0]*length  # [0 for x in range(length)]

        for i in range(length-1, -1, -1):
            temp = self.nums[i] + carry
            if temp == 10:
                carry = 1
            else:
                carry = 0
            new_array[i] = temp % 10
        if carry == 1:
            new_array = [0]*(length+1)
            new_array[0] = 1

        return new_array


test = Solution([9, 9, 9])
print(test.plus_one())

