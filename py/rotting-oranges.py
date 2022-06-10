# 994. Rotting Oranges
# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible,
# return -1.
#
# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten,
#  because rotting only happens 4-directionally.
# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

from typing import List


class Solution:
    def isFresh(self, grid: List[List[int]], i: int, j: int) -> bool:
        return 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh_orange_count = 0
        queue = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh_orange_count += 1

        if not fresh_orange_count:
            return 0

        next_tick = []

        while queue:
            el = queue.pop(0)
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                col, row = i + el[0], j + el[1]
                if self.isFresh(grid, col, row):
                    grid[col][row] = 2
                    next_tick.append([col, row])
                    fresh_orange_count -= 1

            if not queue and next_tick:
                queue = next_tick
                minutes += 1
                next_tick = []

        return minutes if not fresh_orange_count else -1


if __name__ == '__main__':
    res = Solution().orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]])
    print(res)  # 2

    res = Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    print(res)

    res = Solution().orangesRotting([[1]])
    print(res)
    #
    res = Solution().orangesRotting([[0, 2]])
    print(res)
