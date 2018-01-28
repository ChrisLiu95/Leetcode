"""

Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

collections.Counter()
http://www.pythoner.com/205.html

get(key[, default])
Return the value for key if key is in the dictionary, else default.
If default is not given, it defaults to None, so that this method never raises a KeyError.
"""
import collections


class solution(object):

    def whether_palin(self, s):
        return sum(v % 2 for v in collections.Counter(s).values()) < 2

    def canPermutePalindrome(self, s):
        dic = {}
        for item in s:
            dic[item] = dic.get(item, 0) + 1
        # return sum(v % 2 for v in dic.values()) < 2
        count1 = 0
        print(dic)
        for val in dic.values():
            if val % 2 == 1:
                count1 += 1
            if count1 > 1:
                return False
        return True


test = solution()
print(test.canPermutePalindrome("aba"))
