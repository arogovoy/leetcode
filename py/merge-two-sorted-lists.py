# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two
# lists.
# Return the head of the merged linked list.
#
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        temp = head
        cur1, cur2 = list1, list2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                temp.next = cur1
                cur1 = cur1.next
            else:
                temp.next = cur2
                cur2 = cur2.next

            temp = temp.next

        if cur1: temp.next = cur1
        if cur2: temp.next = cur2

        return head.next


if __name__ == '__main__':
    # res = Solution().moveZeroes([4,2,4,0,0,3,0,5,1,0])
    print(1)
    #
    # res = Solution().moveZeroes([1, 0, 1])
    # print(res)
    #
    # res = Solution().moveZeroes([0,1,0,3,12])
    # print(res)
    #
    # res = Solution().moveZeroes([0, 1, 0, 3, 12, 0])
    # print(res)
    #
    # res = Solution().moveZeroes([0])
    # print(res)
