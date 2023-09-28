class Solution:
    def isValid(self, s: str) -> bool:
        check = {')': 0,
                 '(': 0,
                 '[': 0,
                 ']': 0,
                 '{': 0,
                 '}': 0}
        for i in s:
            check[i] += 1
        for count, i in enumerate(check):
            if i == ')' and check[i] != check['(']:
                return False
            elif i == ']' and check[i] != check['[']:
                return False
            elif i == '}' and check[i] != check['{']:
                return False
        return True




# is_valid = '{()(){}[]{}}'
# test = Solution()
# print(test.isValid(is_valid))
# for count, i in enumerate(s):
#     if int(len(s)) // 10 != 0:
#         return False
#     if count == 0:
#         return False
#     elif i == ')' and s[count - 1] != '(' or count > len(s):
#         return False
#     elif i == ']' and s[count - 1] != '[' or count > len(s):
#         return False
#     elif i == '}' and s[count - 1] != '{' or count > len(s):
#         return False
# return True