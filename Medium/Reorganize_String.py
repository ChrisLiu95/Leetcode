"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other
are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""

1.Sort the letters in the string by their frequency. (I used Counter of python.)
2.Create the piles as many as the max frequency.
3.Put the letter one by one from the sorted string onto the piles with cyclic order.
4.Finally, concatenate the letters in each pile.

"""

from collections import Counter


class Solution(object):
    def reorganizeString(self, S):
        count = Counter(S)
        mylist = count.most_common()
        _, maxfreq = mylist[0]

        if maxfreq > (len(S) + 1) // 2:
            return ""
        else:
            res = [[] for _ in range(maxfreq)]
            start = 0
            for char, freq in mylist:
                for i in range(freq):
                    res[(i + start) % maxfreq].append(char)
                start += freq
            return "".join("".join(temp) for temp in res)
