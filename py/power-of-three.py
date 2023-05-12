# 326. Power of Three
import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


if __name__ == '__main__':
    print(Solution().isPowerOfThree(243))
    print(Solution().isPowerOfThree(45))
    print(Solution().isPowerOfThree(27))
    print(Solution().isPowerOfThree(0))
    print(Solution().isPowerOfThree(-1))
