from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsMapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans = []

        def backtracking(idx: int, res: List[str], curr: str):
            if idx == len(digits):
                res.append(curr)
                return
            for char in digitsMapping[digits[idx]]:
                backtracking(idx + 1, res, curr + char)

        backtracking(0, ans, "")
        return ans
    # Time Complexity: O(N^2)
    # Space Complexity: O(N)


print(Solution().letterCombinations("23"))
