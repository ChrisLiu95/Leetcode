"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.


"""


class Solution(object):
    # not in place
    def compress(self, chars):
        dic = {}
        res = []
        for char in chars:
            dic[char] = dic.get(char, 0) + 1
        for key, val in dic.items():
            digits = len(str(val))
            res.append(key)
            if digits == 1 and val != 1:
                res.append(str(val))
            else:
                for i in range(digits):
                    res.append(str(val)[i])
        chars = chars[:len(res)] = res
        print(chars)
        return len(res)

    def compress2(self, chars):
        left = i = 0

        while i < len(chars):
            char, length = chars[i], 1

            while i + 1 < len(chars) and chars[i + 1] == char:
                length += 1
                i += 1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left
        # in place


test = Solution()
test.compress(["a", "a", "b", "b", "c", "c", "c"])
