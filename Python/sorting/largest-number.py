from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = self.mergeSort(nums, 0, len(nums) - 1)
        return str(int("".join(map(str, nums))))

    def compare(self, s1: int, s2: int) -> bool:
        return str(s1) + str(s2) > str(s2) + str(s1)

    def mergeSort(self, nums: List[int], left: int, right: int) -> List[int]:
        if left > right:
            return []
        if left == right:
            return [nums[left]]
        mid = left + (right - left) // 2
        leftNums = self.mergeSort(nums, left, mid)
        rightNums = self.mergeSort(nums, mid + 1, right)
        return self.merge(leftNums, rightNums)

    def merge(self, l1: List[int], l2: List[int]) -> List[int]:
        res, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if self.compare(l1[i], l2[j]):
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        res.extend(l1[i:] or l2[j:])
        return res


print(Solution().largestNumber([3, 30, 34, 5, 9]))
