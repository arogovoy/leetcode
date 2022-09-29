# 108. Convert Sorted Array to Binary Search Tree

from typing import Optional, List
from py.utils import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def balancedTree(start, end) -> Optional[TreeNode]:
            if start > end:
                return None
            mid = int((start + end) / 2)
            node = TreeNode(nums[mid])
            node.left = balancedTree(start, mid - 1)
            node.right = balancedTree(mid + 1, end)
            return node

        return balancedTree(0, len(nums) - 1)
