# 58. Length of Last Word


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s) - 1
        w = 0

        while l >= 0:
            if not w and s[l] != ' ':
                w = l
            if w and s[l] == ' ':
                break
            l -= 1

        return w - l


if __name__ == '__main__':
    res = Solution().lengthOfLastWord('Hello World')
    print(res)

    res = Solution().lengthOfLastWord("   fly me   to   the moon  ")
    print(res)

    res = Solution().lengthOfLastWord('Hello')
    print(res)
