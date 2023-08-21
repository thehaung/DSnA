from functools import lru_cache


class Solution:
    # Đề bài yêu cầu kiểm tra 2 string
    # Với điều kiện các phần tử phải bằng nhau về số lượng
    # s: abca, t: acba -> a = 2, b = 1, c = 1
    # So sánh 2 string để thõa điều kiện trên
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.v1(s, t)

    def v2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    # Time Complexity: O(N * logN)
    # Space Complexity: O(N)

    def v1(self, s: str, t: str) -> bool:
        s_dict = self.strDictornary(s)
        t_dict = self.strDictornary(t)
        return s_dict == t_dict
    # Time Complexity: O(N)
    # Space Complexity: O(N)

    @lru_cache(None)
    def strDictornary(self, s: str) -> dict:
        str_dict = dict()
        for element in s:
            if element in str_dict:
                str_dict[element] += 1
            else:
                str_dict[element] = 1

        return str_dict
    # Time Complexity: O(N)
    # Space Complexity: O(N)
