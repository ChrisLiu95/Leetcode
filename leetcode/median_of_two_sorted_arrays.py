"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

"""

# stupid solution


class Solution(object):
    def __init__(self, arrayA, arrayB):
        self.arrayA = arrayA
        self.arrayB = arrayB

    def median_of_arrays(self):
        new_array = []
        for item in self.arrayA:
            new_array.append(item)
        for item in self.arrayB:
            new_array.append(item)
        new_array.sort()
        length = len(new_array)

        if length % 2 == 0:
            return (new_array[int(length/2)]+new_array[int(length/2)-1])/2
        else:
            return new_array[int((length-1)/2)]


test = Solution([1, 3], [2, 4])
print(test.median_of_arrays())
