# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 82. Remove Duplicates from Sorted List II (Medium)
# Time Complexity: O(N) | Space Complexity: O(1)

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # Tạo dummy node trỏ vào đầu danh sách để dễ dàng xử lý trường hợp head bị xóa
        dummy = ListNode(0, head)
        prev = dummy

        curr = head
        while curr:
            # Kiểm tra nếu có chuỗi giá trị trùng lặp phía trước
            if curr.next and curr.val == curr.next.val:
                # Bỏ qua toàn bộ các nút có giá trị trùng lặp
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Nối prev vượt qua toàn bộ các nút trùng lặp
                prev.next = curr.next
            else:
                # Nếu không trùng lặp, dịch chuyển prev lên
                prev = prev.next
            
            curr = curr.next

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
    
    # Test Example 1: [1, 2, 3, 3, 4, 4, 5] -> [1, 2, 5]
    head1 = create_linked_list([1, 2, 3, 3, 4, 4, 5])
    print(linked_list_to_list(sol.deleteDuplicates(head1)))  # Output: [1, 2, 5]

    # Test Example 2: [1, 1, 1, 2, 3] -> [2, 3]
    head2 = create_linked_list([1, 1, 1, 2, 3])
    print(linked_list_to_list(sol.deleteDuplicates(head2)))  # Output: [2, 3]