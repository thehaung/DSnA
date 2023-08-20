from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numDict = dict()
        ans = [-1] * len(nums1)

        for i, num in enumerate(nums2):
            numDict[num] = i
        for i, num in enumerate(nums1):
            for j in range(numDict[num], len(nums2)):
                if nums2[j] > num:
                    ans[i] = nums2[j]
                    break
        return ans
