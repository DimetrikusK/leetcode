def mergeTwoLists(list1, list2):
    for i in list2:
        list1.append(i)
    return sorted(list1)



one = [1, 2, 4]
two = [1, 3, 4]

print(mergeTwoLists(one, two))
