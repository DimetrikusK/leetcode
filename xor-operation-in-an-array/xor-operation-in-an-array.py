from functools import reduce


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        array = [start]
        for i in range(n - 1):
            array.append(array[-1] + 2)
        return reduce(lambda x, y: x ^ y, array)



# c = Solution()
# print(c.xorOperation(5, 0))