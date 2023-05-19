# 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = {}
        for c in magazine:
            if c not in hash_map:
                hash_map[c] = 0
            hash_map[c] += 1

        for c in ransomNote:
            if c not in hash_map:
                hash_map[c] = 0
            hash_map[c] -= 1
            if hash_map[c] < 0:
                return False

        return True


if __name__ == '__main__':
    print(Solution().canConstruct("a", "b"))
    print(Solution().canConstruct("aa", "ab"))
    print(Solution().canConstruct("ba", "ab"))
    print(Solution().canConstruct("aa", "aab"))
    print(Solution().canConstruct("aa", "aaab"))
