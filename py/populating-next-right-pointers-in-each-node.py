# 116. Populating Next Right Pointers in Each Node You are given a perfect binary tree where all leaves are on the
# same level, and every parent has two children. The binary tree has the following definition:
#
# struct Node { int val; Node *left; Node *right; Node *next; } Populate each next pointer to point to its next right
# node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Example 1: Input: root = [1,2,3,4,5,6,7] Output: [1,#,2,3,#,4,5,6,7,#] Explanation: Given the above perfect binary
# tree (Figure A), your function should populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of
# each level.
#
# Example 2:
# Input: root = []
# Output: []


from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left=None, right=None, n=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = n


class Solution:
    def connect1(self, root: Optional[Node]) -> Optional[Node]:
        stack = []

        def traverse(node: Optional[Node]):
            if not node: return None
            node.next = stack.pop() if len(stack) else None
            traverse(node.right)
            traverse(node.left)
            stack.append(node)

        traverse(root)
        return root

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        level_start = root
        while level_start:
            cur_level = level_start
            while cur_level:
                if cur_level.left: cur_level.left.next = cur_level.right
                if cur_level.right and cur_level.next: cur_level.right.next = cur_level.next.left
                cur_level = cur_level.next
            level_start = level_start.left

        return root


if __name__ == '__main__':
    res = Solution().connect([1, 2, 3, 4, 5, 6, 7])
    print(res)
