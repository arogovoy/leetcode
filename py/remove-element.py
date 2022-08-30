# 27. Remove Element


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        l = len(nums)
        for i in range(l - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[l - count - 1] = nums[l - count - 1], nums[i]
                count += 1

        return l - count


if __name__ == '__main__':
    res = Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    print(res)

    res = Solution().removeElement([3, 2, 2, 3], 3)
    print(res)
