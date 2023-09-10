from typing import List


class Solution:
    """
    Đề bài yêu cầu tìm ra mảng con có tổng lớn nhất trong arr nums
    Ý tưởng: Maintain 1 pointer
    Initial biến maxSum và currentSum nums[0]
    Khi loop qua mỗi phần tử, ta kiểm tra num hiện tại có lớn hơn currentSum không
    Sau đó sẽ kiểm tra maxSum và overwrite giá trị
    """
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]
        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum
    # Time Complexity: O(N)
    # Space Complexity: O(1)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
