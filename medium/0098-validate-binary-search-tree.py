# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 98. Validate Binary Search Tree (Medium)
# Time Complexity: O(N) | Space Complexity: O(H) (với H là chiều cao của cây)

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node: TreeNode | None, low: float, high: float) -> bool:
            if not node:
                return True
            
            # Giá trị nút hiện tại phải nằm nghiêm ngặt trong khoảng (low, high)
            if not (low < node.val < high):
                return False
            
            # Kiểm tra đệ quy hai nhánh con với cận mới được siết chặt
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
            
        return validate(root, float('-inf'), float('inf'))

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Example 1: root = [2, 1, 3] -> True
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(sol.isValidBST(root1))  # Output: True[cite: 9]

    # Test Example 2: root = [5, 1, 4, null, null, 3, 6] -> False
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(sol.isValidBST(root2))  # Output: False