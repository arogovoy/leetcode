# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = {}
        for i in range(0, len(s)):
            if s[i] not in hash_map:
                hash_map[s[i]] = t[i] if t[i] not in hash_map.values() else None

            if t[i] != hash_map[s[i]]:
                return False

        return True


if __name__ == '__main__':
    res = Solution().isIsomorphic('badc', 'baba')
    print(res)

    res = Solution().isIsomorphic('egg', 'add')
    print(res)

    res = Solution().isIsomorphic('foo', 'bar')
    print(res)

    res = Solution().isIsomorphic('paper', 'title')
    print(res)
