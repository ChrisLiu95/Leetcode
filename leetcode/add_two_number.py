"""
You are given two non-empty linked lists representing two non-negative integers. The digits
 are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and
  return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)  // 342+465 = 807
Output: 7 -> 0 -> 8

"""


class Solution(object):

    def __init__(self, arrayA, arrayB):
        self.arrayA = arrayA
        self.arrayB = arrayB

    def add_two_number(self):
        length = len(self.arrayA)
        carry = 0
        new_array = [0 for _ in range(length)]
        for i in range(length):
            temp = self.arrayA[i] + self.arrayB[i] + carry
            if temp >= 10:
                carry = 1
                new_array[i] = temp % 10
            else:
                carry = 0
                new_array[i] = temp
        if carry == 1:
            new_array.append(1)
        return new_array


test = Solution([2, 4, 8], [5, 6, 4])
print(test.add_two_number())
