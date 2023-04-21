# 160. Intersection of Two Linked Lists
from typing import Optional

from py.utils import ListNode, array_to_list


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and not headB:
            return

        result = self.getIntersectionNode(headA and headA.next, headB and headB.next)


        return re


if __name__ == '__main__':
    res = Solution().getIntersectionNode(array_to_list([4, 1, 8, 4, 5, null]), array_to_list([5, 6, 1, 8, 4, 5]))
    print(res.val)
