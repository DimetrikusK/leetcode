from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_s = s.split(' ')
        pat = list(pattern)
        if len(split_s) != len(pat):
            return False
        else:
            for i in range(0,len(split_s)):
                print(split_s.index(split_s[i]))
                if split_s.index(split_s[i]) != pat.index(pat[i]):
                    return False
            return True


pattern = "aaa"
s = "aa aa aa"
test = Solution()
print(test.wordPattern(pattern, s))
