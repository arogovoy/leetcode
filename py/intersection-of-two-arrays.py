# 349. Intersection of Two Arrays
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        for x in nums1:
            if x not in hash_map:
                hash_map[x] = 1

        for x in nums2:
            if x in hash_map:
                hash_map[x] += 1

        return [key for key, value in hash_map.items() if value > 1]


if __name__ == '__main__':
    print(Solution().intersection([1, 2, 2, 1], [2, 2]))
    print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
