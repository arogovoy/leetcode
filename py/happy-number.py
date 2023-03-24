# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        r = n

        while r != 1:
            x = 0

            while r:
                x += pow(r % 10, 2)
                r = int(r / 10)

            r = x

            if r == 4:
                return False

        return True


if __name__ == '__main__':
    res = Solution().isHappy(3)
    print(res)

    # res = Solution().isHappy(19)
    # print(res)
    #
    # res = Solution().isHappy(7)
    # print(res)
    #
    # res = Solution().isHappy(2)
    # print(res)
