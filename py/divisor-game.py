# 1025. Divisor Game


class Solution:
    def divisorGame(self, n: int) -> bool:
        alice_visited = {}
        bob_visited = {}

        def check_win(v: int, alice: bool):
            hash_map = alice_visited if alice else bob_visited

            if v in hash_map or v == 1:
                return False

            for x in range(1, v):
                if v % x == 0 and not check_win(v - x, not alice):
                    return True

            hash_map[v] = True

            return False

        return check_win(n, True)


if __name__ == '__main__':
    res = Solution().divisorGame(5)
    print(res)

    # res = Solution().divisorGame(2)
    # print(res)
    #
    # res = Solution().divisorGame(3)
    # print(res)
    #
    # res = Solution().divisorGame(4)
    # print(res)
