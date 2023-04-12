# 231. Power of Two
import math


class Solution:

    def isPowerOfTwo3(self, n: int) -> bool:
        if n < 1:
            return False
        return (n & (n - 1)) == 0
    def isPowerOfTwo2(self, n: int) -> bool:
        while n and not n % 2:
            n /= 2

        return n == 1

    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return math.log2(n).is_integer()


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(3))
    print(Solution().isPowerOfTwo(12))
    print(Solution().isPowerOfTwo(8))
    print(Solution().isPowerOfTwo(1))
    print(Solution().isPowerOfTwo(0))
    print(Solution().isPowerOfTwo(-2))
