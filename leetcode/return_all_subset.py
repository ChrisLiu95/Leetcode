# return all the subset of a list

from itertools import combinations


class Solution(object):

    def subset(self, nums):
        result = set()

        for i in range(len(nums) + 1):
            result |= set(combinations(nums, i))  # 求并集

        return result


# test = solution0()
# print(test.subset([1, 3, 5]))


class solution1():  # without the python already-have function

    def split(self, l, index):  # this is going to return a new set without the element in index
        return tuple(x for i, x in enumerate(l) if i != index)  # i is index, where x is the item

    def subset(self, nums):

        return_set = set()

        def recurse(list_of_nums):
            if not list_of_nums:
                return
            return_set.add(tuple(list_of_nums))

            for i in range(len(list_of_nums)):

                split_list = self.split(list_of_nums, i)

                if split_list not in return_set:
                    recurse(split_list)

        recurse(nums)
        return return_set


test = Solution()
print(test.subset([1, 2, 3]))
