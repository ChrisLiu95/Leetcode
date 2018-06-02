"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

"""


class Solution(object):
    # LTE slow
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res += self.hammingdistance(nums[i], nums[j])
        return res

    def hammingdistance(self, x, y):
        return bin(x ^ y).count("1")

    def totalHammingDistance2(self, nums):
        hasOne = 1
        res = 0

        while hasOne:
            hasOne = 0
            cnt0 = 0
            cnt1 = 0

            for i in range(len(nums)):
                if nums[i]:
                    hasOne = 1
                if nums[i] % 2:
                    cnt1 += 1
                else:
                    cnt0 += 1
                nums[i] >>= 1
            res += cnt0 * cnt1
        return res


test = Solution()
print(test.totalHammingDistance([4, 14, 2]))
