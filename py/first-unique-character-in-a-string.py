# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = {}
        for i, c in enumerate(s):
            if c not in table:
                table[c] = i
            else:
                table[c] = -1

        return next((x for x in table.values() if x != -1), -1)


if __name__ == '__main__':
    print(Solution().firstUniqChar('leetcode'))
    print(Solution().firstUniqChar('loveleetcode'))
    print(Solution().firstUniqChar('aabb'))

