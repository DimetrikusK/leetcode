# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        st1, st2 = '', ''
        while l1:
            st1 += str(l1.val)
            l1 = l1.next
        while l2:
            st2 += str(l2.val)
            l2 = l2.next

        reversOne = st1[::-1]
        reversTwo = st2[::-1]
        summa = str(int(reversOne) + int(reversTwo))
        result = [int(i) for i in summa[::-1]]
        return result


# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
