# 234. Palindrome Linked List
from typing import Optional

from py.utils import ListNode, array_to_list


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def traverse(node: Optional[ListNode]):
            if not node:
                return True

            nonlocal head
            res = traverse(node.next)
            if res and node.val == head.val:
                head = head.next
                return True
            return False

        return traverse(head)


if __name__ == '__main__':
    print(Solution().isPalindrome(array_to_list([1, 2, 1])))
    print(Solution().isPalindrome(array_to_list([1, 2, 2, 1])))
    print(Solution().isPalindrome(array_to_list([1, 2])))
