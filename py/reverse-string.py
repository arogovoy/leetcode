# Reverse String
#
# You must do this by modifying the input array in-place with O(1) extra memory.
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        m = l // 2
        for i in range(m):
            s[i], s[l - i - 1] = s[l - i - 1], s[i]
        return s


if __name__ == '__main__':
    res = Solution().reverseString(["h","e","l","l","o"])
    print(res)
