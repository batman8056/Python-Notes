# Find Maximum Depth of Binary Tree
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(max_depth(root))  # Output: 2
