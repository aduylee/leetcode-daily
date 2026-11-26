# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
# Time Complexity: O(N) - mỗi nút được xử lý đúng 1 lần, tra cứu index trong O(1)
# Space Complexity: O(N) - lưu trữ Hash Map và ngăn xếp đệ quy

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            # Lấy giá trị nút gốc hiện tại từ preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Tìm vị trí phân chia trái/phải trong inorder
            mid = inorder_map[root_val]

            # Lưu ý: Phải xây dựng cây con trái trước vì preorder duyệt Left trước Right
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

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
    
    # Test Example 1: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    tree1 = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(level_order(tree1))  # Output: [3, 9, 20, None, None, 15, 7]

    # Test Example 2: preorder = [-1], inorder = [-1]
    tree2 = sol.buildTree([-1], [-1])
    print(level_order(tree2))  # Output: [-1]