# 108. Convert Sorted Array to Binary Search Tree

from typing import Optional

from py.utils import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True

            if not left and right or not right and left:
                return False

            return left.val == right.val and compare(left.left, right.right) and compare(left.right, right.left)

        return compare(root.left, root.right)