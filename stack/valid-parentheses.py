class Solution:
    """
    Đề bài yêu cầu kiểm tra 1 chuỗi ngoặc có được đóng mở đúng không
    Với rules ngoặc mở trước thì phải được đóng trước
    Ý tưởng: Dùng Stack để implement
    Loop và Stack sẽ lưu những ngoặc mở, nếu ngoặc đóng thì sẽ kiểm tra
    ngoặc mở cuối cùng có phải là 1 cặp không, nếu không thì return False
    Sau khi loop xong mà stack empty thì là hợp lệ
    """

    def isValid(self, s: str) -> bool:
        stack = []
        matchingPair = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in "({[":
                stack.append(char)
                continue
            if not stack or stack[-1] != matchingPair[char]:
                return False
            stack.pop()
        return len(stack) == 0
    # Time Complexity: O(N)
    # Space Complexity: O(N)


print(Solution().isValid('()[]{}'))
