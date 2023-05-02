# 257. Binary Tree Paths
from typing import List, Optional

from py.utils import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        left = list(map(lambda s: f'{root.val}->{s}', self.binaryTreePaths(root.left)))
        right = list(map(lambda s: f'{root.val}->{s}', self.binaryTreePaths(root.right)))

        return (left + right) or [str(root.val)]


