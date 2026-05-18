# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []
        def dfs(root):
            if(root is None):
                return
            dfs(root.left)
            dfs(root.right)
            heapq.heappush(min_heap,root.val)
        dfs(root)
        for i in range(k - 1):
            heapq.heappop(min_heap)
        return heapq.heappop(min_heap)
        
            
            
