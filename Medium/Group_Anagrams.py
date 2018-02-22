"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""
import collections


class Solution(object):
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        res = []
        for str in strs:
            dic[tuple(sorted(str))].append(str)
        for item in dic.values():
            res.append(item)
        return res

    def solution2(self, strs):
        res = {}
        for i in strs:
            key = tuple(sorted(i))
            if key in res:
                res[key].append(i)
            else:
                res[key] = [i]
        return list(res.values())


test = Solution()
print(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
