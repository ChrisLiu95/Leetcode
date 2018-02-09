# return the first recurring character of a given string
# example 'ABCA' --> 'A'  'ABC'--> None


class Solution(object):

    def __init__(self, given_str):
        self.given_str = given_str

    def return_first_character(self):
        my_hush = {}
        for char in self.given_str:
            if char in my_hush:
                return char
            else:
                my_hush[char] = 1

        return None


test = Solution('ABCbcB')
print(test.return_first_character())
