# top k frequent elements
# given a none empty array of integers and return the K most frequent elements
# for example, given [1,1,1,1,2,2,2,3,3], K=2, return [1,2]

from collections import Counter


class solution():

    def topKfrequent(self, nums, k):

        counted = Counter(nums)

        most_common_element = counted.most_common(k)

        return_set = set()
        for x in most_common_element:
            return_set.add(x[0])
        return return_set


test = solution()
print(test.topKfrequent([1, 1, 1, 2, 2, 3, 3, 3, 3], 2))

