"""
题目：输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。例如，输入”They are students.”和”aeiou”，
则删除之后的第一个字符串变成”Thy r stdnts.”。

正则表达式?
"""


class Solution(object):
    # time: O(m*n) space: O(n)
    def deleteChar(self, s1, s2):
        dir = set(s2)
        for char in s1:
            if char in dir:
                s1 = s1.replace(char, "")
        return s1


test = Solution()
print(test.deleteChar("They are students.", "aeiou"))
