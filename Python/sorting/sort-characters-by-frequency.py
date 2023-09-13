import operator


class Solution:
    def frequencySort(self, s: str) -> str:
        return self.v1Naive(s)

    def v1Naive(self, s: str) -> str:
        charMap = dict()
        for char in s:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
        sortedCharMap = sorted(charMap.items(), key=operator.itemgetter(1), reverse=True)
        res = ""
        for item in sortedCharMap[:len(s)]:
            res += "".join(item[0] for _ in range(item[1]))
        return res


print(Solution().frequencySort("aaaAcc"))
