from typing import List


class Solution:

    # Đề bài yêu cầu tính tổng của các phần tử trong hàng hiện tại
    # Dựa vào giá trị hàng trên nó
    # Ở đây ta thấy đầu và cuối mỗi hàng có giá trị luôn là 1
    # Và công thức tính giá trị của phần tử thứ 2 (hiểu là currIndex)
    # prevRow[currIndex - 1] + prevRow[currIndex]
    def generate(self, num_rows: int) -> List[List[int]]:
        pascals_triangle = [[1]]
        # By constraints 1 <= numRows <= 30
        if num_rows < 2:
            return pascals_triangle

        # Loop từ 1 bởi vì đã init giá trị cho hàng đầu tiên
        for i in range(1, num_rows):
            curr_row = [1]
            prev_row = pascals_triangle[-1]
            for j in range(1, len(prev_row)):
                curr_row.append(prev_row[j - 1] + prev_row[j])
            curr_row.append(1)
            pascals_triangle.append(curr_row)

        return pascals_triangle
    # Time Complexity: O(N^2)
    # Space Complexity: O(N)
