# 61. Rotate List (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1. Tính chiều dài danh sách và tìm node cuối cùng (tail)
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. Tối ưu số lần quay k và nối vòng tròn
        k = k % length
        if k == 0:
            return head
        
        tail.next = head  # Nối thành vòng tròn

        # 3. Tìm node mới (length - k bước từ đầu)
        steps_to_new_head = length - k
        new_tail = tail
        for _ in range(steps_to_new_head):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None  # Cắt vòng tròn

        return new_head