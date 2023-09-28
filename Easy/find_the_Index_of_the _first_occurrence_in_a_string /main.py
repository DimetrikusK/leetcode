class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            print(haystack.find(needle))
        else:
            return -1






haystack = "sadbutsad"
needle = "sad"

test = Solution()
print(test.strStr(haystack, needle))
