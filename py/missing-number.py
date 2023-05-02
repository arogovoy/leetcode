# 268. Missing Number
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (1 + n) * n // 2
        for x in nums:
            s -= x
        return s


if __name__ == '__main__':
    print(Solution().missingNumber([3, 0, 1]))
    print(Solution().missingNumber([0, 1]))
    print(Solution().missingNumber([1]))
    print(Solution().missingNumber([0]))
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
