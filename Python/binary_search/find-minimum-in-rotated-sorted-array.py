from typing import List


class Solution:
    """
    Đề bài yêu cầu tìm min trong 1 arr đã được sorted and rotated n times
    Ý tưởng: Binary Search
    Ở đây ta thấy phải thoả điều kiện này nums[i] < nums[i - 1] && nums[i] < nums[i + 1ư
    Nếu như mid đang ở biên left or right thì điều kiện còn lại phải đúng
    """
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (mid == left or nums[mid - 1] > nums[mid]) and (mid == right or nums[mid] < nums[mid + 1]):
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    # Time Complexity: O(logN)
    # Space Complexity: O(1)
