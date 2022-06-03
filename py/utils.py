from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_list(a: List[int], i: int = 0):
    if i >= len(a): return
    return ListNode(a[i], array_to_list(a, i + 1))

