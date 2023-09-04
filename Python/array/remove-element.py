from typing import List


class Solution:

    # Đề bài yêu cầu dịch chuyển các phần tử có value khác val về đầu của mảng
    # Trả về số lượng phần tử có giá trị != val
    # nums[:p] chỉ bao gồm những số hợp lệ còn lại trong mảng nums
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        # Khi nums[i] != val thì overwrite nums[p] = nums[i]
        # Để dịch chuyển giá trị hợp lệ lên đầu mảng
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        return p

    # Time Complexity: O(N)
    # Space Complexity: O(1)


instance = Solution()
print(instance.removeElement([1, 2, 2, 1], 1))
