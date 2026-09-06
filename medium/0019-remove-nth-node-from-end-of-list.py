# 19. Remove Nth Node From End of List (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        
        # Cho fast tiến trước n + 1 bước
        for _ in range(n + 1):
            fast = fast.next
            
        # Di chuyển cả 2 con trỏ cho đến khi fast chạm tới cuối danh sách
        while fast:
            fast = fast.next
            slow = slow.next
            
        # Xóa nút thứ n từ dưới lên
        slow.next = slow.next.next
        
        return dummy.next

# --- HÀM HỖ TRỢ TEST TRONG VS CODE ---
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print(linked_list_to_list(sol.removeNthFromEnd(head1, 2)))  # Output: [1, 2, 3, 5]
    
    # Example 2
    head2 = create_linked_list([1])
    print(linked_list_to_list(sol.removeNthFromEnd(head2, 1)))  # Output: []
    
    # Example 3
    head3 = create_linked_list([1, 2])
    print(linked_list_to_list(sol.removeNthFromEnd(head3, 1)))  # Output: [1]