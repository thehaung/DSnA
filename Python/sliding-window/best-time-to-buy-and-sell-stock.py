from typing import List


class Solution:
    """
    Đề bài yêu cầu tìm thời điểm thích hợp để mua và bán cổ phiếu, tính ra lợi nhuận tốt nhất
    Ở đây ta thấy ta chỉ được mua cố phiếu vào ngày T0 và giả sử sẽ bán nó vào ngày T + n (T0 < n < len(prices) - 1)
    Ta sẽ tính toán profit dựa trên cột mốc ngày cổ phiếu giá thấp nhất có thể, khi loop qua bảng giá mà có
        giá nào thấp hơn giá thấp nhất hiện tại thì ta replace, và sẽ dùng giá của ngày hiện tại - giá thấp nhất
        so sánh với lợi nhuận tối đa để replace
    Ý tưởng: Dùng Sliding Window
    """
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = float("inf")
        maxProfit = 0
        for price in prices:
            if price < lowestPrice:
                lowestPrice = price
            elif price - lowestPrice > maxProfit:
                maxProfit = price - lowestPrice
        return maxProfit
    # Time Complexity: O(N)
    # Space Complexity: O(1)


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
