# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        first, last = 0, len(s) - 1
        while first < last:
            while first < last and not s[first].isalnum():
                first = first + 1

            while first < last and not s[last].isalnum():
                last = last - 1

            if s[first] != s[last]:
                return False
            first = first + 1
            last = last - 1

        return True


if __name__ == '__main__':
    res = Solution().isPalindrome('aba')
    print(res)  # false

    res = Solution().isPalindrome('80P')
    print(res)  #false

    res = Solution().isPalindrome('A man, a plan, a canal: Panama')
    print(res)  #true

    res = Solution().isPalindrome('race a car')
    print(res) #false

    res = Solution().isPalindrome(' ')
    print(res) #true
