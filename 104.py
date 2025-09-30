# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        hleft = self.maxDepth(root.left)
        hright = self.maxDepth(root.right)

        return max(hleft, hright) + 1

'''
Solution 1.

def maxDepth(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if not root:
        return 0

    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# DFS
# Time: O(n)
# Space: O(h)

'''

'''
Solution 2.

from collections import deque

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
            
        return depth

# BFS, Queue
# Time : O(n)
# Space : O(w)

'''
