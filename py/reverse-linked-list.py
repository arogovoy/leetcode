# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
# Input: head = []
# Output: []

from typing import Optional

from py.utils import ListNode, array_to_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        while cur:
            n = cur.next
            cur.next, dummy.next = dummy.next, cur
            cur = n
        return dummy.next


if __name__ == '__main__':
    res = Solution().reverseList(array_to_list([1, 2, 3, 4, 5]))
    print(res)
