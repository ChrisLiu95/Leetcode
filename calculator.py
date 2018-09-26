"""
“1+2*3*3+2”

"""


class Solution(object):
    def cal(self, str):
        index = -1
        for i in range(len(str) - 1, -1, -1):
            if str[i] == "+" or str[i] == "-":
                index = i
                break
        if index == -1:
            total = int(str[0])
            for i in range(1, len(str), 2):
                sign = str[i]
                num = int(str[i + 1])
                if sign == "*":
                    total *= num
                elif sign == "/":
                    total /= num
            return total

        else:
            if str[index] == "+":
                return self.cal(str[:index]) + self.cal(str[index + 1:])
            elif str[index] == "-":
                return self.cal(str[:index]) - self.cal(str[index + 1:])


test = Solution()
print(test.cal("1+2*3*3+2"))
