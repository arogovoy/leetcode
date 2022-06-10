# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#
# Example 3:
# Input: nums = [1]
# Output: [[1]]
from typing import List


class Solution1:
    def combinations(self, arr: List[int], v: int):
        result = []
        for i in range(len(arr) + 1):
            t, k = [], 0
            for j in range(len(arr) + 1):
                if i != j:
                    t.append(arr[k])
                    k += 1
                else:
                    t.append(v)

            result.append(t)
        return result

    def append(self, i: int, nums: List[int], variants: List[List[int]]):
        if i >= len(nums):
            return variants
        result = []
        for j in range(len(variants)):
            result += self.combinations(variants[j], nums[i])
        return self.append(i + 1, nums, result)

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.append(1, nums, [[nums[0]]])

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [[nums[0]]]

        for i in range(len(nums)):
            v = nums.pop(0)
            combinations = self.permute(nums)
            for j in range(len(combinations)):
                combinations[j].append(v)
            result.extend(combinations)
            nums.append(v)

        return result


if __name__ == '__main__':
    res = Solution().permute([1, 2, 3])
    print(res)

    # res = Solution().permute([0, 1])
    # print(res)
    #
    # res = Solution().permute([1])
    # print(res)
