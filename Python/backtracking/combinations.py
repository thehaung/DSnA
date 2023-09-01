from typing import List


class Solution:
    """
    Đề bài yêu cầu combine các số dựa trên n và k
    n là max của số e.g: n = 4 thì số lớn nhất trong combine sẽ là 4
    k là max của độ dài số sau khi combine e.g: k = 2 thì 1 số
    chỉ được có tối đa 2 phần tử combine ví dụ [14]

    Ý tưởng: Dùng backtracking để combine
    Func backtrack sẽ nhận vào remain và nex
    remain được tính dựa trên số k
    nex sẽ được tính dựa trên loop range (init num, n + 1)
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        current_solution = []

        def backtrack(remain: int, nex: int):
            # base case
            if remain == 0:
                ans.append(current_solution.copy())
            else:
                # iterate through all possible candidates
                for i in range(nex, n + 1):
                    current_solution.append(i)
                    backtrack(remain - 1, i + 1)
                    current_solution.pop()

        backtrack(k, 1)
        return ans


print(Solution().combine(4, 2))
