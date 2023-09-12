class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class BrowserHistory:
    # Đề bài yêu cầu implement lịch sử cho trình duyệt
    # Tới trang, back lại trang trước đó, forward tới trang sau
    def __init__(self, homepage: str):
        self.root = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def back(self, steps: int) -> str:
        # Back về prev theo số step
        # Nếu hết step thì chứng tỏ nằm ở root, trả về homepage
        while steps and self.root.prev:
            self.root = self.root.prev
            steps -= 1
        return self.root.val
    # Time Complexity: O(N)
    # Space Complexity: O(1)

    def forward(self, steps: int) -> str:
        # Forward tới next theo số step
        # Nếu hết step thì chứng tỏ dừng ở vị trí cuối của node
        # Trả về giá trị node đó
        while steps and self.root.next:
            self.root = self.root.next
            steps -= 1
        return self.root.val
    # Time Complexity: O(N)
    # Space Complexity: O(1)
