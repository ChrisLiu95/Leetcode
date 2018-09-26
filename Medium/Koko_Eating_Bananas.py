"""

Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.



Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23

经典二分法， 最少吃1， 最多吃max（piles） per hour

"""

import math


class Solution:
    def minEatingSpeed(self, piles, H):
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            h = 0
            for p in piles:
                h += math.ceil(p / mid)
            if h > H:
                l = mid + 1
            else:
                r = mid - 1
        return l
