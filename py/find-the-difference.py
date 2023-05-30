# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        chars = [0] * 28
        for c in t:
            chars[ord(c) - 97] += 1
        for c in s:
            chars[ord(c) - 97] -= 1

        return next((chr(i + 97) for i, count in enumerate(chars) if count == 1), '')


if __name__ == '__main__':
    print(Solution().findTheDifference('abcd', 'abcde'))
    print(Solution().findTheDifference('', 'y'))

