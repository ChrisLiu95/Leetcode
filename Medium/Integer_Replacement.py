"""

Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
Idea:
If n is even, obviously do >> 1.
If n is odd,
If n+1 has more leading zeros, do n + 1. Otherwise, do n - 1.

Here, the one with more leading zeros actually implies it has fewer ones and can be applied by >> 1 more times than n - 1.

n = 3 is a special case and we do n - 1.

example   9: 1001 if n is odd, find the second last digit, if it is 0, n-1; else n+1
and case n==3 is a special case, which should be treated differently.

"""


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0

        while n != 1:
            if n & 1 == 0:
                n = n >> 1
            elif n & 2 == 0 or n == 3:
                n -= 1
            else:
                n += 1
            res += 1

        return res
