from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Đề bài yêu cầu kiểm tra LL có phải là cycle không
    # Nếu là Cycle thì trả về 1 ListNode với head là điểm bắt đầu của cycle
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visitedNode = set()
        while head:
            # Nếu head đã có trong visitedNode thì sẽ return head
            if head in visitedNode:
                return head
            else:
                # Add head vào set
                visitedNode.add(head)
                head = head.next
    # Time Complexity: O(N)
    # Space Complexity: O(N)
