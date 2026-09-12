# 25. Reverse Nodes in k-Group (Hard)
# Time Complexity: O(N) | Space Complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Tìm node thứ k kể từ groupPrev
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next

            # Đảo ngược nhóm k nodes
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Nối lại liên kết với phần còn lại của danh sách
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

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
    h1 = create_linked_list([1, 2, 3, 4, 5])
    print(linked_list_to_list(sol.reverseKGroup(h1, 2)))  # Output: [2, 1, 4, 3, 5]
    
    # Example 2
    h2 = create_linked_list([1, 2, 3, 4, 5])
    print(linked_list_to_list(sol.reverseKGroup(h2, 3)))  # Output: [3, 2, 1, 4, 5]