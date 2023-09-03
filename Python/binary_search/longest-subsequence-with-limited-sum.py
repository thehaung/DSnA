from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
    """
    Đề bài yêu cầu dựa vào arr nums có n phần tử và arr queries có m phần tử
    Trả về 1 arr ans với m phần tử là đáp án yêu cầu
    Với mỗi phần tử trong arr queries ta phải kiểm tra xem nó có thể
        có bao nhiêu phần tử con trong arr nums mà tổng của số phần tử con <= phần tử đang query

    Ý tưởng: Có 2 cách
        - Prefix sum sau đó loop qua queries kiểm tra nếu queries >= phần tử prefixSum
            thì tiếp tục kiểm tra tiếp ngược lại thì break
        - Prefix sum sau đó dùng bisect_right để kiểm tra để tìm ra vị trí chèn phải
            với điều kiện >= target query
    """

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        return self.v1PrefixSum(nums, queries)

    def v1PrefixSum(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        prefixSum = list(accumulate(sorted(nums)))

        ans = [0] * m
        for i in range(m):
            for j in range(n):
                if prefixSum[j] <= queries[i]:
                    ans[i] = j + 1
                else:
                    break
        return ans
    # Time Complexity: O(N^2)
    # Space Complexity: O(N)

    def v2BinarySearch(self, nums: List[int], queries: List[int]) -> List[int]:
        # Calculate prefix sum for sorted nums arr
        prefixSum = list(accumulate(sorted(nums)))
        for i, q in enumerate(queries):
            queries[i] = bisect_right(prefixSum, q)
        # Return queries for opz space allocate
        return queries
    # Time Complexity: O(NlogN) -> NlogN is time complexity of sorted builtin function (tim sort)
    # Space Complexity: O(N) -> N is space complexity of sorted builtin function (tim sort)


print(Solution().answerQueries([4, 5, 2, 1], [4, 10, 21]))
