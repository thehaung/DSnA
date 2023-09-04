from bisect import bisect_right
from typing import List


class Solution:
    """
    Đề bài cho 1 list sorted arr, và target number
    Dựa vào target number ta phải kiểm tra sum của 2 index trong arr bằng với target
    Ý tưởng: Binary Search
    Loop qua từng num trong arr numbers, sau đó init left, right
        và tmp, tmp là target để tìm trong mảng con dùng Binary Search
    P/s: Bài yêu cầu trả ra kết quả với index + 1 [0, 1] target = 1 -> [1, 2]
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    left = mid + 1
                else:
                    right = mid - 1
    # Time Complexity: O(NlogN)
    # Space Complexity: O(1)


print(Solution().twoSum([2, 3, 4], 6))
