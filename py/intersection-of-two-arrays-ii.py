# 349. Intersection of Two Arrays
from typing import List


class Solution:
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        hash_map = {}
        for x in nums1:
            if x not in hash_map:
                hash_map[x] = 0
            hash_map[x] += 1

        res = []
        for x in nums2:
            if x in hash_map and hash_map[x] > 0:
                hash_map[x] -= 1
                res.append(x)

        return res

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return res


if __name__ == '__main__':
    print(Solution().intersect([1, 2, 2, 1], [2, 2]))
    print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))
