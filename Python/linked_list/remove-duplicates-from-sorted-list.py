# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Đề bài yêu cầu xóa phần tử trùng trong ListNode với value đã được sorted
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Tạo 1 biến curr copy ref của head
        curr = head

        # Trong khi curr != None thì check điều kiện
        while curr:
            # Trong khi curr.next != None và curr.next.val mà == val hiện tại
            # Thì gán next = next.next để skip Node có giá trị trùng
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
        return head

    # Time Complexity: O(N)
    # Space Complexity: O(1)
