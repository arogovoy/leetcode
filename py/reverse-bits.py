# 190. Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            bit = n >> i
            res += bit << 31 - i
            n -= bit << i

        return res


if __name__ == '__main__':
    print(Solution().reverseBits(43261596))
    print(Solution().reverseBits(4294967293))  # 10111111111111111111111111111111 -> 10111111111111111111111111111111
