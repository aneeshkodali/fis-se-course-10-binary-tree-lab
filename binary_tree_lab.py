from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    
    # base case: empty tree
    if root is None:
        return 0

    # recursively find left and right subtree depths
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # return the larger depth + 1 for current node
    return max(left_depth, right_depth) + 1

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    current = root

    while current:

        # both nodes are smaller → go left
        if p.val < current.val and q.val < current.val:
            current = current.left

        # both nodes are larger → go right
        elif p.val > current.val and q.val > current.val:
            current = current.right

        # split point found → this is the LCA
        else:
            return current
