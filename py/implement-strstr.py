# 28. Implement strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        i = needle_len - 1
        while i < len(haystack):
            if haystack[i] == needle[needle_len - 1] and haystack[i - needle_len + 1:i + 1] == needle:
                return i - needle_len + 1

            i += 1

        return -1


if __name__ == '__main__':
    res = Solution().strStr('1233333f', '333f')
    print(res)

    res = Solution().strStr('hello', 'll')
    print(res)
    res = Solution().strStr('aaaaa', 'bba')
    print(res)
