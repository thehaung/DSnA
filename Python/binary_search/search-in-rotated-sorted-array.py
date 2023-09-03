from typing import List


class Solution:
    """
    Đề bài yêu cầu tìm số target trong arr nums, trả về index của target trong arr nums
    Ý tưởng: Dùng Binary Search
        - Dùng std pattern khai báo các tham số left, right, mid
        - Trong trường hợp nums[mid] != target ta tiếp tục so sánh
            + Nếu nums[left] <= nums[mid] thì phía bên trái đã được sorted
                ta tiếp tục kiểm tra nums[left] <= target < nums[mid]
                (target sẽ ở trong biên độ này) không nếu có thì lui về bên trái
            + Ngược lại bên phải đã được sorted
                ta kiểm tra nums[mid] < target <= nums[right]
                (target sẽ ở trong biên độ này) không nếu có thì lui về bên phải để tìm kiếm
    """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    # Time Complexity: O(logN)
    # Space Complexity: O(1)


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 1))
