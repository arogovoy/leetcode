# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_list(a: List[int], i: int = 0):
    if i >= len(a): return
    return ListNode(a[i], array_to_list(a, i + 1))


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i, l = 0, 1
        node = head

        while node.next:
            node = node.next
            l += 1

        if not head.next:
            return None
        node, prev = head, head

        while node:
            if i == l - n:
                if i == 0:
                    head = node.next
                else:
                    prev.next = node.next
            else:
                prev = node
            node = node.next
            i += 1

        return head


if __name__ == '__main__':
    # res = Solution().removeNthFromEnd(array_to_list([1, 2, 3, 4, 5]), 2)
    # print(res.val)
    #
    # res = Solution().removeNthFromEnd(array_to_list([1]), 1)
    # print(res.val)

    # res = Solution().removeNthFromEnd(array_to_list([1, 2]), 1)
    # print(res.val)

    res = Solution().removeNthFromEnd(array_to_list([1, 2]), 2)
    print(res.val)
