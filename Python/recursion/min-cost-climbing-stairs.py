from functools import lru_cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.v2CalcViaLoop(cost)

    def v1Recursion(self, cost: List[int]) -> int:
        @lru_cache(None)
        def calcCost(index: int):
            if index >= len(cost):
                return 0
            take1Step = calcCost(index + 1)
            take2Step = calcCost(index + 2)
            return min(take1Step, take2Step) + cost[index]

        startIndex0 = calcCost(0)
        startIndex1 = calcCost(1)
        return min(startIndex0, startIndex1)

    def v2CalcViaLoop(self, cost: List[int]) -> int:
        s1, s2 = 0, 0
        for i in range(2, len(cost)):
            temp = min(s1 + cost[i - 2], s2 + cost[i - 1])
            s1, s2 = s2, temp
        return s2


print(Solution().minCostClimbingStairs([10, 15, 20]))
