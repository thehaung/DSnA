from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        ans = []
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
        ans.append("")
        for i in range(len(digits)):
            idx = digits[i]
            while len(ans[0]) == i:
                t = ans.pop(0)
                for s in digitsMapping[idx]:
                    ans.append(t + s)
        return ans
    # Time Complexity: O(N^2)
    # space Complexity: O(N)


print(Solution().letterCombinations("23"))
