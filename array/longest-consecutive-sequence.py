from typing import List


class Solution:
    """
        Đề bài yêu cầu xác định length của dãy số liên tiếp lớn nhất
        Ý tưởng: Lưu list num vào trong 1 set để đảm bảo unique
        Sau đó nếu num - 1 không nằm trong numSet thì num hiện tại là head
        Nếu longest đang kiểm tra đã lớn hơn nums.length / 2
        Thì đây là length lớn nhất
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        longest = 1
        for _, num in enumerate(nums):
            if num - 1 not in numSet:
                count = 1
                # logN time execution
                while num + 1 in numSet:
                    num += 1
                    count += 1
                longest = max(longest, count)
            if longest > len(nums) / 2:
                break
        return longest

    # Time Complexity: O(NlogN)
    # Space Complexiy: O(N)
