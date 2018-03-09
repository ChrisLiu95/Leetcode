# basic binary_search for a sorted list nums
"""
Binary Search is one of the most fundamental and useful algorithms in Computer Science.
It describes the process of searching for a specific value in an ordered collection.

Binary Search is generally composed of 3 main sections:

Pre-processing - Sort if collection is unsorted.

Binary Search - Using a loop or recursion to divide search space in half after each comparison.

Post-processing - Determine viable candidates in the remaining space.

O（logn）
"""


def binary_search(nums, target):
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    nums = [1, 3, 2, 4, 5]
    print(binary_search(nums, 5))


main()
