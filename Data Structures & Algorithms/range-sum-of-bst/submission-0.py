# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = []

        def traverse(root): 
            if not root:
                return 
            traverse(root.left)
            traverse(root.right)
            if low <= root.val <= high: 
                result.append(root.val) 
        
        traverse(root)
        return sum(result)