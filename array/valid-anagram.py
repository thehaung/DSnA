from functools import lru_cache


class Solution:
    # Đề bài yêu cầu kiểm tra 2 string
    # Với điều kiện các phần tử phải bằng nhau về số lượng
    # s: abca, t: acba -> a = 2, b = 1, c = 1
    # So sánh 2 string để thõa điều kiện trên
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = Solution().loadDictornary(s)
        t_dict = Solution().loadDictornary(t)

        for key, value in t_dict.items():
            if key not in s_dict or s_dict[key] != value:
                return False

        return True

    @lru_cache(None)
    def loadDictornary(self, s: str) -> dict:
        str_dict = dict()
        for element in s:
            if element in str_dict:
                str_dict[element] += 1
            else:
                str_dict[element] = 1

        return str_dict

    # Time Complexity: O(N)
    # Space Complexity: O(N)


instance = Solution()
print(instance.isAnagram("rat", "car"))
