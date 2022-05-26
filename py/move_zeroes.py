# 283. Move Zeroes
#
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
# elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
# Input: nums = [0]
# Output: [0]

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0
        n = len(nums) - 1

        while l < n and r < n:
            while r < n and nums[r + 1] == 0:
                r += 1

            if r < n and nums[l] == 0:
                nums[l], nums[r + 1] = nums[r + 1], nums[l]
                r += 1
            l += 1

            if r < l:
                r = l

        return nums


if __name__ == '__main__':
    res = Solution().moveZeroes([4,2,4,0,0,3,0,5,1,0])
    print(res)

    res = Solution().moveZeroes([1, 0, 1])
    print(res)

    res = Solution().moveZeroes([0,1,0,3,12])
    print(res)

    res = Solution().moveZeroes([0, 1, 0, 3, 12, 0])
    print(res)

    res = Solution().moveZeroes([0])
    print(res)
