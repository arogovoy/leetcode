# 110. Balanced Binary Tree
from typing import Optional

from py.utils import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False

        val_left = root.left.val if root.left else 0
        val_right = root.right.val if root.right else 0

        if abs(val_left - val_right) >= 2:
            return False

        root.val = max(val_left, val_right) + 1
        return True
