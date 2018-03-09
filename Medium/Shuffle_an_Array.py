"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must
equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();


"""
from random import randint


class Solution(object):

    def __init__(self, nums):
        self.nums = nums
        self.res = [num for num in nums]

    def reset(self):
        return self.nums

    def shuffle(self):
        for i in range(len(self.nums)):
            rand = randint(0, len(self.nums) - 1)
            self.res[i], self.res[rand] = self.res[rand], self.res[i]
        return self.res
