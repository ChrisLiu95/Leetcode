# find the longest consecutive character in a given string
# 'abcddddbbba' ---> 'd'


class Solution(object):

    def __init__(self, given_str):
        self.given_str = given_str

    def longest_char(self):
        max_count = 0
        count = 0
        max_char = None
        previous = None

        for char in self.given_str:
            if char == previous:
                count += 1
            else:
                count = 1
            if count >= max_count:
                max_count = count
                max_char = char
            previous = char

        return {max_char: max_count}


test = Solution("aaaabbbcdbbbb")
print(test.longest_char())

