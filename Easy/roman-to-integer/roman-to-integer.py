class Solution:
    def __init__(self):
        self.romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.result = int()

    def romanToInt(self, s: str) -> int:

        for i in s:
            self.result += self.romanDict[i]

        for index, value in enumerate(s):
            if index < len(s) - 1:
                if value == 'I' and (s[index + 1] == 'V' or s[index + 1] == 'X'):
                    self.result -= 1 * 2
                elif value == 'X' and (s[index + 1] == 'L' or s[index + 1] == 'C'):
                    self.result -= 10 * 2
                elif value == 'C' and (s[index + 1] == 'D' or s[index + 1] == 'M'):
                    self.result -= 100 * 2
        return self.result



# s = Solution()
# print(s.romanToInt('MMCCCXCIX'))
# 2399