"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this:
"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s.
In particular, your input is the string p and you need to output the number of different non-empty substrings of p in
the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.

"""


# zabc: single char: z,a,b,c double: za,ab,bc tripple: zab,abc, quadra: zabc, thus 1+2+3+4= 10，
# based on this idea, dir[ord[char]] means the numbers of substring ends by such char.
class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        mydir = {}
        cnt = 0

        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i - 1]) - ord(p[i]) == 25):
                cnt += 1
            else:
                cnt = 1
            mydir[p[i]] = max(mydir.get(p[i], 0), cnt)

        return sum(mydir.values())
