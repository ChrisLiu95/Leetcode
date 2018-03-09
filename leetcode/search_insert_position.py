"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

"""


def search_insert_position(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
        if target < array[0]:
            return 0
        elif target > array[len(array) - 1]:
            return len(array)
        else:
            if array[i] < target < array[i + 1]:
                return i + 1


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    return len([x for x in nums if x < target])


print(search_insert_position([1, 5, 7, 23], 2))
