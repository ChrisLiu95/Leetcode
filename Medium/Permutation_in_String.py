"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""
import collections


class Solution(object):
    def checkInclusion(self, s1, s2):

        n1, n2 = len(s1), len(s2)
        need = collections.Counter(s1)
        have = collections.Counter(s2[:n1])
        for i in range(n2 - n1):
            if need == have:
                return True
            have[s2[i]] -= 1
            have[s2[i + n1]] += 1
            if not have[s2[i]]:
                del have[s2[i]]
        return need == have

    def checkInclusion2(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False


test = Solution()
print(test.checkInclusion("ab", "eidbaooo"))
