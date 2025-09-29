# Recursive way
def inorderTraversal(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    inorder(root)
    return result

# Time: O(n)
# Space : O(h)

'''
Solution1.
# Iterative way, using stack

def inorderTraversal(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result

# Time: O(n)
# Space: O(n)

'''
