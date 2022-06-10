# 338. Counting Bits
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        a = [0] * (n + 1)

        for x in range(1, n + 1):
            mod = x % 4
            if mod == 0:
                a[x] = a[x // 4]
            elif mod == 3:
                a[x] = a[x - 1] + 1
            else:
                a[x] = a[x - mod] + 1

        return a


if __name__ == '__main__':
    res = Solution().countBits(64)
    print(res)

    res = Solution().countBits(2)
    print(res)

    res = Solution().countBits(5)
    print(res)

    res = Solution().countBits(0)
    print(res)
