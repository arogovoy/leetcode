# 111. Minimum Depth of Binary Tree
from typing import Optional

from py.utils import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return 1 + (min(l, r) if l and r else l or r)
