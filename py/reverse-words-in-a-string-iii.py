# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still
# preserving whitespace and initial word order.
#
# Example
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# Example
# Input: s = "God Ding"
# Output: "doG gniD"
from typing import List


class Solution:
    def reverseStr(self, s: str, start: int, end: int) -> str:
        r = ''
        for i in range(end, start - 1, -1):
            r += s[i]
        return s[:start] + r + s[end + 1:]

    def reverseWords(self, s: str) -> str:
        l, i = len(s), 0
        end = 0

        while end < l:
            if s[end] != ' ':
                end += 1
            else:
                s = self.reverseStr(s, i, end - 1)
                i = end + 1
                end = i
        return self.reverseStr(s, i, end - 1)


if __name__ == '__main__':
    res = Solution().reverseWords("Let's take LeetCode contest")
    print(res)

    res = Solution().reverseWords("a")
    print(res)

    res = Solution().reverseWords("aw")
    print(res)
