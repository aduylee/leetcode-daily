# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 104. Maximum Depth of Binary Tree (Easy)
# Time Complexity: O(N) - duyệt qua mỗi nút đúng 1 lần
# Space Complexity: O(H) - chiều cao của ngăn xếp đệ quy (O(log N) nếu cân bằng, O(N) nếu lệch)

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
            
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Example 1: root = [3, 9, 20, null, null, 15, 7] -> 3
    root1 = TreeNode(3,
                     TreeNode(9),
                     TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.maxDepth(root1))  # Output: 3[cite: 13]

    # Test Example 2: root = [1, null, 2] -> 2
    root2 = TreeNode(1, None, TreeNode(2))
    print(sol.maxDepth(root2))  # Output: 2[cite: 13]