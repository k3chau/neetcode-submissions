# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root,1)]
        max_depth = 0
        while stack:
            curr, current_depth = stack.pop()
            max_depth = max(current_depth,max_depth)
            if curr.right:
                stack.append((curr.right,current_depth + 1))
            if curr.left:
                stack.append((curr.left,current_depth + 1))
        return max_depth
        

        