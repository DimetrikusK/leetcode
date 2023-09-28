def calPoints(operations):
    tablo = []
    for count, i in enumerate(operations):
        if i == 'x':
            tablo = []
        elif i == '+':
            tablo.append(tablo[-2] + tablo[-1])
        elif i == 'D':
            tablo.append(tablo[-1] * 2)
        elif i == 'C':
            tablo.pop()
        else:
            tablo.append(int(i))
    return sum(tablo)







ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops))

# x - новая запись
# + - Запишите новый результат, который представляет собой сумму двух предыдущих баллов
# D - Запишите новый результат, в два раза превышающий предыдущий.
# C - Аннулировать предыдущий результат, удалив его из записи.
