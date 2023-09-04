from typing import List


class Solution:

    # Đề bài yêu cầu từ mảng đã cho tính
    # Với giá trị của ans[i] bằng với tích của các phần tử còn lại
    # Ý tưởng sẽ là dùng prefix và postfix cho mảng sau [1, 2, 3, 4]
    # Nếu muốn tính nums[2] -> nums[2] = (nums[0] * nums[1]) * nums[3]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        # Giá trị phần tử đầu tiên (prefix) và cuối cùng (postfix) phải là 1
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    # Note -> Nếu như theo đề bài Follow up: Can you solve the problem in O(1)
    # extra space complexity? (The output array does not count as
    # extra space for space complexity analysis.)
    # Thì Space Complexity của bài này là O(1)


instance = Solution()
print(instance.productExceptSelf([1, 2, 3, 4]))
