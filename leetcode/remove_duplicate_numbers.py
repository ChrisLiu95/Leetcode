"""
Given a sorted array, remove the duplicates in place such that each element appear only once and
 return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
"""
# use filter function


class Solution(object):
    def __init__(self, array):
        self.array = array

    def remove_duplicate(self):
        my_dir = []
        count = 0
        for i in range(len(self.array)):
            if self.array[i] in my_dir:
                count += 1
                self.array[i] = 0
            else:
                my_dir.append(self.array[i])
        while 0 in self.array:
            self.array.remove(0)

        return self.array, len(self.array)-count


test = Solution([1, 3, 3, 4, 4, 5])
print(test.remove_duplicate())
