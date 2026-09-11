# 24. Swap Nodes in Pairs (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            # Hoán đổi liên kết
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Cập nhật prev cho vòng lặp tiếp theo
            prev = first
            
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
    h1 = create_linked_list([1, 2, 3, 4])
    print(linked_list_to_list(sol.swapPairs(h1)))  # Output: [2, 1, 4, 3]
    
    # Example 2
    h2 = create_linked_list([])
    print(linked_list_to_list(sol.swapPairs(h2)))  # Output: []
    
    # Example 3
    h3 = create_linked_list([1])
    print(linked_list_to_list(sol.swapPairs(h3)))  # Output: [1]
    
    # Example 4
    h4 = create_linked_list([1, 2, 3])
    print(linked_list_to_list(sol.swapPairs(h4)))  # Output: [2, 1, 3]