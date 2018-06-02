"""

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

101 & 110 & 111 = 100
Example 2:

Input: [0,1]
Output: 0


explanation:

First let's think what does bitwise AND do to two numbers, for example ( 0b means base 2)

4 & 7 = 0b100 & 0b111 = 0b100
5 & 7 = 0b101 & 0b111 = 0b101
5 & 6 = 0b101 & 0b110 = 0b100
The operator & is keeping those bits which is set in both number.

For several numbers, the operator & is keeping those bits which is 1 in every number.

In other word, a bit is 0 in any number will result in 0 in the answer's corresponding bit.

Now consider a range

[m = 0bxyz0acd, n=0bxyz1rst]
here xyzpacdrst all are digits in base 2.

We can find two numbers that are special in the range [m, n]

(1) m' = 0bxyz0111
(2) n' = 0bxyz1000
The bitwise AND of all the numbers in range [m, n] is just the bitwise AND of the two special number

rangeBitwiseAnd(m, n) = m' & n' = 0bxyz0000

This tells us, the bitwise and of the range is keeping the common bits of m and n from left to right until the
first bit that they are different, padding zeros for the rest. ！！
"""


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 只要其中一位为0，结果该位必为零， 因为与（&） 运算
        if m == 0:
            return 0
        i = 0

        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i
