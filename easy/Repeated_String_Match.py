"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.

"""


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # C = ""
        # for i in range(len(B)/len(A) + 3):
        #     if B in C:
        #         return i
        #     C += A
        # return -1

        if len(set(B)) > len(set(A)):
            return -1
        k = len(B) // len(A)
        if B in A * k:
            return k
        elif B in A * (k + 1):
            return k + 1
        elif B in A * (k + 2):
            return k + 2
        return -1
