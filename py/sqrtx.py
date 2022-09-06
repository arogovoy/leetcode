# 67. Add Binary

class Solution:
    def mySqrt(self, x: int) -> int:
        m, left, right = 0, 0, x

        while left < right:
            m = left + int((right - left) / 2)
            s = m * m

            if s == x:
                return m

            if s < x:
                left = m + 1

            if s > x:
                right = m - 1

        return left - 1 if left * left > x else left


if __name__ == '__main__':
    res = Solution().mySqrt(6)
    print(res)  # 2
    assert res == 2, f"got: {res}"

    res = Solution().mySqrt(5)
    print(res)  # 2
    assert res == 2, f"got: {res}"

    res = Solution().mySqrt(3)
    print(res)  # 1
    assert res == 1, f"got: {res}"

    res = Solution().mySqrt(2)
    print(res)  # 1
    assert res == 1, f"got: {res}"

    res = Solution().mySqrt(4)
    print(res)  # 2
    assert res == 2, f"got: {res}"

    res = Solution().mySqrt(8)
    print(res)  # 2
    assert res == 2, f"got: {res}"

    res = Solution().mySqrt(0)
    print(res)  # 0
    assert res == 0, f"got: {res}"

    res = Solution().mySqrt(1)
    print(res)  # 1
    assert res == 1, f"got: {res}"

    res = Solution().mySqrt(10)
    print(res)  # 3
    assert res == 3, f"got: {res}"

    res = Solution().mySqrt(16)
    print(res)  # 4
    assert res == 4, f"got: {res}"
