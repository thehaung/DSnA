from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        for i in range(len(digits)):
            for char in digitsMapping[digits[i]]:
                ans.append(char)

        for i in range(len(ans)):
            for j in range(1, len(ans)):
                if i != j:
                    ans[i] = ans[i] + ans[j]
                    break

        return ans


print(Solution().letterCombinations("23"))


def test():
    tes1 = ['a', 'b', 'c', 'd', 'e', 'f']
    for i in range(len(tes1)):
        tes1[i] = tes1[i] + '1'

    print(tes1)


# print(test())
