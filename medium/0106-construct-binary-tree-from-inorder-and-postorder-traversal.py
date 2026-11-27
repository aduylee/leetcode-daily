# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 106. Construct Binary Tree from Inorder and Postorder Traversal (Medium)
# Time Complexity: O(N) - mỗi nút được xử lý đúng 1 lần, tra cứu index trong O(1)
# Space Complexity: O(N) - lưu trữ Hash Map và ngăn xếp đệ quy

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def helper(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            # Lấy giá trị nút gốc hiện tại từ cuối postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            # Tìm vị trí phân chia trái/phải trong inorder
            mid = inorder_map[root_val]

            # Bắt buộc dựng cây con phải trước vì đang duyệt ngược postorder (Root -> Right -> Left)
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    from collections import deque
    def level_order(root):
        if not root: return []
        res, q = [], deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)
        while res and res[-1] is None:
            res.pop()
        return res

    sol = Solution()
    
    # Test Example 1: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    tree1 = sol.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(level_order(tree1))  # Output: [3, 9, 20, None, None, 15, 7]

    # Test Example 2: inorder = [-1], postorder = [-1]
    tree2 = sol.buildTree([-1], [-1])
    print(level_order(tree2))  # Output: [-1]