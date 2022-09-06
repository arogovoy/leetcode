# 66. Plus One
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        need_increase = True
        i = len(digits) - 1

        while need_increase and i >= 0:
            need_increase = digits[i] == 9
            digits[i] = digits[i] + 1 if not need_increase else 0
            i -= 1

        if need_increase:
            digits.insert(0, 1)

        return digits


if __name__ == '__main__':
    res = Solution().plusOne([1,2,3])
    print(res)

    res = Solution().plusOne([4,3,2,1])
    print(res)

    res = Solution().plusOne([9])
    print(res)
