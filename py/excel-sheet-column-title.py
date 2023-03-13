# 168. Excel Sheet Column Title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''

        while columnNumber:
            c = ord('A') + (columnNumber - 1) % 26
            result = chr(c) + result
            columnNumber = int((columnNumber - 1) / 26)

        return result


if __name__ == '__main__':
    res = Solution().convertToTitle(1)
    print(res)  # A

    res = Solution().convertToTitle(28)
    print(res)  # AB

    res = Solution().convertToTitle(701)
    print(res)  # ZY
