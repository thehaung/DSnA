from typing import List


class Solution:
    """
    Đề bài yêu cầu từ 1 sơ đồ cột, tính lượng nước tối đa có thể chứa
    Ý tưởng: Two Pointer
    Tính chiều ngang hiện tại bằng cách dùng right - left
    Sau đó lấy min(x, y) x là value của left, y là value của right
        để lấy mực nước tối đa có thể chứa được, ưu tiên cọc bé hơn
        nhân với chiều ngang hiện tại, sau đó so sánh với max hiện tại
        và lấy số lớn hơn và tiếp tục tìm đáp án tốt hơn
    Nếu left < right thì tiếp tục dịch chuyển về bên phải để kiểm tra
        ngược lại dịch về bên trái
    """
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0

        while left < right:
            horizontalSize = right - left
            currentArea = min(height[left], height[right]) * horizontalSize
            maxArea = max(maxArea, currentArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
    # Time Complexity: O(N)
    # Space Complexity: O(1)


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
