def deleteDuplicates(head):
    # res = []
    # for count, i in enumerate(head):
    #     if i != head[count - 1] and count < len(head):
    #         res.append(i)
    # res.sort()
    head = sorted(head)
    return head
    # return res


head = [1, 1, 2]
print(deleteDuplicates(head))
