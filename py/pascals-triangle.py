# 118. Pascal's Triangle


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for lvl in range(1, numRows, 1):
            prev = res[lvl-1]
            r = []
            for j in range(len(prev)):
                left = 0 if j - 1 < 0 else prev[j - 1]
                right = prev[j]
                r.append(left + right)
            r.append(1)

            res.append(r)

        return res


if __name__ == '__main__':
    res = Solution().generate(5)
    print(res)