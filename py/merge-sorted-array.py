# 88. Merge Sorted Array
from typing import List


class Solution:
    # def merge(self, nums1, m, nums2, n):
    #     while m > 0 and n > 0:
    #         if nums1[m - 1] >= nums2[n - 1]:
    #             nums1[m + n - 1] = nums1[m - 1]
    #             m -= 1
    #         else:
    #             nums1[m + n - 1] = nums2[n - 1]
    #             n -= 1
    #     if n > 0:
    #         nums1[:n] = nums2[:n]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0: return
        for i in range(m):
            j = 0

            if nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]

            while j + 1 < n and nums2[j] > nums2[j + 1]:
                nums2[j], nums2[j + 1] = nums2[j + 1], nums2[j]
                j += 1

        for i in range(n):
            nums1[i + m], nums2[i] = nums2[i], nums1[i + m]

        return nums1


if __name__ == '__main__':
    res = Solution().merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
    print(res)

    res = Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    print(res)

    res = Solution().merge([4, 0, 0, 0, 0, 0], 1, [2, 5, 6], 3)
    print(res)
