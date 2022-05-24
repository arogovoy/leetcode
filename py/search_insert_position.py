# 35. Search Insert Position
#
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m

            if nums[m] < target:
               l = m + 1
            else:
                r = m - 1
        return l



if __name__ == '__main__':
    res = Solution().searchInsert([1, 3, 5, 6], 5)
    print(res)

    res = Solution().searchInsert([1, 3, 5, 6], 2)
    print(res)

    res = Solution().searchInsert([1, 3, 5, 6], 7)
    print(res)
