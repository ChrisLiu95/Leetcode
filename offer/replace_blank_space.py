"""
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution(object):
    def replace(self, s):
        # 记得判断输入
        if type(s) != str:
            return
        string = list(s)
        new = []
        for char in string:
            if char == " ":
                new.append("%20")
            else:
                new.append(char)
        return "".join(new)

    def replace2(self, s):
        if type(s) != str:
            return
        return s.replace(" ", "%20")


test = Solution()
print(test.replace2("We Are Happy"))
