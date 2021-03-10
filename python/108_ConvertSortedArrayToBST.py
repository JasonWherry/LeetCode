# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums or len(nums) == 0:
            return None
        
        elif len(nums) == 1:
            return TreeNode(nums[0])
        
        else:
            middle = int(len(nums) / 2)
            
            left = nums[:middle]
            right = nums[middle+1:]
            
            root = TreeNode(nums[middle])
            
            root.left = self.sortedArrayToBST(left)
            root.right = self.sortedArrayToBST(right)
            
            return root
        