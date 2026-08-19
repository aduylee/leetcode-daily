# 2. Add Two Numbers (Medium)
# Time Complexity: O(max(N, M)) | Space Complexity: O(max(N, M))

from typing import Optional

# Định nghĩa cấu trúc nút của Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            curr.next = ListNode(new_val)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next

# --- HÀM HỖ TRỢ TEST TRONG VS CODE ---
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

# TEST CASE
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: l1 = [2, 4, 3], l2 = [5, 6, 4] -> Output: [7, 0, 8]
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    print_linked_list(sol.addTwoNumbers(l1, l2))

    # Example 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] -> Output: [8, 9, 9, 9, 0, 0, 0, 1]
    l3 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l4 = create_linked_list([9, 9, 9, 9])
    print_linked_list(sol.addTwoNumbers(l3, l4))