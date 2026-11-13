# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 92. Reverse Linked List II (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # 1. Di chuyển prev đến vị trí ngay trước left
        for _ in range(left - 1):
            prev = prev.next

        # 2. Đảo ngược đoạn từ left đến right
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

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
    
    # Test Example 1: head = [1, 2, 3, 4, 5], left = 2, right = 4 -> [1, 4, 3, 2, 5]
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print(linked_list_to_list(sol.reverseBetween(head1, 2, 4)))  # Output: [1, 4, 3, 2, 5]

    # Test Example 2: head = [5], left = 1, right = 1 -> [5]
    head2 = create_linked_list([5])
    print(linked_list_to_list(sol.reverseBetween(head2, 1, 1)))  # Output: [5]