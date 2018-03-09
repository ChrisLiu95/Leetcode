"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

"""

import collections


class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        print(sorted(count.most_common(3), reverse=True))
        return [x for x, y in count.most_common(k)]


test = Solution()
print(test.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
