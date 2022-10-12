from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            prev = 0
            for j in range(i):
                prev, result[j] = result[j], prev + result[j]
        return result


if __name__ == '__main__':
    res = Solution().getRow(3)
    print(res)

    res = Solution().getRow(0)
    print(res)

    res = Solution().getRow(1)
    print(res)

    res = Solution().getRow(4)
    print(res)
