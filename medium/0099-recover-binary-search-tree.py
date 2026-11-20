# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 99. Recover Binary Search Tree (Medium)
# Time Complexity: O(N) | Space Complexity: O(H) (với H là chiều cao của cây)

class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        first = None
        second = None
        prev = None

        def inorder(node: TreeNode | None):
            nonlocal first, second, prev
            if not node:
                return
            
            inorder(node.left)
            
            # Kiểm tra tính tăng dần của phép duyệt Inorder
            if prev and prev.val > node.val:
                if not first:
                    first = prev
                second = node
            prev = node
            
            inorder(node.right)

        inorder(root)
        # Hoán đổi lại giá trị của 2 nút bị sai
        if first and second:
            first.val, second.val = second.val, first.val

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    def print_inorder(node):
        return print_inorder(node.left) + [node.val] + print_inorder(node.right) if node else []

    sol = Solution()
    
    # Test Example 1: root = [1, 3, null, null, 2] -> [3, 1, null, null, 2]
    root1 = TreeNode(1, TreeNode(3, None, TreeNode(2)), None)
    sol.recoverTree(root1)
    print(print_inorder(root1))  # Output: [1, 2, 3]

    # Test Example 2: root = [3, 1, 4, null, null, 2] -> [2, 1, 4, null, null, 3]
    root2 = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2), None))
    sol.recoverTree(root2)
    print(print_inorder(root2))  # Output: [1, 2, 3, 4]