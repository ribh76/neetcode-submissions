from typing import List
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        queue = deque() 
        if root: 
            queue.append(root) 
        level = 0

        while len(queue) > 0: 
            curr_level = []
            for i in range(len(queue)): 
                curr = queue.popleft()
                curr_level.append(curr.val) 
                if curr.left: 
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right) 
            level =+1
            result.append(curr_level) 

        return result
        




