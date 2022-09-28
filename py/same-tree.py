# 100. Same Tree
from typing import Optional

from py.utils import TreeNode, BinaryTree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        return p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [[p, q]]
        while stack:
            h1, h2 = stack.pop()
            if (not h2 and h1) or (h2 and not h1):
                return False

            if h1 and h2:
                if h2.val != h1.val:
                    return False
                stack.append([h1.left, h2.left])
                stack.append([h1.right, h2.right])

        return True


if __name__ == '__main__':
    res = BinaryTree([3, 1, '#', '#', 2])
    res.display()
