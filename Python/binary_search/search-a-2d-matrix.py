from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.v1Naive(matrix, target)

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


print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0))
