from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_str = s.split()
        tmp1, tmp2 = defaultdict(set), defaultdict(set)
        for i, j in zip(pattern, list_str):
            tmp1[i].add(j)
            tmp2[j].add(i)

        for i, j in zip(pattern, list_str):
            if len(tmp1[i]) != 1 or len(tmp2[j]) != 1:
                return False
        return True


pattern = "abba"
s = "dog cat cat dog"
test = Solution()
print(test.wordPattern(pattern, s))
