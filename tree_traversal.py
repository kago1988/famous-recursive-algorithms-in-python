class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# Example usage:
# Creating a simple binary tree:
#     1
#    / \
#   2   3
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)

inorder_traversal(node)  # Output: 2 1 3
