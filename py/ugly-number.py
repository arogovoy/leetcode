# 263. Ugly Number

class Solution:
    def isUgly2(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        div2 = not n % 2 and self.isUgly(n // 2)
        div3 = not div2 and not n % 3 and self.isUgly(n // 3)
        div5 = not div3 and not n % 5 and self.isUgly(n // 5)
        return div2 or div3 or div5

    def isUgly(self, n: int) -> bool:
        for p in 2, 3, 5:
            while n % p == 0 < n:
                n /= p
        return n == 1


if __name__ == '__main__':
    print(Solution().isUgly(6))
    print(Solution().isUgly(1))
    print(Solution().isUgly(14))
    print(Solution().isUgly(-2147483648))
