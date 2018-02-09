"""

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd".
We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

"""


class Solution(object):
    def __init__(self, mylist):
        self.mylist = mylist

    def group_shift(self):
        dic = {}
        for s in self.mylist:
            d = ord(s[0]) - 97
            key = tuple((ord(ch) - d) % 26 for ch in s)
            dic[key] = dic[key] + [s] if key in dic else [s]
        ans = []
        for key in dic:
            dic[key].sort()
            ans.append(dic[key])
        return ans


test = Solution(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
print(test.group_shift())
