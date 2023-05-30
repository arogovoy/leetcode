# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        pos = 0
        i = 0

        if not len_s:
            return True

        while pos < len_s and i < len(t):
            if s[pos] == t[i]:
                pos += 1
            i += 1

        return pos == len_s


if __name__ == '__main__':
    print(Solution().isSubsequence('acb', 'ahbgdc'))
    print(Solution().isSubsequence('b', 'c'))
    print(Solution().isSubsequence('abc', 'abdabc'))
    print(Solution().isSubsequence('abc', 'ahbgdc'))
    print(Solution().isSubsequence('axc', 'ahbgdc'))
    print(Solution().isSubsequence('', 'ahbgdc'))
    print(Solution().isSubsequence('dadw', ''))

