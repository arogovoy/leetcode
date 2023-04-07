# 191. Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            bit = n >> i
            res += bit
            n -= bit << i

        return res


if __name__ == '__main__':
    print(Solution().hammingWeight(3))
    print(Solution().hammingWeight(12))
