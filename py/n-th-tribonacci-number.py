# 1137. N-th Tribonacci Number


class Solution:
    def tribonacci(self, n: int) -> int:
        if not n: return 0
        if n == 1 or n == 2: return 1

        t1, t2, t3 = 0, 1, 1
        s = 0
        i = 3
        while n >= i:
            i += 1
            s = t1 + t2 + t3
            t1, t2, t3 = t2, t3, s

        return s


if __name__ == '__main__':
    res = Solution().tribonacci(37)
    print(res)

    res = Solution().tribonacci(2)
    print(res)

    res = Solution().tribonacci(4)
    print(res)

    res = Solution().tribonacci(25)
    print(res)

    res = Solution().tribonacci(0)
    print(res)
