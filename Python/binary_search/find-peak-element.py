from typing import List


class Solution:
    """
    Đề bài yêu cầu trả về bất cứ index nào trong arr nums thoả mãn condition sau
    1. Nếu arr len == 1 return index
    2. Nếu arr len == 2 return bigger number index [2, 1] -> 0
    3. Nếu arr len > 2 thì kiểm tra điều kiện value của index phải lớn hơn index neighbor (hàng xóm)
        là index - 1 và index + 1

    Ý tưởng: Binary Search
    Nếu như phần tử bên phải mà lớn hơn phần tử bên trái, tiếp tục tìm bên phải để tìm peak
        ngược lại tìm bên trái
    Nếu như tìm kiếm không thoả mãn điều kiện thì ta trả về left hoặc right đều được
        vì lúc này nó đã chiếu đến peak element (beak while condition then left == right)
    """

    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            if nums[mid] > nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
        return left
    # Time Complexity: O(logN)
    # Space Complexity: O(1)


print(Solution().findPeakElement([3, 5, 6, 4, 3, 1, 1]))
