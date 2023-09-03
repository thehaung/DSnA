from typing import List


class Solution:
    """
    Đề bài yêu cầu từ 1 matrix được biểu diễn trên List of List có tính monotonic
        List[n] tăng thì List[n][m] tăng find target number
    Ý tưởng: Binary Search
    Có 2 cách tiếp cận nhưng vẫn base trên BS
    1. Loop qua matrix sau đó với mỗi matrix ta dùng BS để tìm target
    2. Ta có right = len(matrix) * len(matrix[0]) (cho là n số lượng phần tử của 1 matrix[i])
        sau đó để tìm ra midRow và midCol dựa vào mid và n ta dùng divmod -> (mid//n, mid%n)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.v2Better(matrix, target)

    def v1Naive(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i]) - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
    # Time Complexity: O(N * logN)
    # Space Complexity: O(N)

    def v2Better(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            midRow, midCol = divmod(mid, n)
            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
    # Time Complexity: O(log(M * N))
    # Space Complexity: O(1)


print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 30))
