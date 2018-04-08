"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of
 largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.


"""


class Solution(object):
    # brute force (LTE)
    def largestRectangleArea(self, heights):
        if not heights:
            return 0

        # brute force
        res = 0
        for i in range(len(heights)):
            left, right = i, i
            while left > 0 and heights[left - 1] >= heights[i]:
                left -= 1
            while right < len(heights) - 1 and heights[right + 1] >= heights[i]:
                right += 1
            res = max((right - left + 1) * heights[i], res)
        return res

    def largestRectangleArea2(self, heights):
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans
