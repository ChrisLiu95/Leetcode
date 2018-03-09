"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".


Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0

"""


class Solution(object):
    def find_jewels(self, j, s):
        mydir = []
        res = 0
        for jewel in j:
            mydir.append(jewel)
        for stone in s:
            if stone in mydir:
                res += 1
        return res

