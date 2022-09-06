# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, result = 0, ''
        max_len = max([len(a), len(b)])
        a = a[::-1]
        b = b[::-1]

        carry = 0

        while i < max_len:
            v1 = int(a[i]) if i < len(a) else 0
            v2 = int(b[i]) if i < len(b) else 0
            s = v1 + v2 + carry
            carry = 1 if s > 1 else 0
            result = (str(s) if not carry else str(s - 2)) + result
            i += 1

        if carry:
            result = '1' + result

        return result


if __name__ == '__main__':
    res = Solution().addBinary('11', "1")
    print(res)  # "100"

    res = Solution().addBinary("1010", "1011")
    print(res)  # "10101"

    res = Solution().addBinary('1111', "1111")
    print(res)  # "11110"
