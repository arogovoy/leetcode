# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        sum_left, sum_right = 1, 1
        for x in range(2, n + 1, 1):
            sum_right, sum_left = sum_left, sum_left + sum_right
        return sum_left


if __name__ == '__main__':
    res = Solution().climbStairs(2)
    print(res)  # 2

    res = Solution().climbStairs(6)
    print(res)  # 3
