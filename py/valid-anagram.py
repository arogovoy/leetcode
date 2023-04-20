# 242. Valid Anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alph = {}

        for i in range(len(s)):
            alph[s[i]] = 1 if s[i] not in alph else alph[s[i]] + 1
            alph[t[i]] = -1 if t[i] not in alph else alph[t[i]] - 1

        for item in alph.values():
            if item:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAnagram('anagram', 'nagaram'))
    print(Solution().isAnagram('rat', 'car'))
