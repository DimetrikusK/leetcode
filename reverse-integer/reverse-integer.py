class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x > 0 else -1
        str_x = str(abs(x))
        revers_x = int(str_x[::-1]) * flag
        if revers_x > ((2**31) - 1) or revers_x < ((-2**31) + 1):
            return 0
        else:
            return revers_x




# x = -2147483648
# c = Solution()
# print((c.reverse(x)))
