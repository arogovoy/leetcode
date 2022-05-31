# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        start, end = 0, 0
        l = len(s)
        res, temp_res = 0, 0
        while end < l:
            # not found
            if s.find(s[end], start, end) == -1:
                end += 1
                temp_res += 1
                res = res if temp_res < res else temp_res
            else:
                res = res if temp_res < res else temp_res
                start += 1
                end = start
                temp_res = 0

        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans


if __name__ == '__main__':
    # res = Solution().lengthOfLongestSubstring(" ")
    # print(res)
    #
    # res = Solution().lengthOfLongestSubstring("dvdf")
    # print(res)

    res = Solution().lengthOfLongestSubstring('abcabcbb')
    print(res)

    # res = Solution().lengthOfLongestSubstring('bbbbb')
    # print(res)
    #
    # res = Solution().lengthOfLongestSubstring('pwwkew')
    # print(res)
    #
    # res = Solution().lengthOfLongestSubstring('')
    # print(res)
