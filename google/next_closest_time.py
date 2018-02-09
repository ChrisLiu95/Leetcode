"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9"
are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
"""


class Solution(object):
    def closest_time(self, current_time):
        current = 60*int(current_time[:2])+int(current_time[3:])
        digit = {int(x) for x in current_time if x != ":"}
        for cur in range(current+1, current+24*60):
            if cur > 1440:
                cur = cur-1440
            hr = int(cur/60)
            hra = int(hr/10)
            hrb = hr % 10
            mina = int((cur-hr*60)/10)
            minb = (cur-hr*60) % 10
            if hra in digit and hrb in digit and mina in digit and minb in digit:
                return "{}{}:{}{}".format(hra, hrb, mina, minb)


test = Solution()
print(test.closest_time("19:34"))
