from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        current_solution = []

        def backtrack(remain: int, nex: int):
            # solution found
            if remain == 0:
                ans.append(current_solution.copy())
            else:
                # iterate through all possible candidates
                for i in range(nex, n + 1):
                    # add candidate
                    current_solution.append(i)
                    # backtrack
                    backtrack(remain - 1, i + 1)
                    # remove candidate
                    current_solution.pop()

        backtrack(k, 1)
        return ans


print(Solution().combine(4, 2))
