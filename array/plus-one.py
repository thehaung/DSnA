from typing import List

class Solution:
    
    # Đề bài yêu cầu +1 giá trị vào phần tử cuối trong mảng
    # Nếu phần tử cuối +1 = 10 thì overwrite giá trị cho phần tử là 0
    # Tiếp tục dịch chuyển lên phần tử trước nó tiếp tục cộng cho tới khi phần tử được cộng thêm 1 < 9
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            
        digits.insert(0, 1)
        return digits

    # Time Complexity: O(N)
    # Space Complexity: O(1)