# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
        
    def isMirror(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None: 
            return True
        else:
            if root1 and root2:
                # print('root1', root1)
                # print('root2', root2)
                if root1.val == root2.val:
                    # print('root1.val', root1.val)
                    # print('root2.val', root2.val)
                    return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
        
        return False
    