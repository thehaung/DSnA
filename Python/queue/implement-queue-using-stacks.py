class MyQueue:
    # Đề bài yêu cầu implement Queue DS dựa trên Stack DS
    # Ý tưởng: Dùng Dynamic Array trong Py
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        return self.stack.append(x)
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def pop(self) -> int:
        if self.empty():
            return -1
        return self.stack.pop(0)
    # Time Complexity: O(N) -> N là size của Stack
    # Space Complexity: O(1)

    def peek(self) -> int:
        return self.stack[0]
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def empty(self) -> bool:
        return len(self.stack) == 0
    # Time Complexity: O(1)
    # Space Complexity: O(1)
