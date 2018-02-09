"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

str.join(sequence)
返回通过指定字符连接序列中元素后生成的新字符串。

str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );
a-b-c

!!! In Python, strings are not mutable, which means they cannot be changed.
"""


class Solution(object):
    def reverse_str(self, mystr):

        # s = mystr[::-1]
        return " ".join(mystr.split()[::-1])


test = Solution()
print(test.reverse_str("the sky is blue"))
