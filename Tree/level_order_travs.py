from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bst(root):
            queue = deque()
            result = []
            if root:
                queue.append(root)
            level = 0
            while len(queue)>0:
                result_value=[]
                for i in range(len(queue)):
                    curr = queue.popleft()
                    result_value.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                result.append(result_value)
                level+=1
            return result



        return bst(root)