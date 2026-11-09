# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 86. Partition List (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        
        before = before_dummy
        after = after_dummy
        
        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next
            
        # Ngắt kết nối phần cuối của after để tránh vòng lặp
        after.next = None
        # Nối phần before với phần after
        before.next = after_dummy.next
        
        return before_dummy.next

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    def create_linked_list(arr):
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def linked_list_to_list(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    sol = Solution()
    
    # Test Example 1: head = [1, 4, 3, 2, 5, 2], x = 3 -> [1, 2, 2, 4, 3, 5]
    head1 = create_linked_list([1, 4, 3, 2, 5, 2])
    print(linked_list_to_list(sol.partition(head1, 3)))  # Output: [1, 2, 2, 4, 3, 5][cite: 8]

    # Test Example 2: head = [2, 1], x = 2 -> [1, 2]
    head2 = create_linked_list([2, 1])
    print(linked_list_to_list(sol.partition(head2, 2)))  # Output: [1, 2][cite: 8]