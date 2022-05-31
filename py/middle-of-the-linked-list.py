# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 1
        node = head
        while node.next:
            node = node.next
            l += 1

        node = head
        m = l // 2
        for i in range(m):
            node = node.next

        return node


if __name__ == '__main__':
    res = Solution().middleNode(array_to_list([1, 2, 3, 4, 5]))
    print(res.val)

    res = Solution().middleNode(array_to_list([1, 2, 3, 4, 5, 6]))
    print(res.val)
