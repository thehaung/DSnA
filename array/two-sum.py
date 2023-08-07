from typing import List


class Solution:
    # Đề bài yêu cầu với 1 mảng cho trước và 1 target
    # Kiểm tra tổng của 2 phần tử trong mảng có bằng target không
    # Nếu có thì return index của 2 phần tử thỏa mãn
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [] * 2
        nums_dict = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in nums_dict:
                ans.append(nums_dict[target - nums[i]])
                ans.append(i)
                return ans
            else:
                nums_dict[nums[i]] = i

        return ans

    # Time Complexity: O(N)
    # Space Complexity: O(N)
