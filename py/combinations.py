# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
#
# You may return the answer in any order.
#
# Example 1:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(n, k, res, [], 1)
        return res

    def backtrack(self, n, k, res, path, index):
        if len(path) == k:
            res.append(path)
            return
        for i in range(index, n + 1):
            self.backtrack(n, k, res, path + [i], i + 1)


if __name__ == '__main__':
    # res = Solution().combine(2, 1)
    # print(res)

    res = Solution().combine(4, 2)
    print(res)

    # res = Solution().combine(1, 1)
    # print(res)
