"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number
is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

"""


class Solution(object):
    # slow
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        while k > 0:
            k -= 1
            i = 0
            while i < len(num) - 1:
                if num[i] > num[i + 1]:
                    break
                i += 1
            num = num[:i] + num[i + 1:]

        if not num:
            return "0"
        return str(int(num))

    # much faster
    def removeKdigits2(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        n = len(num)
        i = 0
        while i < n:
            while k > 0 and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        while k > 0:
            stack.pop()
            k -= 1
        while len(stack) > 1 and stack[0] == '0':
            stack.pop(0)
        if not stack:
            return '0'
        return ''.join(stack)
