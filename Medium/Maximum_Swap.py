"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
 Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.

"""


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        ss = list(str(num))

        # 10909091  90909011   90109091
        for i in range(len(ss)):
            index = 0
            tempM = ss[i]
            for j in range(i + 1, len(ss)):
                if ss[j] >= tempM:
                    tempM = ss[j]
                    index = j

            if index != 0 and tempM != ss[i]:
                ss[index] = ss[i]
                ss[i] = tempM
                return int("".join(ss))
        return num


test = Solution()
print(test.maximumSwap(10909091))
