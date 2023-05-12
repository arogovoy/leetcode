# 292. Nim Game


class Solution:
    def canWinNim2(self, n: int) -> bool:
        res = False
        queue = [[n]]
        while queue:
            current_level = queue.pop(-1)
            res = not res
            level = []
            for x in current_level:
                t = [x - i for i in (3, 2, 1) if x - i > 0]
                if len(t) == 3:
                    level.extend(t)
            if len(level):
                queue.append(level)
        return res

    def canWinNim1(self, n: int) -> bool:
        if n <= 3:
            return True
        return not (self.canWinNim(n - 3) and self.canWinNim(n - 2) and self.canWinNim(n - 1))

    def canWinNim(self, n: int) -> bool:
        if n <= 3:
            return True
        return n % 4 != 0


if __name__ == '__main__':
    print(Solution().canWinNim(1348820612))
    # print(Solution().canWinNim(5))
    # print(Solution().canWinNim(4))
    # print(Solution().canWinNim(1))
    # print(Solution().canWinNim(2))
