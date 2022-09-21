# 94. Binary Tree Inorder Traversal
from typing import Optional, List

from py.utils import TreeNode, BinaryTree


class Solution:
    # def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
    #     stack = []
    #     result = []
    #     last = root
    #     while stack or last:
    #         while last:
    #             stack.append(last)
    #             last = last.left
    #
    #         last = stack.pop()
    #         result.append(last.val)
    #         last = last.right
    #
    #     return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = [root]
        result = []
        while stack:
            last = stack[-1]
            if not last.left:
                result.append(stack.pop().val)
                if last.right:
                    stack.append(last.right)
            else:
                stack.append(last.left)
                last.left = None

        return result


if __name__ == '__main__':
    res = BinaryTree([3, 1, '#', '#', 2])
    res.display()
