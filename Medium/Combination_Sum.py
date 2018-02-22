"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]

"""


class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        candidates = sorted(candidates)

        def dfs(remain, stack):
            if remain == 0:
                print(stack)
                result.append(stack)
                return

            for item in candidates:
                if item > remain:
                    break
                if stack and item < stack[-1]:
                    print(item)
                    continue
                else:
                    dfs(remain - item, stack + [item])
        dfs(target, [])
        return result


test = Solution()
print(test.combinationSum([2, 3, 6, 7], 7))
