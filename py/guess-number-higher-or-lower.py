# 374. Guess Number Higher or Lower

def guess(num: int) -> int:
    if num > pick:
        return -1
    if num < pick:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        m = n
        s = 1
        while guess(m) != 0:
            m = (n + s) // 2
            if guess(m) == -1: # higher
                n = m - 1
            else: # lower
                s = m + 1
        return m


if __name__ == '__main__':
    pick = 6
    print(Solution().guessNumber(10))
    pick = 1
    print(Solution().guessNumber(1))
    pick = 1
    print(Solution().guessNumber(2))
