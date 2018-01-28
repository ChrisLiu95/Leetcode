# letter combination of a phone number


class Solution():

    def __init__(self):
        self.d = {
            '0': '_',
            '1': None,
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def lettercombination(self, digits):

        combinations = set()

        def recurse(test_of_world, path_so_far):

            if not test_of_world:
                combinations.add(path_so_far)
                return
            first, rest = test_of_world[0], test_of_world[1:]

            letters = self.d[first]

            for letter in letters:

                recurse(rest, path_so_far + letter)

        recurse(digits, '')
        return combinations


test = Solution()
print(test.lettercombination('23'))
