from functools import lru_cache
from typing import List


class Solution:
    """
    Đề bài yêu cầu tính cost dựa trên 1 nums array
    Với mỗi lần bước ta có thể take 1 or 2 steps
    Cost sẽ được cộng dồn với những ô (tương ứng với index)
    mà ta bước qua

    Ý tưởng: Ta sẽ có 2 biến tính toán, cho bước 1 bước và 2 bước khởi đầu
    Mỗi lần bước qua 1 hoặc 2 bước ta sẽ tính min của 2 lần bước
    Và sau đó trả ra min cost sau n lần bước
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.v2CalcViaLoop(cost)

    def v1Recursion(self, cost: List[int]) -> int:
        @lru_cache(None)
        def calcCost(index: int) -> int:
            if index >= len(cost):
                return 0
            take1Step = calcCost(index + 1)
            take2Step = calcCost(index + 2)
            return min(take1Step, take2Step) + cost[index]

        startIndex0 = calcCost(0)
        startIndex1 = calcCost(1)
        return min(startIndex0, startIndex1)
    # Time Complexity: O(N)
    # Space Complexity: O(N)

    def v2CalcViaLoop(self, cost: List[int]) -> int:
        s1, s2 = 0, 0
        for i in range(2, len(cost)):
            temp = min(s1 + cost[i - 2], s2 + cost[i - 1])
            s1, s2 = s2, temp
        return s2
    # Time Complexity: O(N)
    # Space Complexity: O(N)


print(Solution().minCostClimbingStairs([10, 15, 20]))
