"""
Given two sentences words1, words2 (each represented as an array of strings),
and a list of similar word pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the
similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is not transitive. For example,
if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good"
are not necessarily similar.

However, similarity is symmetric. For example, "great" and "fine" being similar is the
same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"],
words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence
 like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

"""


class Solution(object):
    def sentence_similarity(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        mypairs = set(map(tuple, pairs))
        for x, y in zip(words1, words2):
            if x == y or (x, y) in mypairs or (y, x) in mypairs:
                pass
            else:
                return False
        return True

    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2): return False

        pairset = set(map(tuple, pairs))
        return all(w1 == w2 or (w1, w2) in pairset or (w2, w1) in pairset for w1, w2 in zip(words1, words2))


test = Solution()
print(test.sentence_similarity(["great", "acting", "skills", "lalala"], ["fine", "drama", "talent", "lalala"],
                               [["fine", "great"], ["acting", "drama"], ["skills", "talent"]]))
