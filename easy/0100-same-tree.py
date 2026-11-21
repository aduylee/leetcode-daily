# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 100. Same Tree (Easy)
# Time Complexity: O(N) - với N là số nút của cây nhỏ hơn
# Space Complexity: O(H) - với H là chiều cao của cây (O(log N) nếu cân bằng, O(N) nếu lệch)

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Cả hai đều rỗng -> giống nhau
        if not p and not q:
            return True
        
        # Một bên rỗng hoặc giá trị khác nhau -> khác nhau
        if not p or not q or p.val != q.val:
            return False
        
        # Kiểm tra đệ quy cả nhánh trái và nhánh phải
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# --- TEST TRONG VS CODE ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Example 1: p = [1, 2, 3], q = [1, 2, 3] -> True
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(sol.isSameTree(p1, q1))  # Output: True

    # Test Example 2: p = [1, 2], q = [1, null, 2] -> False
    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))
    print(sol.isSameTree(p2, q2))  # Output: False