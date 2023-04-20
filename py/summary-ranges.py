# 228. Summary Ranges
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            start = i
            end = i
            while end + 1 < len(nums) and nums[end + 1] - nums[end] == 1:
                end += 1

            res.append(str(nums[start]) if start == end else f'{nums[start]}->{nums[end]}')
            i = end + 1

        return res


if __name__ == '__main__':
    print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
    print(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))
    print(Solution().summaryRanges([0]))
    print(Solution().summaryRanges([0, 1]))
    print(Solution().summaryRanges([0, 5]))
