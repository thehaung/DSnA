from collections import deque


class MyCircularQueue:
    # Đề bài yêu cầu implement Circular Queue với base performed FIFO (Queue)
    # Ý tưởng dùng deque trong Py collections để implement
    def __init__(self, k: int):
        self.queue = deque()
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.capacity == len(self.queue):
            return False
        self.queue.append(value)
        return True
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def deQueue(self) -> bool:
        if len(self.queue) == 0:
            return False
        self.queue.popleft()
        return True
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def Front(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[0]
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def Rear(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def isEmpty(self) -> bool:
        return len(self.queue) == 0
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def isFull(self) -> bool:
        return len(self.queue) == self.capacity
    # Time Complexity: O(1)
    # Space Complexity: O(1)
