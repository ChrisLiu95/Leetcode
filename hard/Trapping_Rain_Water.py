"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        leftwall, rightwall = 0, 0
        res = 0

        maxh = max(height)
        index = height.index(maxh)

        while left < index:
            if height[left] < leftwall:
                res += leftwall - height[left]
            else:
                leftwall = height[left]
            left += 1

        while right > index:
            if height[right] < rightwall:
                res += rightwall - height[right]
            else:
                rightwall = height[right]
            right -= 1

        return res
