# 367. Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            m = (low + high) // 2
            if m * m == num:
                return True
            if m * m > num:
                high = m - 1
            else:
                low = m + 1
        return False


if __name__ == '__main__':
    print(Solution().isPerfectSquare(14))
    print(Solution().isPerfectSquare(16))
    print(Solution().isPerfectSquare(1))
    print(Solution().isPerfectSquare(4))
    print(Solution().isPerfectSquare(2))
