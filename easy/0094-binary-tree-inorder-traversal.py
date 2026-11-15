# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 94. Binary Tree Inorder Traversal (Easy)
# Time Complexity: O(N) | Space Complexity: O(H) (với H là chiều cao của cây)

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        # Cách 1: Đệ quy
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return res

        # Cách 2: Khử đệ quy (Iterative dùng Stack)
        # res = []
        # stack = []
        # curr = root
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     curr = curr.right
        # return res

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    # Test Example 1: root = [1, null, 2, 3] -> [1, 3, 2]
    root1 = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    sol = Solution()
    print(sol.inorderTraversal(root1))  # Output: [1, 3, 2]