class Solution:
    """
    Đề bài yêu cầu kiểm tra xem nums có phải là 1 perfect square không
    Ý tưởng: Dùng Binary Search
    Ở đây ta chỉ kiểm tra trên số nguyên nên sẽ chia nguyên để tính mid
    """

    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        if num == 1:
            return True

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
    # Time Complexity: O(logN)
    # Space Complexity: O(1)
