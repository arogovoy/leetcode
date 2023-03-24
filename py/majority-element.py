# 169. Majority Element
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        x = nums[0]

        for n in nums:
            if n == x:
                count += 1
            else:
                if count == 0:
                    x = n
                else:
                    count -= 1
        return x


if __name__ == '__main__':
    res = Solution().majorityElement([3, 2, 3])
    print(res)

    res = Solution().majorityElement([1, 1, 1, 1, 5, 5])
    print(res)

    res = Solution().majorityElement([5, 5, 1, 1, 1, 1])
    print(res)

    res = Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
    print(res)

    res = Solution().majorityElement([1, 1, 2, 2, 1, 2, 2])
    print(res)

    res = Solution().majorityElement([3, 3, 4])
    print(res)

    res = Solution().majorityElement([3, 4, 4])
    print(res)

    res = Solution().majorityElement([8, 8, 7, 7, 7])
    print(res)
