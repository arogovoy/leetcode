# 617. Merge Two Binary Trees
# You are given two binary trees root1 and root2.
#
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the
# others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes
# overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as
# the node of the new tree.
#
# Return the merged tree.
#
# Note: The merging process must start from the root nodes of both trees.
#
# Example 1:
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
#
# Example 2:
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def arrayToNode(arr, i, n) -> TreeNode:
    root = None
    # Base case for recursion
    if i < n and not (arr[i] is None):
        root = TreeNode(arr[i])

        # insert left child
        root.left = arrayToNode(arr, 2 * i + 1, n)

        # insert right child
        root.right = arrayToNode(arr, 2 * i + 2, n)

    return root


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2

        if not root2:
            return root1

        root2.val += root1.val
        root2.left = self.mergeTrees(root1.left, root2.left)
        root2.right = self.mergeTrees(root1.right, root2.right)

        return root2


if __name__ == '__main__':
    res = Solution().mergeTrees(arrayToNode([1, 3, 2, 5], 0, 4), arrayToNode([2, 1, 3, None, 4, None, 7], 0, 7))
    print(res)
