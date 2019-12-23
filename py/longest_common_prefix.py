# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        prev = None
        max_len = 0

        while res != prev:
            prev = res
            alphabet = {}
            for i, s in enumerate(strs):
                if len(s):
                    char = s[0]
                    if char not in alphabet:
                        alphabet[char] = 1
                    else:
                        alphabet[char] += 1
                    strs[i] = s[1:]
                else:
                    alphabet[''] = 0

            temp_max = 0
            temp_char = ''

            for key, value in alphabet.items():
                if value >= temp_max:
                    temp_max = value
                    temp_char = key

            if temp_max < max_len:
                break

            res += temp_char
            max_len = temp_max
        return res


if __name__ == '__main__':
    res = Solution().longestCommonPrefix(["dog", "racecar", "car"])
    print(res)
    res = Solution().longestCommonPrefix([""])
    print(res)

    res = Solution().longestCommonPrefix(["a"])
    print(res)

    res = Solution().longestCommonPrefix(["flower", "fow", "flight"])
    print(res)

    res = Solution().longestCommonPrefix(["lower", "iow", "flight"])
    print(res)

    res = Solution().longestCommonPrefix(["flower", "flow", "flight"])
    print(res)
