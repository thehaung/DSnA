# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # A palindrome is a sequence that reads the same forward and backward.
    # Đề bài yêu cầu kiểm tra ListNode có phải là 1 palindrome không
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Tìm mid của ListNode, sau đó đảo ngược
        midNodeReversed = self.reverseList(self.middleNode(head))

        # Kiểm tra ListNode khác None thì kiểm tra
        # Nếu val của reversedNode != head.val thì chứng tỏ không hợp lệ
        while midNodeReversed:
            if midNodeReversed.val != head.val:
                return False
            midNodeReversed = midNodeReversed.next
            head = head.next
        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead = None
        while head:
            nxt = head.next
            head.next = reversedHead
            reversedHead = head
            head = nxt

        return reversedHead

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Time Complexity: O(N)
    # Space Complexity: O(1)
