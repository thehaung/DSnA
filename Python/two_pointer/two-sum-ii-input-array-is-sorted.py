from typing import List


class Solution:
    """
    Đề bài cho 1 list sorted arr, và target number
    Dựa vào target number ta phải kiểm tra sum của 2 index trong arr bằng với target
    Ý tưởng: Two Pointer
    Init left, right và cộng giá trị lại, nếu bằng target thì return ans
    Vì đã được sorted nên khi sum lớn hơn target thì ta dịch về bên trái để kiểm tra
        ngược lại thì dịch về bên phải
    P/s: Bài yêu cầu trả ra kết quả với index + 1 [0, 1] target = 1 -> [1, 2]
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sumNum = numbers[left] + numbers[right]
            if sumNum == target:
                return [left + 1, right + 1]
            elif sumNum > target:
                right -= 1
            else:
                left += 1
    # Time Complexity: O(N)
    # Space Complexity: O(1)
