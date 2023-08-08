from typing import List


class Solution:
    # Đề bài yêu cầu với 1 mảng cho trước và 1 target
    # Kiểm tra tổng của 2 phần tử trong mảng có bằng target không
    # Nếu có thì return index của 2 phần tử thỏa mãn
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in nums_dict:
                return [nums_dict[target - nums[i]], i]
            else:
                nums_dict[nums[i]] = i

    # Time Complexity: O(N)
    # Space Complexity: O(N)
