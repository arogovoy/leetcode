# 704. Binary Search
#
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
# target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Constraints:
# * 1 <= nums.length <= 10^4
# * -10^4 < nums[i], target < 10^4
# * All the integers in nums are unique.
# * nums is sorted in ascending order.
#
# Example:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
# Example:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = int((l + r) / 2)
            if nums[m] < target:
                l = m + 1
            if nums[m] > target:
                r = m - 1
            if nums[m] == target:
                return m

        return -1


if __name__ == '__main__':
    res = Solution().search([-1, 0, 3, 5, 9, 12], 9)
    print(res)
    res = Solution().search([-1, 0, 3, 4, 5, 9, 12], 2)
    print(res)
    res = Solution().search([5], 5)
    print(res)