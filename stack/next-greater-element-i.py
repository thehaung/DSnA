from typing import List


class Solution:
    # Đề bài yêu cầu tìm phần tử lớn hơn tiếp theo cuả num in nums1 ở nums2
    # Ý tưởng: Dùng dict để lưu lại key pair, value & value lớn hơn của nó
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreatest = dict()
        stack = []

        # Loop qua nums2, kiểm tra stack.peek() < num hiện tại
        # Thì put value vào dict
        # Nếu stack empty thì push num vào stack
        for _, num in enumerate(nums2):
            while stack and stack[-1] < num:
                nextGreatest[stack.pop()] = num
            stack.append(num)

        # Kiểm tra số trong nums1 có ở trong dict không
        # Nếu có thì set ngược kết quả vào nums1[i] không thì def -1
        for i in range(len(nums1)):
            nums1[i] = nextGreatest.get(nums1[i], -1)
        return nums1
    # Time Complexity: O(N^2)
    # Space Complexity: O(N)
