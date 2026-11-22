# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 101. Symmetric Tree (Easy)
# Time Complexity: O(N) - duyệt qua mỗi nút đúng 1 lần
# Space Complexity: O(H) - chiều cao của ngăn xếp đệ quy (O(log N) nếu cân bằng, O(N) nếu lệch)

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        def isMirror(t1: TreeNode | None, t2: TreeNode | None) -> bool:
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            # So sánh chéo: ngoài với ngoài, trong với trong
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Example 1: root = [1, 2, 2, 3, 4, 4, 3] -> True
    root1 = TreeNode(1,
                     TreeNode(2, TreeNode(3), TreeNode(4)),
                     TreeNode(2, TreeNode(4), TreeNode(3)))
    print(sol.isSymmetric(root1))  # Output: True[cite: 12]

    # Test Example 2: root = [1, 2, 2, null, 3, null, 3] -> False
    root2 = TreeNode(1,
                     TreeNode(2, None, TreeNode(3)),
                     TreeNode(2, None, TreeNode(3)))
    print(sol.isSymmetric(root2))  # Output: False