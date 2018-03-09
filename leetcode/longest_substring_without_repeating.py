"""
Given a string, find the length of the longest substring without repeating characters.
Given "abcabcbb",the answer is "abc", which the length is 3.

"""


class Solution(object):
    def __init__(self, given_string):
        self.given_string = given_string

    def longest_non_repeating_string(self):
        my_dir = []
        Max_count = 0
        count = 0
        for char in self.given_string:
            if char in my_dir:
                if count > Max_count:
                    Max_count = count
                count = 1
                my_dir.clear()
                my_dir.append(char)
            else:
                my_dir.append(char)
                count += 1

        return Max_count

    def solution2(self):

        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i

        return max_length


test = Solution('abcdeefabcbb')
print(test.longest_non_repeating_string())
