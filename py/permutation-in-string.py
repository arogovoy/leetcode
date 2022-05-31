# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1, map2 = {}, {}
        l1, l2 = len(s1), len(s2)
        for i in range(l1):
            map1[s1[i]] = map1[s1[i]] + 1 if s1[i] in map1 else 1
            map2[s1[i]] = 0

        start, end = 0, 0
        while end < l2:
            if s2[end] in map2:
                map2[s2[end]] += 1

                if map1[s2[end]] < map2[s2[end]]:
                    map2[s2[end]] -= 1
                    map2[s2[start]] -= 1
                    start += 1
                    end -= 1

                if end - start + 1 == l1:
                    return True
            else:
                for i in range(start, end):
                    if s2[i] in map2 and map2[s2[i]] > 0:
                        map2[s2[i]] -= 1
                start = end + 1
            end += 1

        return False


if __name__ == '__main__':
    res = Solution().checkInclusion('abc', 'eidbadddabc')  # true
    print(res)

    res = Solution().checkInclusion('abc', 'eidbaabc') #true
    print(res)

    res = Solution().checkInclusion('ab', 'eidbaooo') #true
    print(res)

    res = Solution().checkInclusion('ab', 'eidboaoo') #false
    print(res)

    res = Solution().checkInclusion('ab', 'eidbaaoo') #true
    print(res)

    res = Solution().checkInclusion('abc', 'eidbaaoo') #false
    print(res)

    res = Solution().checkInclusion('abb', 'eidbbaabc') #true
    print(res)
