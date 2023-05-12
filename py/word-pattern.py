# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        hash_words = {}
        hash_patterns = {}
        for i, w in enumerate(words):
            p = pattern[i]
            if w not in hash_words and p not in hash_patterns:
                hash_words[w], hash_patterns[p] = p, w

            if w not in hash_words or hash_words[w] != p:
                return False
        return True


if __name__ == '__main__':
    print(Solution().wordPattern('abba', 'dog dog dog dog'))
    print(Solution().wordPattern('abba', 'dog cat cat dog'))
    print(Solution().wordPattern('abba', 'dog cat cat fish'))
    print(Solution().wordPattern('aaaa', 'dog cat cat dog'))
