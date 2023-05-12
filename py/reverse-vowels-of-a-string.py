# 345. Reverse Vowels of a String


class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while j > i and s[j] not in vowels:
                j -= 1

            c1, c2 = s[i], s[j]
            s = s[:i] + c2 + s[i + 1:]
            s = s[:j] + c1 + s[j + 1:]
            i += 1
            j -= 1
        return s


if __name__ == '__main__':
    print(Solution().reverseVowels('hello'))
    print(Solution().reverseVowels('ae'))
    print(Solution().reverseVowels('waef'))
    print(Solution().reverseVowels('waf'))
