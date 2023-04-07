# 217. Contains Duplicate
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for x in nums:
            if x in values:
                return True
            values[x] = True
        return False


if __name__ == '__main__':
    print(Solution().containsDuplicate([1, 2, 3, 1]))
    print(Solution().containsDuplicate([1, 2, 3, 4]))
