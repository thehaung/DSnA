from typing import List
import operator


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        numMap = dict()
        for _, num in enumerate(nums):
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1
        sortedNums = sorted(
            numMap.items(), key=operator.itemgetter(1), reverse=True)
        return [item[0] for item in sortedNums[:k]]
