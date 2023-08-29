from functools import lru_cache


class Solution:

    """
    Đề bài yêu cầu đếm số cách bước có thể để tiến lên n bậc thang
    Mỗi lần bước chỉ có thể bước 1 hoặc 2 bước lên n bậc thang
    Ý tưởng: Recursion, chia nhỏ bài toán
    Base: n = 1 thì 1 cách, n = 2 thì 2 cách (1 + 1 | 2)
    Dựa trên Base case ta tính toán dùng n - 1 và n - 2 để tính tổng
    E.g: f(5) = f(4) + f(3) = f(3) + f(2) + f(2) + f(1)
                            = f(2) + f(1) + f(2) + f(2) + f(1)
                            = 8
    """
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def climb(s: int) -> int:
            if s <= 2:
                return s
            ans = climb(s - 1) + climb(s - 2)
            return ans

        return climb(n)
    # Time Complexity: O(N) N -> subproblems
    # Space Complexity: O(N)


print(Solution().climbStairs(5))
