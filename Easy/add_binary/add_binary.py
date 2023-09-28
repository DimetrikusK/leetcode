def addBinary(a, b):
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
        matchA = []
        matchB = []
        result = ''
        flag = 0
        for i in a:
            matchA.append(i)
        matchA.reverse()
        for i in b:
            matchB.append(i)
        matchB.reverse()
        for count, i in enumerate(matchA):
            if count - 1 == len(matchB):
                if flag > 0:
                    if i == '1' and matchB[count] == '1' or i == '0'and matchB[count] == '1' or i == '1' and matchB[count] == '0':
                        result += '0'
                elif i == '0' and matchB[count] == '1' or i == '1' and matchB[count] == '0':
                    pass
                if flag > 0:
                    if count + 1 >= len(matchA):
                        result += '1'
                    else:
                        result += '10'
                    flag = 0
                else:
                    result += '1'
            elif matchB[count] == '0' and i == '0':
                if flag > 0:
                    if count + 1 >= len(matchA):
                        result += '1'
                    else:
                        result += '10'
                    flag = 0
                else:
                    result += '0'
            elif i == '1' and matchB[count] == '1':
                if count + 1 >= len(matchA):
                    result += '1'
                else:
                    result += '0'
                flag = 1
        return str(result)


# 0 + 0 = 0
# 1 + 0 = 1
# 1 + 1 = 10
a = "11"
b = "1"
print(addBinary(a, b))
#10101


git remote add origin https://github.com/DimetrikusK/leetcode.git