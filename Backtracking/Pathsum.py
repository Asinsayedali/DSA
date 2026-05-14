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
    
# another solutions which doesn't use a list to store the path but instead uses a variable to keep track of the sum of the path
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, remaining):
            if not node:
                return False
            remaining -= node.val
            if not node.left and not node.right:
                return remaining == 0

            return dfs(node.left, remaining) or dfs(node.right, remaining)

        return dfs(root, targetSum)