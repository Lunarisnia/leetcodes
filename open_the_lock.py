class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        # 0202 > 0212 > 0211 > 0210 > 0110 > 0010 > 0000
        # 0202 > 1202 > 1102 > 1002 > 1001 > 1000 > 0000
        # ^                                     ^ All that matters

        lock_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i, c in enumerate(target):
            print(c)
            if int(c) != 0:
                # 4 - 2 = 2

                pass


        pass


if __name__ == '__main__':
    s = Solution()
    s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202")
