# 258. Add Digits


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        num %= 9
        return 9 if num == 0 else num


if __name__ == '__main__':
    print(Solution().addDigits(38))
    print(Solution().addDigits(0))
