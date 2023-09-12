from typing import List


class Solution:
    """
    Đề bài yêu cầu merge 2 sorted array vào trong nums1
    Cho m là số lượng phần tử đang hợp lệ trong nums1 và n là số lượng phần tử hợp lệ nums2
    Ý tưởng: Two Pointer
    Maintain 2 con trỏ i và j tương đương với m và n
    Và 1 index k để chứa index của arr để insert
    Sẽ kiểm tra i và j nếu cùng đang lớn hơn 0 thì chứng tỏ vẫn có thể so sánh được
        sau khi so sánh xong thì insert vào index k và dịch sang trái
    Thoát ra khỏi vòng while thì ta chỉ cần check nums2 vì nếu nums1 còn thì hiển nhiên nó là những số bé hơn
        và hợp lệ vì đây là modify nums1 in-place theo đề bài
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        return self.raw(nums1, m, nums2, n)

    def raw(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        # Time Complexity: O(m + n)
        # Space Complexity: O(1)

    def normal(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        mergedArr = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                mergedArr.append(nums1[i])
                i += 1
            else:
                mergedArr.append(nums2[j])
                j += 1
        while i < m:
            mergedArr.append(nums1[i])
            i += 1
        while j < n:
            mergedArr.append(nums2[j])
            j += 1
        nums1 = list(mergedArr)
    # Time Complexity: O(m + n)
    # Space Complexity: O(m + n)


print(Solution().normal([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
