"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""
from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        if not s:
            return 0
        cnt = Counter(s)
        print(cnt)
        # print(cnt.most_common())  # is equal to sorted() method
        cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        # print(cnt)
        res = ''
        for key, val in cnt:
            res += key * val
        return res


test = Solution()
print(test.frequencySort('tree'))
