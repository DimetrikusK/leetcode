class Solution:
    def plusOne(self, digits):
        if digits[-1] != 9:
            digits[-1] += 1
            return digits[-1]
        else:
            digits.append(0)
            return digits[-2::-1]



digits = [4, 3, 2, 1]
test = Solution()
print(test.plusOne(digits))
