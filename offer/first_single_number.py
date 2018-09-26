"""
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
"""


class Solution(object):
    def find_first(self, s):
        mydir = {}
        mylist = list(s)

        for char in s:
            mydir[char] = mydir.get(char, 0) + 1
        # print(mydir)
        for char in mylist:
            if mydir[char] == 1:
                return char
        return -1


test = Solution()
print(test.find_first('abaccdeff'))
