# 136. Single Number
from typing import List


class Solution:
    def singleNumber2(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            if not nums[i] in hash_map:
                hash_map[nums[i]] = 0
            hash_map[nums[i]] = hash_map[nums[i]] + 1

        for k, v in hash_map.items():
            if v == 1:
                return k

    def singleNumber(self, nums):
        # Another thing important is, just as the asker mentioned, XOR operator is commutative; means:
        # A^B=B^A
        # e.g, 5^43^10 = 10^43^5= 43^5^10 =36
        # So, XOR {2,1,4,5,2,4,1} one by one is same as XOR{2,2,4,4,1,1,5};
        # And since A^A=0, so:
        # So ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5.
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == '__main__':
    res = Solution().singleNumber([2, 2, 1])
    print(res)

    res = Solution().singleNumber([4, 1, 2, 1, 2])
    print(res)

    res = Solution().singleNumber([1])
    print(res)
