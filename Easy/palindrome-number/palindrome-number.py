class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False


x = 121
y = -344
test = Solution()
print(test.isPalindrome(x), test.isPalindrome(y), sep='\n')