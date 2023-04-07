# 171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alph_len = 26
        res = 0
        for i in range(len(columnTitle)):
            res += pow(alph_len, i) * (((ord(columnTitle[len(columnTitle) - i - 1]) - ord('A')) % alph_len) + 1)

        return res


if __name__ == '__main__':
    print(Solution().titleToNumber('A'))  # 1
    print(Solution().titleToNumber('AB'))  # 28
    print(Solution().titleToNumber('ZY'))  # 701
