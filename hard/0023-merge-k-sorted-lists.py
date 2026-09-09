# 23. Merge k Sorted Lists (Hard)
# Time Complexity: O(N log k) | Space Complexity: O(k)
# (với N là tổng số nút của tất cả các danh sách, k là số lượng danh sách)

import heapq
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> list[Optional[ListNode]]:
        heap = []
        
        # Đưa nút đầu tiên của mỗi danh sách vào min-heap
        for i, l in enumerate(lists):
            if l:
                # Dùng i để tránh so sánh trực tiếp hai ListNode khi val bằng nhau
                heapq.heappush(heap, (l.val, i, l))
                
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # Nếu nút vừa lấy ra có nút tiếp theo, thêm nút đó vào heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
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
    l1 = create_linked_list([1, 4, 5])
    l2 = create_linked_list([1, 3, 4])
    l3 = create_linked_list([2, 6])
    merged = sol.mergeKLists([l1, l2, l3])
    print(linked_list_to_list(merged))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]
    
    # Example 2
    print(linked_list_to_list(sol.mergeKLists([])))    # Output: []
    
    # Example 3
    print(linked_list_to_list(sol.mergeKLists([None])))  # Output: []