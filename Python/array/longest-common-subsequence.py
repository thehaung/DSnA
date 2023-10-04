class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        count = 0
        text1Map = dict()
        for char in text1:
            text1Map[char] = text1Map.get(char, 0) + 1
        text2Map = dict()
        for char in text2:
            text2Map[char] = text2Map.get(char, 0) + 1

        for text in text2Map:
            if text in text1Map:
                count += text1Map[text] if text2Map[text] < text1Map[text] else text2Map[text]
        return count


print(Solution().longestCommonSubsequence("abcde", "ace"))
