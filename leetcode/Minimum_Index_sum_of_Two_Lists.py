"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite
restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is
a choice tie between answers, output all of them with no order requirement. You could assume there
always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

"""


class Solution(object):
    def min_index(self, l, m):
        dic1 = {v: i for i, v in enumerate(l)}
        best, res = 1e9, []
        for i, v in enumerate(m):
            if v in dic1:
                if i + dic1[v] < best:
                    best = i + dic1[v]
                    res = [v]
                elif i + dic1[v] == best:
                    res.append(v)
        return res


test = Solution()
print(test.min_index(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                     ["KFC", "Shogun", "Burger King"]))
