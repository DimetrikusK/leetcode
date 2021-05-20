import collections


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_str = s.split()
        tmp = {}.fromkeys(pattern, [i for i in list_str ])
        print(tmp)
        list_str = s.split()
        for i in pattern:
            for j in list_str:
                if tmp[i] is None:




pattern = "abba"
s = "dog cat cat dog"
test = Solution()
print(test.wordPattern(pattern, s))
