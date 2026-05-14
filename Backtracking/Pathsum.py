# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path=[]
        def roottoleaf(root, path):
            if not root:
                return False
            path.append(root.val)
            if not root.left and not root.right and sum(path)==targetSum:
                return True
            if roottoleaf(root.right,path):
                return True
            if roottoleaf(root.left, path):
                return True 
            path.pop()
            return False
        return roottoleaf(root,path)