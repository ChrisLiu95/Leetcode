"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

"""


class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = [int(v) for v in version1.split(".")]
        v2 = [int(v) for v in version2.split(".")]

        for i in range(max(len(v1), len(v2))):
            temp1 = v1[i] if i < len(v1) else 0
            temp2 = v2[i] if i < len(v2) else 0
            if temp1 > temp2:
                return 1
            elif temp1 < temp2:
                return -1
        return 0
