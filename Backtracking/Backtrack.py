# Backtracking Template for finding a path without zeroes in the path

def leafpath(root, path):
    if not root:
        return False
    if root.val==0:
        return False
    path.append(root.val)
    if not root.left and not root.right:
        return True
    if leafpath(root.left, path):
        return True
    if leafpath(root.right, path):
        return True
    path.pop()
    return False