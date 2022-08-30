# 26. Remove Duplicates from Sorted Array


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, i, res = 0, 1, 1
        length = len(nums)

        while i < length and k < length - 1:
            if nums[i] <= nums[i - 1]:
                while k < length - 1 and nums[k] <= nums[i - 1]:
                    k += 1
                nums[i], nums[k] = nums[k], nums[i]

            if nums[i] > nums[i - 1]:
                res += 1
            i += 1

        return res


if __name__ == '__main__':
    res = Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(res)

    res = Solution().removeDuplicates([1, 1])
    print(res)

    res = Solution().removeDuplicates([1, 2])
    print(res)
