# 977. Squares of a Sorted Array
#
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
#
# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a
# different approach?
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        i = right
        res = [0] * len(nums)
        while left <= right:
            s1 = nums[left] * nums[left]
            s2 = nums[right] * nums[right]
            if s1 >= s2:
                res[i] = s1
                left += 1
            else:
                res[i] = s2
                right -= 1
            i -= 1

        return res


if __name__ == '__main__':
    res = Solution().sortedSquares([-4, -1, 0, 3, 10])
    print(res)

    res = Solution().sortedSquares([-7, -3, 2, 3, 11])
    print(res)
