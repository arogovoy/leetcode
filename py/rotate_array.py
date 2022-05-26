# 189. Rotate Array
#
# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
# Follow up:
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
from typing import List


# def rotate(self, nums: List[int], k: int) -> None:
#     if k == 0:
#         return nums
#
#     k = k if (k - len(nums)) <= 0 else k - len(nums)
#
#     last = len(nums) - 1
#     i = 0
#     while i + k <= last:
#         for j in range(k - 1, -1, -1):
#             nums[i], nums[last - j] = nums[last - j], nums[i]
#             i += 1
#     return nums

class Solution:
    def reverse(self, nums: List[int], start: int, end: int):
        m = (start + end) // 2
        j = 0
        for i in range(start, m + 1):
            nums[i], nums[end - j] = nums[end - j], nums[i]
            j += 1

    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        if k == 0 or length == k:
            return nums

        k = k if (k - length) <= 0 else k % length

        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, length - 1)

        return nums


if __name__ == '__main__':
    res = Solution().rotate([0, 1, 2, 3, 4, 5, 6], 3)
    print(res)

    res = Solution().rotate([-1, -100, 3, 99], 2)
    print(res)

    res = Solution().rotate([1, 2], 0)
    print(res)

    res = Solution().rotate([1, 2], 2)
    print(res)

    res = Solution().rotate([1, 2, 3], 4)
    print(res)

    res = Solution().rotate([1, 2, 3, 4, 5, 6], 4)
    print(res)

    res = Solution().rotate(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27], 38)
    print(res)

    res = Solution().rotate([1, 2], 5)
    print(res)
