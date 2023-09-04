from typing import List


class Solution:

    # Đề bài cho 1 mảng các số nguyên
    # Yêu cầu trả về true
    # Nếu trong mảng tồn tại 1 giá trị tại 2 phần tử khác nhau
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            nums_set.add(nums[i])
        return False
    # Time Complexity: O(N)
    # Space Complexity: O(N)


instance = Solution()
print(instance.containsDuplicate([1, 2, 3, 1]))
