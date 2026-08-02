from typing import Optional


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Returns the maximum depth (height) of a binary tree.

    The depth is the number of nodes along the longest path from the
    root node down to the farthest leaf node. An empty tree has depth 0.

    Approach:
        Recursively find the depth of the left and right subtrees,
        then return 1 (for the current node) plus whichever side is deeper.
    """
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor (LCA) of two nodes in a Binary Search Tree.

    The LCA is the deepest node that has both p and q as descendants
    (a node can be a descendant of itself).

    Approach:
        Uses BST ordering properties instead of a generic tree search:
        - If both p and q are less than the current node, the LCA must
          be in the left subtree, so move left.
        - If both are greater, the LCA must be in the right subtree,
          so move right.
        - Otherwise, the paths to p and q diverge here (or one of them
          IS the current node), so the current node is the LCA.
    """
    current = root

    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            return current

    return None