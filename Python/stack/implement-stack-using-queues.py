from collections import deque


class MyStack:
    # Đề bài yêu cầu implement Stack DS, nhưng phải dùng queue
    # Ý tường: Dùng deque trong Py vì đã có implement Stack
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def pop(self) -> int:
        return self.queue.pop()
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def top(self) -> int:
        return self.queue[-1]
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def empty(self) -> bool:
        return len(self.queue) == 0
    # Time Complexity: O(1)
    # Space Complexity: O(1)
