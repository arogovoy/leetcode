# 784. Letter Case Permutation
# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
#
# Return a list of all possible strings we could create. Return the output in any order.
#
# Example 1:
# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:
# Input: s = "3z4"
# Output: ["3z4","3Z4"]

from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        char = s[0]
        low = char.lower()
        upper = char.upper()

        if len(s) == 1:
            return [s] if low == upper else [s.lower(), s.upper()]

        result = []
        permutations = self.letterCasePermutation(s[1:len(s)])
        for i in range(len(permutations)):
            if low == upper:
                result.append(char + permutations[i])
            else:
                result.append(low + permutations[i])
                result.append(upper + permutations[i])

        return result


if __name__ == '__main__':
    res = Solution().letterCasePermutation('a1b2')
    print(res)

    # res = Solution().permute([0, 1])
    # print(res)
    #
    # res = Solution().permute([1])
    # print(res)
