# 203. Remove Linked List Elements
from typing import Optional

from py.utils import ListNode, array_to_list

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next

        return dummy.next


if __name__ == '__main__':
    res = Solution().removeElements(array_to_list([1, 2, 6, 3, 4, 5, 6]), 6)
    print(res.print_list())
