from functools import lru_cache
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sortedNums = sorted(nums)
        print(sortedNums)
        longestNegative = self.v1(tuple(sortedNums), True)
        longestPositive = self.v1(tuple(sortedNums))

        if longestNegative > longestPositive:
            return longestNegative
        return longestPositive

    @lru_cache(None)
    def v1(self, sortedNumsTuple: tuple, isNegative: bool = False) -> int:
        cursor = 0
        longest = 0
        tmp = 1
        for i in range(1, len(sortedNumsTuple)):
            # if isNegative and sortedNumsTuple[i] > 0:
            #     continue
            # if isNegative is False and sortedNumsTuple[i] < 0:
            #     continue
            if sortedNumsTuple[i] > sortedNumsTuple[cursor] + 1:
                if tmp > longest:
                    longest = tmp
                    tmp = 1
            elif sortedNumsTuple[i] == sortedNumsTuple[cursor] + 1:
                tmp += 1
            cursor = i
        if tmp > longest:
            longest = tmp
        return longest


print(Solution().longestConsecutive(
    [1, -8, 7, -2, -4, -4, 6, 3, -4, 0, -7, -1, 5, 1, -9, -3]

))
