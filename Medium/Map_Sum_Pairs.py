"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""


class MapSum(object):
    def startWithPrefix(self, pre, word):
        i, j = len(pre), len(word)
        k = 0
        if i > j:
            return False
        while k < i:
            if pre[k] != word[k]:
                return False
            k += 1
        return True

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dir = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dir[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return sum(self.dir[i] for i in self.dir.keys() if self.startWithPrefix(prefix, i))

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
