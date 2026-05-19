#first code 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def inorder_bst(root):
            if not root:
                return 
            inorder_bst(root.left)
            result.append(root.val)
            inorder_bst(root.right)
        inorder_bst(root)
        return result[k-1]
        
#optimsed code only get the required value and not store all the values in the result array
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = root.val
        count = k
        def inorder_bst(root):
            nonlocal result, count
            if not root:
                return 
            inorder_bst(root.left)
            count -= 1
            if count == 0:
                result = root.val
            inorder_bst(root.right)
        inorder_bst(root)
        return result